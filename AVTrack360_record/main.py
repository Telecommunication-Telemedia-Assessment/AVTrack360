"""
This is the main class of the recording tool of AVTrack360.
AVTrack360 is able to get the head orientation of the user by accessing the sensors of the HTC Vive.
It currently only works with Windows 7+.

@author: Stephan Fremerey
"""

import colorama
import helpers
import json
import keyboard
import open_player as player
import os
#import rift
import time
import vive
from argparse import ArgumentParser
from colorama import Fore


parser = ArgumentParser(description="AVTrack360 is a software for playing a 360 video and the synchronised tracking of"
                                    " the head movement data with several devices.")
parser.add_argument("-skip", dest="skip_tracking_enabled", default=False, action='store_true',
                    help="Add this parameter if you do not want to record the head movement data.")
parser.add_argument("-autoplay", dest="autoplay_enabled", default=False, action='store_true',
                    help="Add this parameter if you want to enable the automatic video play function with short delay.")
parser.add_argument("-multiplay", dest="multiplay", default=0, help="Add this parameter if you want to play"
                                                                      " multiple videos one after another"
                                                                      " without a break. Also specify the number of "
                                                                    "videos to play in one row.", type=int)
parser.add_argument("-acr", dest="acr", default=False, action="store_true", help="After every video played back display"
                                                                                 " a dialog to save the ACR score.")
parser.add_argument("-overwrite", dest="overwrite_enabled", default=False, action='store_true',
                    help="Add this parameter if you want to delete already existing filename/HMD combinations in the"
                         " already existing dataset when writing the data.")
parser.add_argument("-videolength", dest="videolength", default=0, type=float)
parser.add_argument("-captureviewport", dest="captureviewport", default=False, action='store_true',
                    help="Add this parameter if you want to enable the capturing of the viewport shown by Whirligig.")
parser.add_argument("-player", dest="player", default="whirligig",
                    help="The 360 player you want to use. (Available: Whirligig, Default: Whirligig)", type=str)
parser.add_argument("-plist", dest="playlist", default="1 Demo.json",
                    help="The path of the playlist you want to play. Default: 1 Demo.json", type=str)


colorama.init()  # Initialization of colorama for colored prints
# Parse arguments and load playlist json file.
arg = parser.parse_args()
with open('playlists\\' + arg.playlist, mode='r') as playlist_file:
    playlist_data = json.load(playlist_file)
label = playlist_data['label']
video_counter = 0

# Check whether every video of the playlist is placed in the respective folder. If not, exit AVTrack360.
missing_videos = []
for video_no in range(0, len(playlist_data['videos'])):
    if not os.path.isfile('videos\\' + playlist_data['videos'][video_no]['filename']):
        missing_videos.append(playlist_data['videos'][video_no]['filename'])
if len(missing_videos) != 0:
    for missing_video in missing_videos:
        print(Fore.LIGHTMAGENTA_EX + "The video '" + missing_video +
               "' is not placed in the respective folder." + Fore.WHITE)
    print(Fore.LIGHTRED_EX + "AVTrack360 will exit now." + Fore.WHITE)
    os._exit(0)

# Check whether the dataset we want to create is already available.
# If yes, inform the user that it should be deleted.
if os.path.isfile('data\\' + label + '.json'):
    print((Fore.LIGHTYELLOW_EX + "IMPORTANT NOTE: The data you record will be added to an already existing dataset! " \
          "Please check the data folder and maybe delete the already existing JSON file "
          + label + ".json" + Fore.WHITE))

# Loop over every video of the playlist and open them successively in Whirligig.
while len(playlist_data['videos']) > 0:
    filename = playlist_data['videos'][0]['filename']
    video_path = os.getcwd() + "\\videos\\" + filename  # Get full path of the video
    projection_scheme = playlist_data['videos'][0]['projection_scheme']
    hmd = playlist_data['videos'][0]['hmd']
    # Get the exact length of the video itself by playlist or by set parameter (without attached greyscreen and ACR scale)
    if arg.videolength == 0:
        video_length_in_s = float(playlist_data['videos'][0]['duration'])
    else:
        video_length_in_s = float(arg.videolength)

    setup_next_video = False
    print(Fore.LIGHTGREEN_EX + "You should be using the HMD '" + hmd + "' now." + Fore.WHITE)
    if arg.multiplay != 0:
        # If already played x PVSs, reset the counter and wait for the test supervisor starting the next session
        if video_counter == arg.multiplay:
            video_counter = 0
            print("Press the ENTER key if the next video session should start. %s videos left in playlist."
                  % (len(playlist_data['videos'])))
            while setup_next_video == False:
                if keyboard.is_pressed("enter"):
                    setup_next_video = True
        else:
            print("The subject still has to watch %s videos. Starting the next video..."
                  % ((arg.multiplay - video_counter)))
            time.sleep(float(0.5))
    else:
        print("Press the ENTER key if the next video should start.")
        while setup_next_video == False:
            if keyboard.is_pressed("enter"):
                setup_next_video = True

    # If we want to track the head movement data, record it and save it to a JSON file.
    if not arg.skip_tracking_enabled:
        # Opening the video in the player if Rift or Vive used.
        if hmd == "rift" or hmd == "vive":
            process_name = player.open_player(arg.player, video_path, filename, projection_scheme, hmd)
        if hmd == "rift":
            rift.rift(label, filename, video_length_in_s, process_name, arg.autoplay_enabled, arg.overwrite_enabled, arg.acr, arg.captureviewport)
        elif hmd == "vive":
            vive.vive(label, filename, video_length_in_s, process_name, arg.autoplay_enabled, arg.overwrite_enabled, arg.acr, arg.captureviewport)
        else:
            print(Fore.LIGHTRED_EX + "This HMD is not supported at yet." + Fore.WHITE)
    # If we do not want to track the head movement data, just play the videos.
    else:
        process_name = player.open_player(arg.player, video_path, projection_scheme, hmd)
        while helpers.is_process_running(process_name):
            time.sleep(0.1)

    # If no videos are available anymore, exit the application.
    if len(playlist_data['videos']) == 1:
        print("No next video available. AVTrack360 will exit now.")
        os._exit(0)
    # If the next used HMD is another one as the actual used HMD, wait until the user plugged in the other HMD
    # and pressed the ENTER-key.
    if playlist_data['videos'][0]['hmd'] != playlist_data['videos'][1]['hmd']:
        print("Please plug in the " + playlist_data['videos'][1]['hmd']\
              + " HMD to continue. If you are ready with the setup, press the ENTER-key.")
        print("Next video to be played is video " + playlist_data['videos'][1]['filename'] + ".")
        hmd_plugged_in = False
        while hmd_plugged_in == False:
            if keyboard.is_pressed("enter"):
                hmd_plugged_in = True
                print("Plugged in the other HMD. AVTrack360 will continue now.")
    # Omit the played video in the playlist and overwrite the existing playlist.
    del playlist_data['videos'][0]
    video_counter += 1
    with open('playlists\\' + arg.playlist, mode='w') as updated_playlist:
        json.dump(playlist_data, updated_playlist, indent=4,
                  sort_keys=True, separators=(',', ':'))
