# AVTrack360

AVTrack360 is a Framework for recording head rotation data while playing back a 360 degree video with an HMD-device.
It records the 3 rotation angles Pitch/Yaw/Roll around the 3 Axes X/Y/Z in synchronization to the player every 100ms.
It also can obtain an ACR rating score after every video played.
It is tested for Windows (version 7 +) devices.

Currently supported HMD-devices:
- Oculus Rift CV 1
- HTC Vive

Currently supported Player:
- [Whirligig (free ZIP version)](http://www.whirligig.xyz/new-page-3)

## Installation

AVTrack360 requires the specific runtimes for the HMD to use:
* [Oculus Rift native Windows packages](https://developer.oculus.com/downloads/native-windows)
* [HTC Vive developer portal](https://developer.viveport.com/de/develop_portal)

For enabling Whirligig to successfully play a variety of media formats, installing some Codecs is necessary (e.g. [LAV DirectShow filter pack](https://github.com/Nevcairiel/LAVFilters/releases)).
It runs with the latest [Python 2.7.x](https://www.python.org/downloads) version.
Using Windows, it is most easy to use [Anaconda](https://www.anaconda.com/download) for running this tool.
It is recommended to work with virtual Python environments.
The virtual environment containing all necessary dependencies for this tool can be installed by running the respective command (administrative permission may be required):
`conda env create -f environment.yml`
The respective created environment can be activated by
`activate pyavtrack360rec`

Afterwards, the tool is ready to run.

## Directory structure

`/data` - Containing recorded head treacking data. <br />
`/playlists` - Containing playlists. <br />
`/tools` - Containing tools as e.g. Whirligig or FFmpeg. Please don't change anything here. <br />
`/videos` - Containing videos for playback. <br />


## Usage

At first, the respective runtimes for the HMD (Oculus/SteamVR) need to be started. When using the Oculus Rift you would also have to agree on this health safety warning.
When using the HTC Vive, please minimize the respective SteamVR windows before starting AVTrack360 as otherwise there could be some problems in the window focus of the player.

If you want to know, which parameters are available for AVTrack360, just call
```
python main.py -h
```

The most common way to use AVTrack360 will be to give a unique playlist for each subject containing every video you want to play via the `-plist` argument.
This JSON-file has to contain all necessary metainformation like the label and the information about the videos (like filename, projection scheme and HMD to use).
You can find an example playlist in the `/playlists` folder called `1 Demo.json`.
Every playlist has to follow this scheme, otherwise AVTrack360 would not be able to parse and use the information and errors could occur.

One possible command to start AVTrack360 using automatic video playback, playing back 16 videos (e.g. one test session) and asking for ACR input in the command line after each video would be:
```
python main.py -autoplay -multiplay 16 -acr -plist ".json"
```

### Creating playlists
If you want to create the playlist via Microsoft Excel, create it in the same way as demonstrated in `/playlists/dummy.xlsx` and save it to the CSV MS-DOS format.
For converting the CSV file to a JSON playlist file which could be processed by AVTrack360, call `python playlist_tool.py`. With the `-csvfile` parameter you can specify the name of the CSV file to convert.
The playlists will be saved in the respective folder.
Alternatively, you also can create your own playlists by directly using the `playlist_tool.py` script.
Please take a look at the main function of this script for setting up the creation due to your wishes.


## Troubleshooting
* If Whirligig doesn't show any image, consider installing some LAV filters from e.g. [official LAV GitHub repository](https://github.com/Nevcairiel/LAVFilters/releases)
* If Whirligig doesn't show a mirror image of the HMD, press `m` in Whirligig for activating mirroring again

## Used software:
* [ffmpeg-3.3.3-win32-static](https://ffmpeg.zeranoe.com/builds/)
* [Whirligig v3.92](http://www.whirligig.xyz/player2-1-2/)
