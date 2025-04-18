import os
import argparse
from moviepy.editor import AudioFileClip


def convert_mp3_to_wav(input_path):
    # Check if file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Check if it's an MP3 file
    if not input_path.lower().endswith('.mp3'):
        raise ValueError(f"Input file is not an MP3: {input_path}")

    # Get directory and filename without extension
    directory = os.path.dirname(input_path) or '.'
    filename = os.path.basename(input_path)
    filename_without_ext = os.path.splitext(filename)[0]

    # Create output path
    output_path = os.path.join(directory, f"{filename_without_ext}.wav")

    # Convert MP3 to WAV using MoviePy
    try:
        audio_clip = AudioFileClip(input_path)
        audio_clip.write_audiofile(output_path, fps=44100, nbytes=2, codec='pcm_s16le')
        audio_clip.close()
        print(f"Successfully converted {input_path} to {output_path}")
        return output_path
    except Exception as e:
        raise RuntimeError(f"Conversion failed: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 file to WAV format")
    parser.add_argument("input_path", nargs='?', help="Path to input MP3 file")
    args = parser.parse_args()

    # If no path provided, prompt the user
    input_path = args.input_path
    if not input_path:
        input_path = input("Please enter the path to the MP3 file: ")

    try:
        convert_mp3_to_wav(input_path)
    except Exception as e:
        print(f"Error: {e}")