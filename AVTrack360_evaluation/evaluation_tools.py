import helpers
import matplotlib.pyplot as plt
import matplotlib
import multiprocessing
import numpy as np
import os
matplotlib.style.use('classic')

color_list = ["red", "green", "blue", "orange", "fuchsia", "cyan", "goldenrod", "saddlebrown",
              "lime", "dimgray", "dodgerblue", "c"]

def plotStackedBarcharts(merged_data, hmd, sequences, sample_number, times_watched, quality_levels, sort_by_playlist,
                         image_format):
    """
    Plot stacked bar charts showing the distribution of several pitch/yaw bins for all sequences.

    This plots are created:
    a) considering distance between Min/Max pitch and yaw values
    b) considering every recorded pitch and yaw value.

    :param merged_data: The merged AVTrack360 dataset.
    :param hmd: The HMD to use.
    :param sequences: The sequences to process.
    :param sample_number: The number of samples (AVTrack360 records roughly 200 values per second).
    :param times_watched: The number of times watching the content.
    :param quality_levels: Specify the number of quality levels to summarize the data of all quality levels
    and multiple times watched for each video.
    :param sort_by_playlist: Activate if the "times watched" definition should not be based on 1st and 2nd time watched
    per quality level, but be based on watching the video itself for the really 1st, 2nd [...] time.
    :param image_format: The format to write the image (pdf, png etc.).
    """
    plt.ion()  # Needed in order to close figures and write them automatically

    # Initialization of variables
    subjects = len(merged_data['merged_data'])
    no_videos = len(sequences)

    ## ((times_watched_sequence, number_of_sequences, pitch_yaw_roll_time, sample_number, subjects))
    subjects_pyrt_data_angle = helpers.getPyrtDataInArray(merged_data, hmd, sequences, sample_number,
                                                          sort_by_playlist, quality_levels, times_watched)
    if sort_by_playlist:
        times_watched = times_watched * quality_levels
        no_videos = int(no_videos / quality_levels)
        quality_levels = 1
        sequences = []
        for s in range(1, no_videos + 1):
            sequences.append("%s.mp4" % (s))

    # Arrays containing the maximum and minimum pitch and yaw value per subject and video (seen over all values)
    subjects_minpy_data = np.zeros((times_watched, no_videos, 2, subjects), dtype=np.float64)
    subjects_maxpy_data = np.zeros((times_watched, no_videos, 2, subjects), dtype=np.float64)
    # Find out the maximum pitch and yaw values per subject
    for i in range(0, subjects):
        for sequence in sequences:
                seqindex = sequences.index(sequence)
                for j in range(0, times_watched):
                    subjects_minpy_data[j, seqindex, 0, i] =\
                        min(subjects_pyrt_data_angle[j, seqindex, 0, :, i])
                    subjects_maxpy_data[j, seqindex, 0, i] =\
                        max(subjects_pyrt_data_angle[j, seqindex, 0, :, i])
                    subjects_minpy_data[j, seqindex, 1, i] =\
                        min(subjects_pyrt_data_angle[j, seqindex, 1, :, i])
                    subjects_maxpy_data[j, seqindex, 1, i] =\
                        max(subjects_pyrt_data_angle[j, seqindex, 1, :, i])

    # Specifying ranges (legend: ed = euclidean distance, r = range no., p = pitch, y = yaw)
    # for euclidean distance min/max stacked bar chart plots
    edr1_y = 0
    edr2_y = 30
    edr3_y = 60
    edr4_y = 90
    edr5_y = 120
    edr6_y = 150
    edr7_y = 180
    edr8_y = 210
    edr9_y = 240
    edr10_y = 270
    edr11_y = 300
    edr12_y = 330
    edr13_y = 360

    edr1_p = 0
    edr2_p = 20
    edr3_p = 40
    edr4_p = 60
    edr5_p = 80
    edr6_p = 100
    edr7_p = 120
    edr8_p = 140
    edr9_p = 160
    edr10_p = 180

    # Obtaining data for min/max pitch/yaw data
    edminmax_pitch_no_bins = 9
    edminmax_yaw_no_bins = 12
    subjects_noncumulative_range_edminmax_pitch = np.zeros((times_watched, no_videos, edminmax_pitch_no_bins), dtype=np.float64)
    subjects_noncumulative_range_edminmax_yaw = np.zeros((times_watched, no_videos, edminmax_yaw_no_bins), dtype=np.float64)

    # Loop for pitch
    for i in range(0, subjects):
        for sequence in sequences:
            seqindex = sequences.index(sequence)
            for j in range(0, times_watched):
                # At first go over the min/max pitch values
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr1_p, edr2_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 0] += 1
                    continue  # Continue necessary here as we want a non cumulative plot
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr2_p, edr3_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 1] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr3_p, edr4_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 2] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr4_p, edr5_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 3] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr5_p, edr6_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 4] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr6_p, edr7_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 5] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr7_p, edr8_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 6] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr8_p, edr9_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 7] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 0, i] - subjects_maxpy_data[j, seqindex, 0, i]) \
                        in range(edr9_p, edr10_p):
                    subjects_noncumulative_range_edminmax_pitch[j, seqindex, 8] += 1
                    continue

    # Loop for yaw
    for i in range(0, subjects):
        for sequence in sequences:
            seqindex = sequences.index(sequence)
            for j in range(0, times_watched):
                # At first go over the min/max pitch values
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr1_y, edr2_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 0] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr2_y, edr3_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 1] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr3_y, edr4_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 2] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr4_y, edr5_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 3] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr5_y, edr6_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 4] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr6_y, edr7_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 5] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr7_y, edr8_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 6] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr8_y, edr9_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 7] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr9_y, edr10_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 8] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr10_y, edr11_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 9] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr11_y, edr12_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 10] += 1
                    continue
                if np.linalg.norm(subjects_minpy_data[j, seqindex, 1, i] - subjects_maxpy_data[j, seqindex, 1, i]) \
                        in range(edr12_y, edr13_y):
                    subjects_noncumulative_range_edminmax_yaw[j, seqindex, 11] += 1
                    continue

    # Specifying ranges (legend: nr/pr = negative/positive range no., p = pitch, y = yaw) for allpy stacked bar chart plots
    nr1_p = -90
    nr2_p = -60
    nr3_p = -30
    pr1_p = 0
    pr2_p = 30
    pr3_p = 60
    pr4_p = 90

    nr1_y = -180
    nr2_y = -150
    nr3_y = -120
    nr4_y = -90
    nr5_y = -60
    nr6_y = -30
    pr1_y = 0
    pr2_y = 30
    pr3_y = 60
    pr4_y = 90
    pr5_y = 120
    pr6_y = 150
    pr7_y = 180

    # Obtaining data for all pitch/yaw data
    allpy_pitch_no_bins = 6
    allpy_yaw_no_bins = 12
    subjects_noncumulative_range_allpy_pitch = np.zeros((times_watched, no_videos, allpy_pitch_no_bins), dtype=np.float64)
    subjects_noncumulative_range_allpy_yaw = np.zeros((times_watched, no_videos, allpy_yaw_no_bins), dtype=np.float64)

    # Two single loops for pitch and yaw needed because of continue command
    # Loop for pitch
    for i in range(0, subjects):
        for sequence in sequences:
            seqindex = sequences.index(sequence)
            for j in range(0, times_watched):
                for x in range(sample_number):
                    try:
                        # At first go over all pitch values
                        if subjects_pyrt_data_angle[j, seqindex, 0, x, i] in range(nr1_p, nr2_p + 1):
                            subjects_noncumulative_range_allpy_pitch[j, seqindex, 0] += 1
                            continue  # Continue necessary here as we want a non cumulative plot
                        if subjects_pyrt_data_angle[j, seqindex, 0, x, i] in range(nr2_p, nr3_p + 1):
                            subjects_noncumulative_range_allpy_pitch[j, seqindex, 1] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 0, x, i] in range(nr3_p, pr1_p + 1):
                            subjects_noncumulative_range_allpy_pitch[j, seqindex, 2] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 0, x, i] in range(pr1_p, pr2_p + 1):
                            subjects_noncumulative_range_allpy_pitch[j, seqindex, 3] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 0, x, i] in range(pr2_p, pr3_p + 1):
                            subjects_noncumulative_range_allpy_pitch[j, seqindex, 4] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 0, x, i] in range(pr3_p, pr4_p + 1):
                            subjects_noncumulative_range_allpy_pitch[j, seqindex, 5] += 1
                            continue
                    except IndexError:
                        None

    # Loop for yaw
    for i in range(0, subjects):
        for sequence in sequences:
            seqindex = sequences.index(sequence)
            for j in range(0, times_watched):
                for x in range(sample_number):
                    try:
                        # Then go over the min/max yaw values
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(nr1_y, nr2_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 0] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(nr2_y, nr3_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 1] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(nr3_y, nr4_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 2] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(nr4_y, nr5_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 3] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(nr5_y, nr6_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 4] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(nr6_y, pr1_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 5] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(pr1_y, pr2_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 6] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(pr2_y, pr3_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 7] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(pr3_y, pr4_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 8] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(pr4_y, pr5_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 9] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(pr5_y, pr6_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 10] += 1
                            continue
                        if subjects_pyrt_data_angle[j, seqindex, 1, x, i] in range(pr6_y, pr7_y + 1):
                            subjects_noncumulative_range_allpy_yaw[j, seqindex, 11] += 1
                            continue
                    except IndexError:
                        None

    width = 0.6
    if quality_levels != 1:
        different_videos = int(len(sequences) / quality_levels)
        plt.close("all")  # Close all figures before so we get no memory RuntimeWarning
        xtick_labels = []
        for xl in range(0, different_videos):
            xtick_labels.append("%s" % (xl + 1))
        # Create version of stacked bar charts showing the amount of time the subjects watched the sequences
        # within the respective pitch/yaw ranges based on all pitch/yaw values
        # Pitch plots
        allpypy_pitch_perc = np.zeros((allpy_pitch_no_bins, different_videos), dtype=np.float64)
        for j in range(0, different_videos):
            ind = np.arange(different_videos)
            labels = "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr1_p, nr2_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr2_p, nr3_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr3_p, pr1_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr1_p, pr2_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr2_p, pr3_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr3_p, pr4_p)
            for k in range(0, times_watched):
                for l in range(0, allpy_pitch_no_bins):
                    for q in range(0, quality_levels):
                        seqindex = j * quality_levels + q
                        allpypy_pitch_perc[l, j] += subjects_noncumulative_range_allpy_pitch[k, seqindex, l]
        # Divide by the number of data points in all bins
        allpypy_pitch_perc[:, :] = (allpypy_pitch_perc[:, :] / sum(allpypy_pitch_perc[:, :])) * 100
        fig = plt.figure(figsize=(12, 9))
        p1 = plt.bar(ind, allpypy_pitch_perc[0, :], width, color=color_list[0])
        p2 = plt.bar(ind, allpypy_pitch_perc[1, :], width, bottom=allpypy_pitch_perc[0, :], color=color_list[1])
        p3 = plt.bar(ind, allpypy_pitch_perc[2, :], width,
                     bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :],
                     color=color_list[2])
        p4 = plt.bar(ind, allpypy_pitch_perc[3, :], width,
                     bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :] + allpypy_pitch_perc[2, :],
                     color=color_list[3])
        p5 = plt.bar(ind, allpypy_pitch_perc[4, :], width,
                     bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :] + allpypy_pitch_perc[2, :]
                            + allpypy_pitch_perc[3, :],
                     color=color_list[4])
        p6 = plt.bar(ind, allpypy_pitch_perc[5, :], width,
                     bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :] + allpypy_pitch_perc[2, :]
                            + allpypy_pitch_perc[3, :] + allpypy_pitch_perc[4, :],
                     color=color_list[5])

        plt.ylabel('Percentage of Time', fontsize=15)
        plt.xlabel('Sequence no.', fontsize=15)
        # plt.title('Percentage of Time watched per Sequence within given Pitch ranges', y=1.09,
        #           fontsize=16)
        plt.xticks(ind, xtick_labels, fontsize=15)
        plt.ylim(ymax=105, ymin=0)
        plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), labels, bbox_to_anchor=(0., 1.02, 1., .102),
                   loc=3, ncol=3, mode="expand", borderaxespad=0., fontsize=15)
        plt.show()
        fig.savefig("results\\plots\\barcharts\\barchart_all_pitch_summarized.%s" % (image_format), bbox_inches='tight',
                    dpi=300)

        # Yaw plots
        allpypy_yaw_perc = np.zeros((allpy_yaw_no_bins, different_videos), dtype=np.float64)
        for j in range(0, different_videos):
            ind = np.arange(different_videos)
            labels = "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr1_y, nr2_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr2_y, nr3_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr3_y, nr4_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr4_y, nr5_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr5_y, nr6_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr6_y, pr1_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr1_y, pr2_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr2_y, pr3_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr3_y, pr4_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr4_y, pr5_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr5_y, pr6_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr6_y, pr7_y)
            for k in range(0, times_watched):
                for l in range(0, allpy_yaw_no_bins):
                    for q in range(0, quality_levels):
                        seqindex = j * quality_levels + q
                        allpypy_yaw_perc[l, j] += subjects_noncumulative_range_allpy_yaw[k, seqindex, l]
        # Divide by the number of data points in all bins
        allpypy_yaw_perc[:, :] = (allpypy_yaw_perc[:, :] / sum(allpypy_yaw_perc[:, :])) * 100
        fig = plt.figure(figsize=(12, 9))
        p1 = plt.bar(ind, allpypy_yaw_perc[0, :], width, color=color_list[0])
        p2 = plt.bar(ind, allpypy_yaw_perc[1, :], width, bottom=allpypy_yaw_perc[0, :], color=color_list[1])
        p3 = plt.bar(ind, allpypy_yaw_perc[2, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :],
                     color=color_list[2])
        p4 = plt.bar(ind, allpypy_yaw_perc[3, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :],
                     color=color_list[3])
        p5 = plt.bar(ind, allpypy_yaw_perc[4, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                            + allpypy_yaw_perc[3, :],
                     color=color_list[4])
        p6 = plt.bar(ind, allpypy_yaw_perc[5, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                            + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :],
                     color=color_list[5])
        p7 = plt.bar(ind, allpypy_yaw_perc[6, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                            + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :],
                     color=color_list[6])
        p8 = plt.bar(ind, allpypy_yaw_perc[7, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                            + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                            + allpypy_yaw_perc[6, :],
                     color=color_list[7])
        p9 = plt.bar(ind, allpypy_yaw_perc[8, :], width,
                     bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                            + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                            + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :],
                     color=color_list[8])
        p10 = plt.bar(ind, allpypy_yaw_perc[9, :], width,
                      bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                             + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                             + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :] + allpypy_yaw_perc[8, :],
                      color=color_list[9])
        p11 = plt.bar(ind, allpypy_yaw_perc[10, :], width,
                      bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                             + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                             + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :] + allpypy_yaw_perc[8, :]
                             + allpypy_yaw_perc[9, :],
                      color=color_list[10])
        p12 = plt.bar(ind, allpypy_yaw_perc[11, :], width,
                      bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                             + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                             + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :] + allpypy_yaw_perc[8, :]
                             + allpypy_yaw_perc[9, :] + allpypy_yaw_perc[10, :],
                      color=color_list[11])
        plt.ylabel('Percentage of Time', fontsize=15)
        plt.xlabel('Sequence no.', fontsize=15)
        # plt.title('Percentage of Time watched per Sequence within given Yaw ranges', y=1.12,
        #           fontsize=16)
        plt.xticks(ind, xtick_labels, fontsize=15)
        plt.ylim(ymax=105, ymin=0)
        plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0],
                    p8[0], p9[0], p10[0], p11[0], p12[0]), labels, bbox_to_anchor=(0., 1.02, 1., .102),
                   loc=3, ncol=4, mode="expand", borderaxespad=0., fontsize=15)
        plt.show()
        fig.savefig("results\\plots\\barcharts\\barchart_all_yaw_summarized.%s" % (image_format), bbox_inches='tight',
                    dpi=300)

    else:
        # Create version of stacked bar charts showing the percentage of subjects
        # discovered the euclidean distance between min/max values in respective ranges
        for j in range(0, times_watched):
            plt.close("all")  # Close all figures before so we get no memory RuntimeWarning
            # Pitch plots
            ind = np.arange(no_videos)
            labels = "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr1_p, edr2_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr2_p, edr3_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr3_p, edr4_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr4_p, edr5_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr5_p, edr6_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr6_p, edr7_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr7_p, edr8_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr8_p, edr9_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr9_p, edr10_p)
            edminmax_pitch_perc = np.zeros((edminmax_pitch_no_bins, no_videos), dtype=np.float64)
            for k in range(0, edminmax_pitch_no_bins):
                for sequence in sequences:
                    seqindex = sequences.index(sequence)
                    # Divide by the number of data point in all bins
                    edminmax_pitch_perc[k, seqindex] = \
                        (subjects_noncumulative_range_edminmax_pitch[j, seqindex, k] / subjects) * 100
            fig = plt.figure(figsize=(12, 9))
            p1 = plt.bar(ind, edminmax_pitch_perc[0, :], width, color=color_list[0])
            p2 = plt.bar(ind, edminmax_pitch_perc[1, :], width, bottom=edminmax_pitch_perc[0, :], color=color_list[1])
            p3 = plt.bar(ind, edminmax_pitch_perc[2, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :],
                         color=color_list[2])
            p4 = plt.bar(ind, edminmax_pitch_perc[3, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :] + edminmax_pitch_perc[2, :],
                         color=color_list[3])
            p5 = plt.bar(ind, edminmax_pitch_perc[4, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :] + edminmax_pitch_perc[2, :]
                                + edminmax_pitch_perc[3, :],
                         color=color_list[4])
            p6 = plt.bar(ind, edminmax_pitch_perc[5, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :] + edminmax_pitch_perc[2, :]
                                + edminmax_pitch_perc[3, :] + edminmax_pitch_perc[4, :],
                         color=color_list[5])
            p7 = plt.bar(ind, edminmax_pitch_perc[6, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :] + edminmax_pitch_perc[2, :]
                                + edminmax_pitch_perc[3, :] + edminmax_pitch_perc[4, :] + edminmax_pitch_perc[5, :],
                         color=color_list[6])
            p8 = plt.bar(ind, edminmax_pitch_perc[7, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :] + edminmax_pitch_perc[2, :]
                                + edminmax_pitch_perc[3, :] + edminmax_pitch_perc[4, :] + edminmax_pitch_perc[5, :]
                                + edminmax_pitch_perc[6, :],
                         color=color_list[7])
            p9 = plt.bar(ind, edminmax_pitch_perc[8, :], width,
                         bottom=edminmax_pitch_perc[0, :] + edminmax_pitch_perc[1, :] + edminmax_pitch_perc[2, :]
                                + edminmax_pitch_perc[3, :] + edminmax_pitch_perc[4, :] + edminmax_pitch_perc[5, :]
                                + edminmax_pitch_perc[6, :] + edminmax_pitch_perc[7, :],
                         color=color_list[8])

            plt.ylabel('Percentage of Subjects', fontsize=15)
            plt.xlabel('Sequence no.', fontsize=15)
            # plt.title('Percentage of Subjects watched given Pitch Norm(Min-Max) for Sequence (#%s time)' % (j + 1), y=1.12,
            #           fontsize=16)
            plt.xticks(ind, [s.replace('.mp4', '') for s in sequences], fontsize=15)
            plt.ylim(ymax=105, ymin=0)
            plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0]),
                       labels, bbox_to_anchor=(0., 1.02, 1., .102),
                       loc=3, ncol=3, mode="expand", borderaxespad=0., fontsize=15)
            plt.show()
            fig.savefig("results\\plots\\barcharts\\barchart_edminmax_time%s_pitch.%s" % (j + 1, image_format),
                        bbox_inches='tight', dpi=300)

            # Yaw plots
            ind = np.arange(no_videos)
            labels = "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr1_y, edr2_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr2_y, edr3_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr3_y, edr4_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr4_y, edr5_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr5_y, edr6_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr6_y, edr7_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr7_y, edr8_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr8_y, edr9_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr9_y, edr10_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr10_y, edr11_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr11_y, edr12_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (edr12_y, edr13_y)
            edminmax_yaw_perc = np.zeros((edminmax_yaw_no_bins, no_videos), dtype=np.float64)
            for k in range(0, edminmax_yaw_no_bins):
                for sequence in sequences:
                    seqindex = sequences.index(sequence)
                    # Divide by the number of data point in all bins
                    edminmax_yaw_perc[k, seqindex] = \
                        (subjects_noncumulative_range_edminmax_yaw[j, seqindex, k] / subjects) * 100
            fig = plt.figure(figsize=(12, 9))
            p1 = plt.bar(ind, edminmax_yaw_perc[0, :], width, color=color_list[0])
            p2 = plt.bar(ind, edminmax_yaw_perc[1, :], width, bottom=edminmax_yaw_perc[0, :], color=color_list[1])
            p3 = plt.bar(ind, edminmax_yaw_perc[2, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :],
                         color=color_list[2])
            p4 = plt.bar(ind, edminmax_yaw_perc[3, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :],
                         color=color_list[3])
            p5 = plt.bar(ind, edminmax_yaw_perc[4, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :],
                         color=color_list[4])
            p6 = plt.bar(ind, edminmax_yaw_perc[5, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :],
                         color=color_list[5])
            p7 = plt.bar(ind, edminmax_yaw_perc[6, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :] + edminmax_yaw_perc[5, :],
                         color=color_list[6])
            p8 = plt.bar(ind, edminmax_yaw_perc[7, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :] + edminmax_yaw_perc[5, :]
                                + edminmax_yaw_perc[6, :],
                         color=color_list[7])
            p9 = plt.bar(ind, edminmax_yaw_perc[8, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :] + edminmax_yaw_perc[5, :]
                                + edminmax_yaw_perc[6, :] + edminmax_yaw_perc[7, :],
                         color=color_list[8])
            p10 = plt.bar(ind, edminmax_yaw_perc[9, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :] + edminmax_yaw_perc[5, :]
                                + edminmax_yaw_perc[6, :] + edminmax_yaw_perc[7, :] + edminmax_yaw_perc[8, :],
                         color=color_list[9])
            p11 = plt.bar(ind, edminmax_yaw_perc[10, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :] + edminmax_yaw_perc[5, :]
                                + edminmax_yaw_perc[6, :] + edminmax_yaw_perc[7, :] + edminmax_yaw_perc[8, :]
                                + edminmax_yaw_perc[9, :],
                         color=color_list[10])
            p12 = plt.bar(ind, edminmax_yaw_perc[11, :], width,
                         bottom=edminmax_yaw_perc[0, :] + edminmax_yaw_perc[1, :] + edminmax_yaw_perc[2, :]
                                + edminmax_yaw_perc[3, :] + edminmax_yaw_perc[4, :] + edminmax_yaw_perc[5, :]
                                + edminmax_yaw_perc[6, :] + edminmax_yaw_perc[7, :] + edminmax_yaw_perc[8, :]
                                + edminmax_yaw_perc[9, :] + edminmax_yaw_perc[10, :],
                         color=color_list[11])
            plt.ylabel('Percentage of Subjects', fontsize=15)
            plt.xlabel('Sequence no.', fontsize=15)
            # plt.title('Percentage of Subjects watched given Yaw Norm(Min-Max) for Sequence (#%s time)' % (j + 1), y=1.16,
            #           fontsize=16)
            plt.xticks(ind, [s.replace('.mp4', '') for s in sequences], fontsize=15)
            plt.ylim(ymax=105, ymin=0)
            plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0],
                        p8[0], p9[0], p10[0], p11[0], p12[0]), labels, bbox_to_anchor=(0., 1.02, 1., .102),
                       loc=3, ncol=4, mode="expand", borderaxespad=0., fontsize=15)
            plt.show()
            fig.savefig("results\\plots\\barcharts\\barchart_edminmax_time%s_yaw.%s" % (j + 1, image_format),
                        bbox_inches='tight', dpi=300)

        # Create version of stacked bar charts showing the amount of time the subjects watched the sequences
        # within the respective pitch/yaw ranges based on all pitch/yaw values
        for j in range(0, times_watched):
            plt.close("all")  # Close all figures before so we get no memory RuntimeWarning
            # Pitch plots
            ind = np.arange(no_videos)
            labels = "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr1_p, nr2_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr2_p, nr3_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr3_p, pr1_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr1_p, pr2_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr2_p, pr3_p),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr3_p, pr4_p)
            allpypy_pitch_perc = np.zeros((allpy_pitch_no_bins, no_videos), dtype=np.float64)
            for k in range(0, allpy_pitch_no_bins):
                for sequence in sequences:
                    seqindex = sequences.index(sequence)
                    overall_data_points = sum(subjects_noncumulative_range_allpy_pitch[j, seqindex, :])
                    # Divide by the number of data point in all bins
                    allpypy_pitch_perc[k, seqindex] = \
                        (subjects_noncumulative_range_allpy_pitch[j, seqindex, k] / overall_data_points) * 100
            fig = plt.figure(figsize=(12, 9))
            p1 = plt.bar(ind, allpypy_pitch_perc[0, :], width, color=color_list[0])
            p2 = plt.bar(ind, allpypy_pitch_perc[1, :], width, bottom=allpypy_pitch_perc[0, :], color=color_list[1])
            p3 = plt.bar(ind, allpypy_pitch_perc[2, :], width,
                         bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :],
                         color=color_list[2])
            p4 = plt.bar(ind, allpypy_pitch_perc[3, :], width,
                         bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :] + allpypy_pitch_perc[2, :],
                         color=color_list[3])
            p5 = plt.bar(ind, allpypy_pitch_perc[4, :], width,
                         bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :] + allpypy_pitch_perc[2, :]
                                + allpypy_pitch_perc[3, :],
                         color=color_list[4])
            p6 = plt.bar(ind, allpypy_pitch_perc[5, :], width,
                         bottom=allpypy_pitch_perc[0, :] + allpypy_pitch_perc[1, :] + allpypy_pitch_perc[2, :]
                                + allpypy_pitch_perc[3, :] + allpypy_pitch_perc[4, :],
                         color=color_list[5])

            plt.ylabel('Percentage of Time', fontsize=15)
            plt.xlabel('Sequence no.', fontsize=15)
            # plt.title('Percentage of Time watched per Sequence (#%s time) within given Pitch ranges' % (j + 1), y=1.12,
            #           fontsize=16)
            plt.xticks(ind, [s.replace('.mp4', '') for s in sequences], fontsize=15)
            plt.ylim(ymax=105, ymin=0)
            plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), labels, bbox_to_anchor=(0., 1.02, 1., .102),
                       loc=3, ncol=3, mode="expand", borderaxespad=0., fontsize=15)
            plt.show()
            fig.savefig("results\\plots\\barcharts\\barchart_all_time%s_pitch.%s" % (j + 1, image_format),
                        bbox_inches='tight', dpi=300)

            # Yaw plots
            ind = np.arange(no_videos)
            labels = "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr1_y, nr2_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr2_y, nr3_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr3_y, nr4_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr4_y, nr5_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr5_y, nr6_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (nr6_y, pr1_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr1_y, pr2_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr2_y, pr3_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr3_y, pr4_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr4_y, pr5_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr5_y, pr6_y),\
                     "[%s\N{DEGREE SIGN}, %s\N{DEGREE SIGN}]" % (pr6_y, pr7_y)
            allpypy_yaw_perc = np.zeros((allpy_yaw_no_bins, no_videos), dtype=np.float64)
            for k in range(0, allpy_yaw_no_bins):
                for sequence in sequences:
                    seqindex = sequences.index(sequence)
                    overall_data_points = sum(subjects_noncumulative_range_allpy_yaw[j, seqindex, :])
                    # Divide by the number of data point in all bins
                    allpypy_yaw_perc[k, seqindex] = \
                        (subjects_noncumulative_range_allpy_yaw[j, seqindex, k] / overall_data_points) * 100
            fig = plt.figure(figsize=(12, 9))
            p1 = plt.bar(ind, allpypy_yaw_perc[0, :], width, color=color_list[0])
            p2 = plt.bar(ind, allpypy_yaw_perc[1, :], width, bottom=allpypy_yaw_perc[0, :], color=color_list[1])
            p3 = plt.bar(ind, allpypy_yaw_perc[2, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :],
                         color=color_list[2])
            p4 = plt.bar(ind, allpypy_yaw_perc[3, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :],
                         color=color_list[3])
            p5 = plt.bar(ind, allpypy_yaw_perc[4, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :],
                         color=color_list[4])
            p6 = plt.bar(ind, allpypy_yaw_perc[5, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :],
                         color=color_list[5])
            p7 = plt.bar(ind, allpypy_yaw_perc[6, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :],
                         color=color_list[6])
            p8 = plt.bar(ind, allpypy_yaw_perc[7, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                                + allpypy_yaw_perc[6, :],
                         color=color_list[7])
            p9 = plt.bar(ind, allpypy_yaw_perc[8, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                                + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :],
                         color=color_list[8])
            p10 = plt.bar(ind, allpypy_yaw_perc[9, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                                + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :] + allpypy_yaw_perc[8, :],
                         color=color_list[9])
            p11 = plt.bar(ind, allpypy_yaw_perc[10, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                                + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :] + allpypy_yaw_perc[8, :]
                                + allpypy_yaw_perc[9, :],
                         color=color_list[10])
            p12 = plt.bar(ind, allpypy_yaw_perc[11, :], width,
                         bottom=allpypy_yaw_perc[0, :] + allpypy_yaw_perc[1, :] + allpypy_yaw_perc[2, :]
                                + allpypy_yaw_perc[3, :] + allpypy_yaw_perc[4, :] + allpypy_yaw_perc[5, :]
                                + allpypy_yaw_perc[6, :] + allpypy_yaw_perc[7, :] + allpypy_yaw_perc[8, :]
                                + allpypy_yaw_perc[9, :] + allpypy_yaw_perc[10, :],
                         color=color_list[11])
            plt.ylabel('Percentage of Time', fontsize=15)
            plt.xlabel('Sequence no.', fontsize=15)
            # plt.title('Percentage of Time watched per Sequence (#%s time) within given Yaw ranges' % (j + 1), y=1.16,
            #           fontsize=16)
            plt.xticks(ind, [s.replace('.mp4', '') for s in sequences], fontsize=15)
            plt.ylim(ymax=105, ymin=0)
            plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0],
                        p8[0], p9[0], p10[0], p11[0], p12[0]), labels, bbox_to_anchor=(0., 1.02, 1., .102),
                       loc=3, ncol=4, mode="expand", borderaxespad=0., fontsize=15)
            plt.show()
            fig.savefig("results\\plots\\barcharts\\barchart_all_time%s_yaw.%s" % (j + 1, image_format),
                        bbox_inches='tight', dpi=300)


def plotHeatmaps(merged_data, hmd, sequences, sample_number, times_watched, quality_levels, invert_py, image_format):
    """
    Plot heatmaps for every subject

    The plots are done twice: a) while considering only Min/Max pitch and yaw values and
    b) considering every recorded pitch and yaw value.
    You need to place some video thumbnails in the images folder to receive overlayed heatmaps (best: JPEG format)!

    :param merged_data: The merged AVTrack360 dataset.
    :param hmd: The HMD to use.
    :param sequences: The sequences to process.
    :param sample_number: The number of samples (AVTrack360 records roughly 200 values per second).
    :param times_watched: The number of times watching the content.
    :param quality_levels: Specify the number of quality levels to summarize the data of all quality levels
    and multiple times watched for each video.
    :param invert_py: Invert the pitch and yaw values.
    :param image_format: The format to write the image (pdf, png etc.).
    """
    plt.ion()  # Needed in order to close figures and write them automatically

    # Initialization of variables
    subjects = len(merged_data['merged_data'])
    no_videos = len(sequences)

    # ((times_watched_sequence, number_of_sequences, pitch_yaw_roll_time, sample_number, subjects))
    subjects_pyrt_data_angle = helpers.getPyrtDataInArray(merged_data, hmd, sequences, sample_number, False,
                                                          quality_levels, times_watched)

    if quality_levels != 1:
        # Close all figures before so we get no memory RuntimeWarning
        # Open figure before plotting loop
        plt.close("all")
        fig = plt.figure(figsize=(24.0, 16.0))
        fig.suptitle("Heatmaps of all sequences watched", size=16, y=0.94)

        # IMPORTANT: Adapt this part to your needs or correct the calculation of the maximum range!
        for j in range(0, int(len(sequences) / (quality_levels))):
            yaw_values = []
            pitch_values = []
            for k in range(0, times_watched):
                for q in range(0, quality_levels):
                    for i in range(0, subjects):
                        try:
                            for x in range(0, sample_number):
                                pitch_value = subjects_pyrt_data_angle[k, j * quality_levels + q, 0, x, i]
                                yaw_value = subjects_pyrt_data_angle[k, j * quality_levels + q, 1, x, i]
                                if np.isnan(pitch_value) or np.isnan(yaw_value):
                                    None
                                else:
                                    if invert_py:
                                        yaw_value = yaw_value * -1
                                    else:
                                        pitch_value = pitch_value * -1
                                    pitch_values.append(pitch_value)
                                    yaw_values.append(yaw_value)
                        except IndexError:
                            None

            # Plot the heatmaps
            img = plt.imread("images/%s.jpg" % (j + 1))
            ax = plt.subplot(3, 2, j + 1)
            ax.set_title("Sequence %s" % (j + 1), size=14)
            ax.set_ylabel("Pitch [Deg]", size=14)
            ax.set_xlabel("Yaw [Deg]", size=14)
            heatmap, xedges, yedges = np.histogram2d(yaw_values, pitch_values, bins=20, range=[[-180, 180], [-90, 90]])
            # Modify axis ticks depending on definition of pitch and yaw
            if invert_py:
                extent = [xedges[-1], xedges[0], yedges[0], yedges[-1]]
            else:
                extent = [xedges[0], xedges[-1], yedges[-1], yedges[0]]
            ax.imshow(img, extent=extent)
            ax.imshow(heatmap.T, extent=extent, origin='lower', alpha=.8, interpolation='bilinear')

        fig.savefig("results\\plots\\heatmaps\\heatmaps_summarized.%s" % (image_format), bbox_inches='tight', dpi=300)
    else:
        # Close all figures before so we get no memory RuntimeWarning
        # Open figure before plotting loop
        plt.close("all")
        fig = plt.figure(figsize=(32.0, 24.0))
        fig.suptitle("Heatmaps of all videos watched (seen for all times watched)", size=16, y=0.91)

        for j in range(0, no_videos):
            for k in range(0, times_watched):
                yaw_values = []
                pitch_values = []
                for i in range(0, subjects):
                    try:
                        for x in range(0, sample_number):
                            pitch_value = subjects_pyrt_data_angle[k, j, 0, x, i]
                            yaw_value = subjects_pyrt_data_angle[k, j, 1, x, i]
                            if np.isnan(pitch_value) or np.isnan(yaw_value):
                                None
                            else:
                                if invert_py:
                                    yaw_value = yaw_value * -1
                                else:
                                    pitch_value = pitch_value * -1
                                pitch_values.append(pitch_value)
                                yaw_values.append(yaw_value)
                    except IndexError:
                        None

            # Plot the heatmaps
            img = plt.imread("images/%s.jpg" % (sequences[j].replace(".mp4", "")))
            ax = plt.subplot(5, 4, j + 1)
            ax.set_title("Sequence %s" % (sequences[j].replace(".mp4", "")), size=14)
            ax.set_ylabel("Pitch [Deg]", size=14)
            ax.set_xlabel("Yaw [Deg]", size=14)
            heatmap, xedges, yedges = np.histogram2d(yaw_values, pitch_values, bins=20, range=[[-180, 180], [-90, 90]])
            # Modify axis ticks depending on definition of pitch and yaw
            if invert_py:
                extent = [xedges[-1], xedges[0], yedges[0], yedges[-1]]
            else:
                extent = [xedges[0], xedges[-1], yedges[-1], yedges[0]]
            ax.imshow(img, extent=extent)
            ax.imshow(heatmap.T, extent=extent, origin='lower', alpha=.6, interpolation='bilinear')

        fig.savefig("results\\plots\\heatmaps\\heatmaps_per_video.%s" % (image_format), bbox_inches='tight', dpi=300)


def plotOverTimeVelocity(merged_data, hmd, sequences, sample_number, times_watched, quality_levels, image_format):
    """
    Plot the color coded velocity over time for each subject and video.

    :param merged_data: The merged AVTrack360 dataset.
    :param hmd: The HMD to use.
    :param sequences: The sequences to process.
    :param sample_number: The number of samples (AVTrack360 records roughly 200 values per second).
    :param times_watched: The number of times watching the content.
    :param quality_levels: Specify the number of quality levels to summarize the data of all quality levels
    and multiple times watched for each video.
    :param image_format: The format to write the image (pdf, png etc.).
    """
    plt.ion()  # Needed in order to close figures and write them automatically

    # Initialization of variables
    subjects = len(merged_data['merged_data'])
    no_videos = len(sequences)

    # ((times_watched_sequence, number_of_sequences, pitch_yaw_roll_time, sample_number, subjects))
    subjects_pyrt_data_angle = helpers.getPyrtDataInArray(merged_data, hmd, sequences, sample_number, False,
                                                          quality_levels, times_watched)
    subjects_pyr_data_velocity = helpers.getPYRVelocityInArray(subjects_pyrt_data_angle, times_watched,
                                                                sequences, sample_number, subjects)
    subjects_pyr_data_velocity = np.nan_to_num(subjects_pyr_data_velocity)
    pyr_description = ["Pitch", "Yaw", "Roll"]
    pyr_vmax = [60, 120, 30]

    if quality_levels != 1:
        None
    else:
        # Close all figures before so we get no memory RuntimeWarning
        # Open figure before plotting loop
        plt.close("all")
        for k in range(0, times_watched):
            for pyr in range(0, 3):
                fig = plt.figure(figsize=(32.0, 24.0))
                fig.suptitle("Color coded pitch velocity diagrams for all sequences watched (%s time watched)" % (k + 1), size=16,
                             y=0.91)
                for j in range(0, no_videos):
                    ax = plt.subplot(9, 3, j + 1)
                    ax.set_title("Sequence %s" % (sequences[j].replace(".mp4", "")), size=14)
                    ax.set_ylabel("Subject no.", size=14)
                    ax.set_xlabel("Time [s]", size=14)
                    ax.set_xticklabels(np.arange(-5, 35, 5))
                    im = ax.imshow(np.abs(np.transpose(subjects_pyr_data_velocity[k, j, pyr, 0:sample_number - 7, :])),
                               interpolation='none', vmin=0, vmax=pyr_vmax[pyr])
                cbaxes = fig.add_axes([0.68, 0.315, 0.2, 0.01])
                cbar = fig.colorbar(im, cax=cbaxes, orientation='horizontal')
                cbar.ax.set_xlabel("Angular %s Speed in Deg/s" % (pyr_description[pyr]))
                fig.savefig("results\\plots\\overtime_velocity\\overtime_velocity_time%s_%s.%s"
                            % (k + 1, pyr_description[pyr], image_format), dpi=400, bbox_inches='tight')
