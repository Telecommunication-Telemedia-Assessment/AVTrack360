"""
This script contains some helper functions.

@author: Stephan Fremerey
"""

from datetime import datetime

import json
import os.path
import pyautogui
import psutil
import subprocess
import time
import win32gui

def autoplay_sleep(overall_sleep_duration):
    """
    This function is desired for the autoplay function of the framework when using Whirligig player.
    It presses the R key every 100ms to assure that the person will not see any
    other parts of the video before the video starts.
    :return:
    """
    sleep_duration = 0
    while sleep_duration < overall_sleep_duration:
        pyautogui.press("R")
        time.sleep(float(0.1))
        sleep_duration += 0.1

def capture_viewport(video_length_in_s, filename):
    """
    This function is desired for using ffmpeg to capture the video output of a specific window. Currently, the
    "Whirligig" window is used.
    :param video_length_in_s: The length of the played back video in s.
    :param filename: The filename of the played back video.
    """
    captureviewport_ff_base_cmd = ["tools\\ffmpeg-4.0-win64-static\\ffmpeg.exe -f gdigrab",
                                   "-framerate 30",
                                   "-t {video_length_in_s}",
                                   "-i title=Whirligig",
                                   "-y",
                                   "data\\viewport_captures\\{filename}.mkv"]
    captureviewport_ff_cmd = " ".join(captureviewport_ff_base_cmd).format(video_length_in_s=video_length_in_s,
                                                                          filename=filename)
    DETACHED_PROCESS = 0x00000008
    subprocess.Popen(captureviewport_ff_cmd, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True,
                     creationflags=DETACHED_PROCESS)

def get_acr_by_cmd_input():
    """
    Gets the ACR score from the user by simple command line type-in.
    :return: The ACR score of the user.
    """
    accepted_inputs = ["1", "2", "3", "4", "5"]
    acr = "0"
    while acr not in accepted_inputs:
        print("You have entered a wrong input. Please enter the ACR score again (1-5)!")
        acr = raw_input("Please type in the subject's ACR score (1-5): ")
    return acr

def get_length_of_video(filename):
    """
    Return the the length of a video using ffprobe.
    See http://stackoverflow.com/questions/31024968/using-ffmpeg-to-obtain-video-durations-in-python

    :param filename: The filename.
    :return: The length of a given video in seconds.
    """
    video = subprocess.Popen('tools\\ffmpeg-3.3.3-win64-static\\bin\\ffprobe.exe -i videos\\' + filename +
                             ' -show_entries format=duration -v quiet -of csv="p=0"',
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    video_length_in_s = video.communicate()
    return float(video_length_in_s[0])

def get_current_time():
    """
    Function to get the current time in a format which could be used in filenames under Windows.

    :return: A string containing the current time in the format yyyy-mm-dd hh-mmm-ss.
    """
    return str(datetime.now()).replace(":", "-")[:-7]  # Omit last 7 characters as we ned no milliseconds here


def is_process_running(process_name):
    n = 0  # number of instances of the program running
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
        except:
            return False
        if p.name() == process_name:
            n += 1
    if n > 0:
        return True
    else:
        return False

def kill_windows_process(process_name):
    """
    Function to kill a Windows process.

    :param process_name: Full name of the process to kill.
    """
    os.system('TASKKILL /F /IM ' + process_name + ' /T')

def set_window_focus(window_name, class_name):
    """
    Function to set the focus of Windows to one window by pressing Alt+Esc as long as the window is found.
    :param window_name: Name of the window.
    :param class_name: Class name of the window.
    """
    actual_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    actual_class_name = win32gui.GetClassName(win32gui.GetForegroundWindow())
    while actual_window != window_name and actual_class_name != class_name:
        pyautogui.hotkey('alt', 'esc')
        time.sleep(float(1))
        actual_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        actual_class_name = win32gui.GetClassName(win32gui.GetForegroundWindow())

def shift_yaw(yaw_orig, initial_yaw):
    """
    Function to shift the input yaw value to a defined value.

    :param yaw_orig: The original yaw value.
    :param initial_yaw: The initial yaw value recorded, hence the value to shift for * -1.
    :return yaw: The shifted yaw value.
    """
    initial_yaw_abs = abs(initial_yaw)
    yaw = yaw_orig + initial_yaw * -1
    if yaw >= 180:
        yaw = -360 + yaw_orig + initial_yaw_abs
    elif yaw <= -180:
        yaw = 360 + yaw_orig - initial_yaw_abs
    return yaw

def write_to_json(label, data, overwrite_enabled):
    """
    Function to write data to a JSON file. If the file is already existing, append the new data.

    :param label: Label of the JSON file (equals the filename).
    :param data: JSON data to write.
    :param overwrite_enabled: True, if already existing filename/HMD combinations should be deleted, False otherwise.
    """
    # If JSON file is already existing, open it first, then get existing data of it.
    if os.path.isfile('data\\' + label + '.json'):
        with open('data\\' + label + '.json', mode='r') as existing_file:
            existing_json = json.load(existing_file)
            updated_json = {'label': label, 'data': []};
            if overwrite_enabled:
                # Loop over existing data. Only add the new recorded data to the new dataset.
                for i in range(0, len(existing_json['data'])):
                    if existing_json['data'][i]['filename'] == data['filename'] and \
                                    existing_json['data'][i]['hmd'] == data['hmd']:
                        pass
                    else:
                        updated_json['data'].append(existing_json['data'][i])
            else:
                updated_json = existing_json
            # Append the new data and write the updated JSON data to the JSON file.
            updated_json['data'].append(data)
            with open('data\\' + label + '.json', mode='w') as updated_file:
                json.dump(updated_json, updated_file, indent=4,
                          sort_keys=True, separators=(',', ':'))
    # If JSON file is not already existing, create it and write the data to it.
    else:
        with open('data\\' + label + '.json', mode='w') as new_file:
            json.dump({'label': label, 'data': [data]}, new_file, indent=4,
                      sort_keys=True, separators=(',', ':'))
