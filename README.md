# SPIDAM Acoustic Modeling

Scientific Python Interactive Data Acoustic Modeling (SPIDAM) is a desktop application for loading audio recordings and examining acoustic properties such as waveform behavior, frequency intensity, amplitude, and reverberation-related decay.

This repository is my personal portfolio version of a collaborative project originally developed at Florida Polytechnic University. The original shared repository remains unchanged.

## What the Project Does

SPIDAM provides a graphical interface for selecting an audio file and running several forms of acoustic analysis. The application can:

- Load MP3 or WAV audio
- Convert audio to a mono WAV format for analysis
- Display recording length and maximum amplitude
- Plot the audio waveform
- Create frequency/intensity visualizations
- Plot low, medium, and high decay-threshold graphs
- Compare multiple decay thresholds in a combined visualization

The project was designed around a simple model-view-controller style separation between audio conversion, analysis functions, and the GUI.

## Technologies

- Python
- Tkinter
- NumPy
- SciPy
- Matplotlib
- pydub
- Python wave module

## Project Structure

```text
src/
    app.py          # Tkinter interface
    controller.py   # Audio analysis and plotting
    download.py     # Audio preparation and mono conversion
    model.py        # Audio format conversion
samples/
    clapMP3.mp3
    20241120_121155.wav
requirements.txt
```

## Running the Project

Python 3.12 is recommended because that is the version used during the original project.

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

MP3 conversion through pydub may also require FFmpeg to be installed on your computer and available on your system PATH.

Run the application:

```bash
python src/app.py
```

You can then select your own MP3 or WAV recording, or use one of the files in the `samples` folder.

## Portfolio Version

The original project used several extensionless Python filenames and included some older experimental files alongside the final application. For this personal portfolio copy, the current application files were given standard `.py` names, imports were updated to match those names, setup instructions were added, and the sample recordings were organized into their own folder.

The acoustic-analysis logic remains based on the original team project.

Original shared repository:

https://github.com/korfel713/Project-Scientific-Python-Interactive-Data-Acoustic-Modeling

This repository is presented as collaborative work and is not intended to represent the original project as solo work.
