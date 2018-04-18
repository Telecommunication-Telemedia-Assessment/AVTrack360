# AVTrack360 Evaluation

Here, some Python scripts are located to evaluate the data recorded by AVTrack360.

## Installation

If Python throws errors because of missing packages, please install them via calling the respective `pip` command.
It runs with the latest [Python 3.6.x](https://www.python.org/downloads) version.
Using Windows, it is most easy to use [Anaconda](https://www.anaconda.com/download) for running this tool.
It is recommended to work with virtual Python environments.
The virtual environment containing all necessary dependencies for this tool can be installed by running the respective command (administrative permission may be required):
`conda env create -f environment.yml`
The respective created environment can be activated by
`activate pyavtrack360eval`

## Directory structure

`/data_modified` - Containing the modified and the merged datasets. <br />
`/data` - Containing the original data recorded by AVTrack360. <br />
`/results` - Containing all plots. <br />
`/videos` - Containing the videos used within the test. <br />


## Usage

At first run `shift_cut_merge.py` with the respective parameters to merge the dataset to one file so it can be easier processed by the evaluation scripts.
Afterwards, `main.py` can be run with the respective parameters to create the required plots. For more detailed information, please refer to the help `-h`.
It could be, that for specific test purposes, the scripts need to get adapted. Feel free to do so.
