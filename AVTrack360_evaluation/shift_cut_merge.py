"""
Contains functionality to shift the yaw values of the datasets recorded by AVTrack360
and merge them together within one file.

This also contains the functionality to cut off not relevant parts of the recorded data.

@author: Stephan Fremerey
"""

from argparse import ArgumentParser
import json
import os


parser = ArgumentParser(description="This tool helps in shifting the yaw values of the datasets recorded by"
                                    "AVTrack360 and merge them together into one file.")
parser.add_argument("-subjects", dest="subjects", help="The number of datasets to process.",
                     type=int, default=49)
parser.add_argument("-cut", dest="cut", help="Add this parameter to only consider the timestamps recorded only for the "
                                             "length of the respective viceo. Hence e.g. if the video "
                                             "lasts 30s with a subsequent greyscreen of 10s, only the data obtained "
                                             "due to the JSON files placed in data/SRC_info folder (get via respective"
                                             " FFmpeg command) would be taken.", default=False, action='store_true')


arg = parser.parse_args()
no_videos_watched = 20
outliers = []  # Array containing the outlier subjects

# Get the data files of all subjects for this test and cut it according to SRC information
for i in range(1, arg.subjects + 1):
    # Exclude subject 1 as it contains too less data
    if i in outliers:
        print("Skipping subject %s as it is an outlier..." % (i))
        continue
    else:
        try:
            with open('data\\%s.json' % (i), mode='r') as data_file:
                data = json.load(data_file)
            if arg.cut:
                # Loop over different videos
                for j in range(len(data["data"])):
                    # Get the exact duration of the video itself (grayscreen NOT included!!!)
                    video_id = data["data"][j]["filename"].split(".")[0]
                    with open('data\\SRC_info\\%s.json' % (video_id), mode='r') as data_file:
                        video_data = json.load(data_file)
                    video_length = float(video_data["streams"][0]["duration"])
                    # Detect timestamp to start cutting from
                    for x in range(len(data["data"][j]["pitch_yaw_roll_data_hmd"])):
                        if data["data"][j]["pitch_yaw_roll_data_hmd"][x]["sec"] > video_length:
                            start_cut = x
                            break
                    # Delete as many timestamps as are following after the timestamp to start cutting
                    k = 0
                    times_to_cut = len(data["data"][j]["pitch_yaw_roll_data_hmd"]) - start_cut
                    while k != times_to_cut:
                        del data["data"][j]["pitch_yaw_roll_data_hmd"][start_cut]
                        k += 1
                    # Set the video length to the length of the video itself
                    data["data"][j]["video_length_in_s"] = video_length
        # If a dataset is not available, catch the error
        except IOError:
            print("The dataset no. %s is not available." % (i))
    # Save the modified datasets
    with open('data_modified\\%s.json' % (i), mode='w') as new_file:
        json.dump(data, new_file, indent=4, sort_keys=True, separators=(',', ':'))


merged_data = {'merged_data': []}
# Get the data files of all subjects for this test
for i in range(1, arg.subjects + 1):
    if i == 0:
        print("Skipping merging subject %s as it contains too less data..." % (i))
        continue
    else:
        print("Merging subject %s..." % (i))
        try:
            with open('data_modified\\%s.json' % (i), mode='r') as data_file:
                data = json.load(data_file)
            merged_data['merged_data'].append(data)
        # If a dataset is not available, catch the error
        except IOError:
            print("The dataset no. %s is not available." % (i))

with open('data_modified\\merged_data.json', mode='w') as new_file:
    json.dump(merged_data, new_file, indent=4,
              sort_keys=True, separators=(',', ':'))

print("Done.")