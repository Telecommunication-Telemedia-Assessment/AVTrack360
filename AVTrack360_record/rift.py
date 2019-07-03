"""
This script gets the 3 rotation angles Pitch/Yaw/Roll around the 3 Axes X/Y/Z by accessing the sensors of the Oculus Rift.
It currently only works with Windows 7+.

@author: Stephan Fremerey
"""
from timeit import default_timer as timer

import helpers
import keyboard
import numpy as np
import ovr  # Python bindings for Oculus Rift SDK, see https://github.com/cmbruns/pyovr
import pyautogui
import time


def rift(label, filename, video_length_in_s, process_name, autoplay_enabled, overwrite_enabled, acr, captureviewport):
    """
    Obtains and saves the data captured by the Oculus Rift in a JSON file.

    :param label: The label of the subject.
    :param filename: The filename of the video.
    :param video_length_in_s: The length of the video in s.
    :param process_name: The name of the process to monitor.
    :param autoplay_enabled: Whether automatic playback of the video is enabled or not.
    :param overwrite_enabled: Whether overwriting the current dataset is enabled or not.
    """
    video_playing_started = False  # Necessary for getting information about playback state of video
    data = {'filename': filename, 'video_length_in_s': float(video_length_in_s),
            'hmd': 'rift', 'pitch_yaw_roll_data_hmd': []}
    if acr:
        data["acr"] = 0

    # Initialize ovr session here as otherwise the video wouldn't be shown on the Rift.
    ovr.initialize(None)
    session, luid = ovr.create()

    if autoplay_enabled:
        # Sleep a few seconds until the video is completely loaded by Whirligig
        if process_name == "Whirligig64bit.exe":
            helpers.autoplay_sleep(float(5.5))  # Adjust value based on your computing power (between 4 and 6 is normal)
    else:
        print("If the player has loaded the video, press the SPACE key to start the measurement.")

    while video_playing_started == False:
        if autoplay_enabled:
            pyautogui.press("space")
            start_time = timer()
            print("Recording of Pitch/Yaw/Roll/Time data will start now.")
            video_playing_started = True
        else:
            if keyboard.is_pressed("space"):
                start_time = timer()
                print("Recording of Pitch/Yaw/Roll/Time data will start now.")
                video_playing_started = True
    try:
        pyautogui.press("r")  # Press R key to assure the user starts watching the video at initial position
        current_playback_state = timer() - start_time
        pitch, yaw, roll = getPYRDataFromRift(session)
        # Define the current position of the user (very first yaw value) as initial position
        initial_yaw = yaw

        # Start viewport capturing if enabled
        if captureviewport:
            helpers.capture_viewport(video_length_in_s, "%s_%s" % (label, filename.split(".")[0]))

        # Get Head orientation data from Vive in loop until the playback is finished
        while video_length_in_s > current_playback_state:
            pitch, yaw, roll = getPYRDataFromRift(session)
            current_playback_state = timer() - start_time
            # Adjust the yaw value according to the very first recorded yaw value
            yaw = helpers.shift_yaw(yaw, initial_yaw)
            if current_playback_state is not None:
                data["pitch_yaw_roll_data_hmd"].append({'pitch': pitch, 'yaw': yaw, 'roll': roll,
                                                        'sec': current_playback_state})
                # print("Pitch/Yaw/Roll:  %s  /  %s  /  %s" % (int(pitch), int(yaw), int(roll)))
                # By adjusting this value, you can set the recording frequency (currently 200Hz).
                time.sleep(float(0.005))
        if acr:
            data["acr"] = helpers.get_acr_by_cmd_input()
        helpers.write_to_json(label, data, filename.split(".")[0], overwrite_enabled)
        ovr.destroy(session)
        ovr.shutdown()
        print("Measurement done. Opening the next video if available.")
    except KeyboardInterrupt:  # Break if ctrl+c is pressed
        ovr.destroy(session)
        ovr.shutdown()
        print("Current Measurement is interrupted and will not be saved. The program will exit now.")

def getPYRDataFromRift(session):
    """
    Method to obtain the current pitch, yaw and roll data of the Oculus Rift.

    :return: Current Pitch, yaw and roll data of the Oculus Rift
    """
    ts = ovr.getTrackingState(session, ovr.getTimeInSeconds(), True)
    if ts.StatusFlags & (ovr.Status_OrientationTracked | ovr.Status_PositionTracked):
        pose = ts.HeadPose.ThePose
        # axisY=1,axisX=0, axisZ=2
        yaw_rad, pitch_rad, roll_rad = pose.Orientation.getEulerAngles(axis1=1, axis2=0, axis3=2,
                                                                       rotate_direction=1, handedness=1)
        # positive rotation is counter-clockwise
        pitch = float(np.rad2deg(pitch_rad))  # Pitch = rotation around X axis
        yaw = float(np.rad2deg(yaw_rad))  # Yaw = rotation around Y axis
        roll = float(np.rad2deg(roll_rad))  # Roll = rotation around Z axis
        yaw_orig = yaw
        yaw = yaw_orig
        if yaw >= 180:
            yaw = -360 + yaw_orig
    return (pitch, yaw, roll)
