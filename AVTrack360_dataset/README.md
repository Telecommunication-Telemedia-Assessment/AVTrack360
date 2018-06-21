# AVTrack360 dataset
Within this folder, the AVTrack360 dataset is included. As well as the single files of the recorded head rotation data as the merged dataset is included. Be aware that the dataset does not contain the very first subject.
The Simulator Sickness Questionnaire scores are also included.
The links to the SRCs used can be found below.


## JSON structure
```
{
    "data":[{  // Containing the different captured data of the videos in an array
        "filename":"2.mp4",  // The name of the played back video file.
        "hmd":"vive",  // The name of the used HMD.
        "pitch_yaw_roll_data_hmd":[  // Containing the captured pitch/yaw/roll data and the playback time of the video ("sec").
            {
                "pitch":-13,
                "roll":2,
                "sec":0.266,
                "yaw":0
            },
            ...
        ],
    ...
    ]
}
```

## Directory structure

`/Head_rotation` - Containing the recorded head rotation values (using Euler angles). The subjects always started to watch the video at the initial position (hence yaw=0°) while the range is from 180° to -180°. Pitching the head up results in a negative pitch value, turning the head left leads to a negative yaw value while tilting the head left results in a negative roll value (order of rotation: mathematical negative direction).   <br />
`/images` - Containing some single images describing the content (e.g. for creating heatmaps). <br />
`/SRC_info` - Containing some info on the original SRCs (without the 10s greyscreen appended). <br />
`/SSQ` - Containing the values obtained from the SSQ after the pre-screening and after every session. <br />

## Links to SRCs

* [1 - Icebreaker](https://downloadarte-a.akamaihd.net/arte360/Antarctica_Module_1_2/video/download/4K/Antarctica_Module_1_2_4K.mp4)
* [2 - Fireworks](https://www.youtube.com/watch?v=_J2e8HpT2To)
* [3 - Helicopter](https://downloadarte-a.akamaihd.net/arte360/Antarctica_Module_1_2/video/download/4K/Antarctica_Module_1_2_4K.mp4)
* [4 - Hawaii](https://www.youtube.com/watch?v=c858UGeCeG4)
* [5 - Penguins](https://downloadarte-a.akamaihd.net/arte360/Antarctica_Module_3_2/video/download/4K/Antarctica_Module_3_2_4K.mp4)
* [6 - Diving](https://downloadarte-a.akamaihd.net/arte360/Antarctica_Module_3_2/video/download/4K/Antarctica_Module_3_2_4K.mp4)
* [7 - Colonie](https://downloadarte-a.akamaihd.net/arte360/Colonie360_3/video/download/4K/Colonie360_3_4K.mp4)
* [8 - Childs](https://downloadarte-a.akamaihd.net/arte360/Wasala2/video/download/4K/Wasala2_4K.mp4)
* [9 - Wasala](https://downloadarte-a.akamaihd.net/arte360/Wasala2/video/download/4K/Wasala2_4K.mp4)
* [10 - Carrara](https://downloadarte-a.akamaihd.net/arte360/Carrara1/video/download/4K/Carrara1_4K.mp4)
* [11 - Edge of Space](https://downloadarte-a.akamaihd.net/arte360/Stratos6_VT/video/download/EdgeofSpace_VT_4K_en.mp4)
* [12 - Arcachon](https://downloadarte-a.akamaihd.net/arte360/Arcachon/video/download/4K/Arcachon_4K.mp4)
* [13 - La Grotte Chauvet](https://downloadarte-a.akamaihd.net/arte360/GrotteChauvet/video/download/de/ArtStories360_Grotte-Chauvet_VisualTimeCode_DEU__mobile_4K_offline.mp4)
* [14 - Aliens](https://downloadarte-a.akamaihd.net/arte360/Aliens/video/download/Aliens_VR_english_mobile_4k_offline_injected.mp4)
* [15 - Elisir](https://downloadarte-a.akamaihd.net/arte360/Elisir_Temp_Overlay222/video/download/4K/Elisir_Temp_Overlay222_4K.mp4)
* [16 - Spotlight HELP](https://www.youtube.com/watch?v=G-XZhKqQAHU)
* [17 - Angel Falls](https://www.youtube.com/watch?v=8rUwdtERUOM)
* [18 - Holifest](https://downloadarte-a.akamaihd.net/arte360/Arte-Wolfskinder-Langfilm/video/download/4K/Arte-Wolfskinder-Langfilm_4K.mp4)
* [19 - Nerf battle](https://www.youtube.com/watch?v=JgWUIwqvvow)
* [20 - Football](https://www.youtube.com/watch?v=ZGx1mWonsh8)

## FFmpeg commands
The FFmpeg commands used for cutting the parts of the SRCs used in the tests can be found in `ffmpegcmds.bat`.
