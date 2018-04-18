"""
This script gets the 3 rotation angles Pitch/Yaw/Roll around the 3 Axes X/Y/Z by accessing the sensors of the HTC Vive.
It currently only works with Windows 7+.

@author: Stephan Fremerey
"""
from timeit import default_timer as timer

import helpers
import keyboard
import numpy as np
import openvr  # Python bindings for Valve's OpenVR SDK, see https://github.com/cmbruns/pyopenvr
import pyautogui
import time


def vive(label, filename, video_length_in_s, process_name, autoplay_enabled, overwrite_enabled, acr):
    """
    Obtains and saves the data captured by the HTC Vive in a JSON file.

    :param label: The label of the subject.
    :param filename: The filename of the video.
    :param video_length_in_s: The length of the video in s.
    :param process_name: The name of the process to monitor.
    :param autoplay_enabled: Whether automatic playback of the video is enabled or not.
    :param overwrite_enabled: Whether overwriting the current dataset is enabled or not.
    """
    video_playing_started = False  # Necessary for getting information about playback state of video
    data = {'filename': filename, 'video_length_in_s': float(video_length_in_s),
            'hmd': 'vive', 'pitch_yaw_roll_data_hmd': []}
    if acr:
        data["acr"] = 0

    if autoplay_enabled:
        # Sleep a few seconds until the video is completely loaded by Whirligig
        if process_name == "Whirligig64bit.exe":
            helpers.autoplay_sleep(float(4))  # Adjust value based on your computing power (between 4 and 6 is normal)
    else:
        print("If the player has loaded the video, press the SPACE key to start the measurement.")

    # Initialize OpenVR as background application, so that the player won't crash.
    openvr.init(openvr.VRApplication_Background)
    while video_playing_started == False:
        if autoplay_enabled:
            pyautogui.press("space")
            start_time = timer()
            print("Recording of Pitch/Yaw/Roll/Time data will start now..")
            video_playing_started = True
        else:
            if keyboard.is_pressed("space"):
                start_time = timer()
                print("Recording of Pitch/Yaw/Roll/Time data will start now...")
                video_playing_started = True
    try:
        pyautogui.press("r")  # Press R key to assure the user starts watching the video at initial position
        current_playback_state = timer() - start_time
        pitch, yaw, roll = getPYRDataFromVive()
        # Define the current position of the user (very first yaw value) as initial position
        initial_yaw = yaw
        # Get Head orientation data from Vive in loop until the playback is finished
        while video_length_in_s > current_playback_state:
            pitch, yaw, roll = getPYRDataFromVive()
            current_playback_state = timer() - start_time
            # Adjust the yaw value according to the very first recorded yaw value
            yaw = helpers.shift_yaw(yaw, initial_yaw)
            if current_playback_state is not None:
                data["pitch_yaw_roll_data_hmd"].append({'pitch': pitch, 'yaw': yaw, 'roll': roll,
                                                        'sec': current_playback_state})
                # By adjusting this value, you can set the recording frequency (currently 200Hz).
                time.sleep(float(0.005))
        if acr:
            data["acr"] = helpers.get_acr_by_cmd_input()
        helpers.write_to_json(label, data, overwrite_enabled)
        openvr.shutdown()
        print("Measurement done. Opening the next video if available.")
    except KeyboardInterrupt:  # Break if ctrl+c is pressed
        openvr.shutdown()
        print("Current Measurement is interrupted and will not be saved. The program will exit now.")

def getPYRDataFromVive():
    """
    Method to obtain the current pitch, yaw and roll data of the HTC Vive.

    :return: Current pitch, yaw and roll data of HTC Vive.
    """
    poses = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0,
                                                              openvr.k_unMaxTrackedDeviceCount)
    hmd_pose = poses[openvr.k_unTrackedDeviceIndex_Hmd]
    v = hmd_pose.mDeviceToAbsoluteTracking
    # Extraction of angles from rotation matrix
    # To get yaw from -180 to +180 degree, axis 0 and 1 have been switched
    pitch_rad = np.arctan2(-v[1][2], np.sqrt(np.square(v[0][2]) + np.square(v[2][2])))
    pitch = float(np.degrees(pitch_rad))

    yaw_rad = np.arctan2(v[0][2], v[2][2])
    yaw = float(np.degrees(yaw_rad))
    # Some calculations needed for Yaw value to get an equal coordinate system
    yaw_orig = yaw
    yaw = yaw + 180
    if yaw >= 180:
        yaw = yaw_orig + 180 * -1

    roll_rad = np.arctan2(v[1][0], v[1][1])
    roll = float(np.degrees(roll_rad))
    return (pitch * -1, yaw * -1, roll * -1)