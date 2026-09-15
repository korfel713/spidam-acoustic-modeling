import os
from pydub import AudioSegment


def converter_wav(file_path):
    """Return a WAV version of the selected audio file."""
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".wav":
        return file_path

    output_path = os.path.splitext(file_path)[0] + ".wav"

    if extension == ".mp3":
        audio = AudioSegment.from_mp3(file_path)
    else:
        audio = AudioSegment.from_file(file_path)

    audio.export(output_path, format="wav")
    return output_path
