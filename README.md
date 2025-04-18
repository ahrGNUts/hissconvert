# HissConvert

A simple audio file converter tool built in Python that converts audio files from one format to another. Currently only MP3 to WAV is supported with more input/output formats planned later. I'll work on this when I have time and/or feel like it, but you're welcome to submit a pull request if you want to help.

## Features

- Converts MP3 files to WAV format
- Converts to 44.1kHz, 16-bit WAV output
- Command-line interface (for now) 
- Interactive mode when no file path is specified
- Creates converted file in the same directory as the source file

## Requirements

- Python 3.6+
- MoviePy

## Installation

1. Clone this repository
2. Install the required dependencies:

```
pip install moviepy
```

### Using Virtual Environment (Recommended)

It's recommended to use a virtual environment to avoid conflicts with other Python packages:

```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install moviepy

# When finished, deactivate the environment
deactivate
```

## Usage

### Command line

```
python main.py /path/to/your/file.mp3
```

### Interactive mode

```
python main.py
```

When run in interactive mode, the program will prompt you to enter the path to the MP3 file.

## Planned Features

- A UI (maybe using wxPython?)
- Support for additional audio formats (FLAC, AAC, OGG, etc.)
- Configurable output settings (sample rate, bit depth, etc.)
- Configurable output path
- Batch conversion capabilities

## License

[MIT License](LICENSE)