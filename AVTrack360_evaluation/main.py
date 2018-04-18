"""
Main class for evaluating the datasets recorded by AVTrack360.

@author: Stephan Fremerey
"""

from argparse import ArgumentParser
import evaluation_tools
import json
import os

def main():
    parser = ArgumentParser(description="This tool helps in evaluating a merged AVTrack360 dataset. "
                                        "Be aware that a few parameters can not be set via the given parameters. "
                                        "You need to set them at the beginning of this script. "
                                        "Be also aware that for plotting a different number of videos than 20, you "
                                        "might need to adapt the respective evaluation_tools.py functions.")
    parser.add_argument("-all", dest="all", default=False, action="store_true",
                        help="Add this parameter if you want to plot every possible figure.")
    parser.add_argument("-overtimevelocity", dest="overtimevelocity", default=False, action="store_true",
                        help="Add this parameter, if you want to plot a color coded plot showing the"
                             " velocity over time for each subject and video.")
    parser.add_argument("-stackedbarcharts", dest="stackedbarcharts", default=False, action='store_true',
                        help="Add this parameter, if you want to plot stacked bar charts showing the percentage of"
                             " people covered the video within given ranges.")
    parser.add_argument("-heatmaps", dest="heatmaps", default=False, action='store_true',
                        help="Add this parameter, if you want to plot heatmaps showing the probability"
                             " of pitch and yaw values per video (per time watched).")
    parser.add_argument("-invertpy", dest="invertpy", default=False, action='store_true',
                        help="Enable for following definition of pitch and yaw values (old): Pitching head up -->"
                             " positive pitch; Turning head left --> positive yaw values. Disable for vice versa.")
    parser.add_argument("-standby", dest="standby", default=False, action='store_true',
                        help="Add this parameter if you want to send your computer to standby after all calculations.")
    parser.add_argument("-shutdown", dest="shutdown", default=False, action='store_true',
                        help="Add this parameter if you want to shutdown the computer after all calculations.")
    arg = parser.parse_args()


    # ----- Some data that are needed quite everywhere ----- #
    with open('data_modified\\merged_data.json', mode='r') as merged_data_file:
        merged_data = json.load(merged_data_file)
    image_formats = ["pdf", "png"]
    hmds = ["vive"]
    quality_levels = 1
    sort_by_playlist = False
    video_list = []
    for video in range(1, 21):
        video_list.append("%s.mp4" % (video))
    quantities_sequence_watched = [1]  # If the sequence was watched multiple times, specify the quantity here
    # Hence for a 10 second long video you would need ~2000 samples
    sample_number = 300

    if arg.stackedbarcharts or arg.all:
        for hmd in hmds:
            for image_format in image_formats:
                evaluation_tools.plotStackedBarcharts(merged_data, hmd, video_list, sample_number,
                                                                len(quantities_sequence_watched),
                                                              quality_levels, sort_by_playlist, image_format)

    if arg.heatmaps or arg.all:
        for hmd in hmds:
            for image_format in image_formats:
                evaluation_tools.plotHeatmaps(merged_data, hmd, video_list, sample_number,
                                                                len(quantities_sequence_watched),
                                                      quality_levels, arg.invertpy, image_format)

    if arg.overtimevelocity or arg.all:
        for image_format in image_formats:
            for hmd in hmds:
                evaluation_tools.plotOverTimeVelocity(merged_data, hmd, video_list, sample_number,
                                                                len(quantities_sequence_watched),
                                                              quality_levels, image_format)

    # ----- Standby & Shutdown scripts ----- #
    if arg.standby:
        print("Done. Sending the PC to Standby mode...")
        os.system("C:\\Windows\\System32\\rundll32.exe powrprof.dll,SetSuspendState Sleep")

    if arg.shutdown:
        print("Done. Shutting <down the PC...")
        os.system("C:\\Windows\\System32\\shutdown.exe /f /s /t 0")

if __name__ == "__main__":
    main()
