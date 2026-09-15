import os
import pydub
from model import converter_wav


def downloader(file_path):
    """Convert/load an audio file and export a mono WAV for analysis."""
    converted_file = converter_wav(file_path)

    original_audio = pydub.AudioSegment.from_file(converted_file, format="wav")
    global audioFile
    audioFile = os.path.splitext(converted_file)[0] + "_modified.wav"

    mono_audio = original_audio.set_channels(1)
    mono_audio.export(audioFile, format="wav", tags={})

    result = os.path.exists(audioFile)
    print(result)
    return audioFile
