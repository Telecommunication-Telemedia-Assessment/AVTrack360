"""
This script opens a 360 video in a respective player.
Also refer to http://www.whirligig.xyz/command-line
It currently only works with Windows 7+.

@author: Stephan Fremerey
"""

import helpers
import os
import pyautogui
import thread
import time
from subprocess import check_output  # For accessing the command line


def open_player(player_name, video_path, filename, projection_scheme, hmd):
    """
    This script opens a 360 video in a respective player.

    :param player_name: Name of the player to use.
    :param video_path: The path of the video to play.
    :param filename: The filename of the video to play.
    :param projection_scheme: The projection scheme of the video to play.
    :param hmd: The name of the HMD to use.
    """
    if player_name == "whirligig":
        try:
            # If Whirligig is already opened, kill it
            whirligig_opened = helpers.is_process_running("Whirligig64bit.exe")
            while whirligig_opened:
                helpers.kill_windows_process("Whirligig64bit.exe")
                whirligig_opened = helpers.is_process_running("Whirligig64bit.exe")

            thread.start_new_thread(open_whirligig, ("videos\\" + filename, projection_scheme))
            if hmd == "vive" or hmd == "rift":
                # For HTC Vive wait a short moment until Whirligig player gets opened. Then set the window focus to it.
                time.sleep(float(2))
                helpers.set_window_focus("Whirligig", "UnityWndClass")
            return "Whirligig64bit.exe"  # Return the process name for later exiting of the player
        except:
            print("Error: unable to start Whirligig player.")


def open_whirligig(source, projection_scheme):
    """
    This script opens a 360 video in Whirligig by using the Command Line Arguments ability of Whirligig.
    Refer to http://www.whirligig.xyz/command-line

    :param source: Filepath to the video.
    :param projection_scheme: Projection scheme to use for playback.
    :return:
    """
    check_output("tools\Whirligig\Whirligig64bit.exe -feature " + source + " -continousplay on -projection " +
                 projection_scheme + " -whenmediaends quit", shell=False).decode()
