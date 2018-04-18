import numpy as np


def calculateAngleVelocity(t0, t1, delta_t):
    """
    Returns the velocity in degrees per second between two given angles at timestamps t and t+1 and the
    difference between those two timestamps.

    :param t0: The angle value at timestamp t.
    :param t1: The angle value at timestamp t+1.
    :param delta_t: The difference between the two values.
    :return: The velocity in degrees per second.
    """
    if abs(t1 - t0) > 180 and t0 < t1:
        delta_a = 180 - abs(t0) + 180 - abs(t1)
    elif abs(t1 - t0) > 180 and t0 > t1:
        delta_a = (180 - abs(t0) + 180 - abs(t1)) * -1
    else:
        delta_a = t1 - t0
    return delta_a / delta_t


def getPyrtDataInArray(merged_data, hmd, sequences, sample_number, sort_by_playlist, quality_levels, times_watched):
    """
    Returns the Pitch/Yaw/Roll/Time data of all subjects in a 5 dimensional array.

    :param merged_data: The merged AVTrack360 dataset.
    :param hmd: The HMD to use.
    :param sequences: The sequences to process.
    :param sample_number: The number of samples (AVTrack360 records roughly 200 values per second).
    :param sort_by_playlist: Activate if the "times watched" definition should not be based on 1st and 2nd time watched
    per quality level, but be based on watching the video itself for the really 1st, 2nd [...] time.
    :param quality_levels: Specify the number of quality levels to summarize the data of all quality levels
    and multiple times watched for each video.
    :param times_watched: The number of times watching the content.
    :return: subjects_pyrt_data_angle =
    ((times_watched_sequence, number_of_sequences, pitch_yaw_roll_time, sample_number, subjects))
    """
    # Initialization of variables
    subjects = len(merged_data['merged_data'])
    if not sort_by_playlist:
        no_sequences = len(sequences)
    else:
        no_sequences = int(len(sequences) / quality_levels)
        times_watched = times_watched * quality_levels
    subjects_pyrt_data_angle = np.zeros((times_watched, no_sequences, 4, sample_number, subjects), dtype=np.float64)
    subjects_pyrt_data_angle[:] = np.nan

    if not sort_by_playlist:
        # Get the data of all subjects and the relevant combinations of HMD and sequence
        # Considering the specific quality level was watched
        for i in range(0, subjects):
            for sequence in sequences:
                sequence_watched_counter = 0
                # Loop over every video
                for j in range(len(merged_data['merged_data'][i]["data"])):
                    # Only consider respective HMD/Sequence combination
                    if merged_data['merged_data'][i]["data"][j]["hmd"] == hmd and \
                                    merged_data['merged_data'][i]["data"][j]["filename"] == sequence:
                        sequence_watched_counter += 1
                        for x in range(sample_number):
                            try:
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequences.index(sequence), 0, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["pitch"]
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequences.index(sequence), 1, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["yaw"]
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequences.index(sequence), 2, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["roll"]
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequences.index(sequence), 3, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["sec"]
                            except IndexError:
                                None
                        # Reset the counter if both videos already were processed
                        if sequence_watched_counter >= times_watched:
                            sequence_watched_counter = 0
    else:
        # Get the data of all subjects and the relevant combinations of HMD and sequence
        # Considering the order the video was watched in the playlist
        for i in range(0, subjects):
            for sequence in range(0, no_sequences):
                sequence_watched_counter = 0
                # Loop over every video
                for j in range(len(merged_data['merged_data'][i]["data"])):
                    # Only consider respective HMD/Sequence combination
                    if merged_data['merged_data'][i]["data"][j]["hmd"] == hmd and\
                            merged_data['merged_data'][i]["data"][j]["filename"][0].isdigit() and\
                            int(merged_data['merged_data'][i]["data"][j]["filename"][0]) == sequence + 1:
                        sequence_watched_counter += 1
                        for x in range(sample_number):
                            try:
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequence, 0, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["pitch"]
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequence, 1, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["yaw"]
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequence, 2, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["roll"]
                                subjects_pyrt_data_angle[sequence_watched_counter-1, sequence, 3, x, i] = \
                                    merged_data['merged_data'][i]["data"][j]["pitch_yaw_roll_data_hmd"][x]["sec"]
                            except IndexError:
                                None

    return subjects_pyrt_data_angle

def getPYRVelocityInArray(subjects_pyrt_data_angle, times_watched, sequences, sample_number, subjects):
    """
    Get the pitch, yaw and roll velocity for each data point (hence t_1 - t_0) / delta_t) while t_1 and
    t_0 are representing the respective values at the respective timestamps.

    :param subjects_pyrt_data_angle: The pitch/yaw/roll/time array calculated by the respective function. Should contain
    ((times_watched_sequence, number_of_sequences, pitch_yaw_roll_time, sample_number, subjects))
    :param times_watched: The number of times watching the content.
    :param sequences: The sequence list.
    :param sample_number: The number of samples (AVTrack360 records roughly 200 values per second).
    :param subjects: The number of subjects.

    :return subjects_pyr_velcocities: The velocities of all subjects in the following array:
    ((times_watched, no_sequences, pyr, sample_number, subjects))

    """
    no_sequences = len(sequences)

    subjects_pyr_data_velocity = np.zeros((times_watched, no_sequences, 3, sample_number, subjects), dtype=np.float64)
    subjects_pyr_data_velocity[:] = np.nan
    for i in range(0, subjects):
        for sequence in sequences:
            for j in range(0, times_watched):
                for x in range(0, sample_number - 1):
                    p_t0 = subjects_pyrt_data_angle[j, sequences.index(sequence), 0, x, i]
                    p_t1 = subjects_pyrt_data_angle[j, sequences.index(sequence), 0, x + 1, i]
                    y_t0 = subjects_pyrt_data_angle[j, sequences.index(sequence), 1, x, i]
                    y_t1 = subjects_pyrt_data_angle[j, sequences.index(sequence), 1, x + 1, i]
                    r_t0 = subjects_pyrt_data_angle[j, sequences.index(sequence), 2, x, i]
                    r_t1 = subjects_pyrt_data_angle[j, sequences.index(sequence), 2, x + 1, i]
                    delta_t = subjects_pyrt_data_angle[j, sequences.index(sequence), 3, x + 1, i] -\
                              subjects_pyrt_data_angle[j, sequences.index(sequence), 3, x, i]
                    # Only calculate velocity if delta_t != 0 as otherwise errors occur
                    # delta_t could be zero because for some reason sometimes the latest values are not recorded by AVTrack360
                    if delta_t != np.nan:
                        pitch_velocity = calculateAngleVelocity(p_t0, p_t1, delta_t)
                        yaw_velocity = calculateAngleVelocity(y_t0, y_t1, delta_t)
                        roll_velocity = calculateAngleVelocity(r_t0, r_t1, delta_t)
                        subjects_pyr_data_velocity[j, sequences.index(sequence), 0, x, i] = pitch_velocity
                        subjects_pyr_data_velocity[j, sequences.index(sequence), 1, x, i] = yaw_velocity
                        subjects_pyr_data_velocity[j, sequences.index(sequence), 2, x, i] = roll_velocity
    return subjects_pyr_data_velocity

def ShiftYawTo360CoordinateSystem(yaw_orig):
    """
    Function to shift the input yaw value using coordinate system from -180/0/180 degrees to a coordinate system
    using 0/360 degrees.

    :param yaw_orig: The original yaw value.
    :return yaw: The shifted yaw value.
    """
    yaw = 0
    if yaw_orig < 0:
        yaw = yaw_orig * -1 + 180
    elif yaw_orig == 0:
        yaw = yaw_orig + 180
    elif yaw_orig > 0:
        yaw = 180 - yaw_orig
    return yaw
