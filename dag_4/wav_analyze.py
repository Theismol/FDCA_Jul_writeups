import wave

import numpy as np
from scipy.fft import fft, fftfreq

dtmf_freqs = {
    (697, 1209): "1",
    (697, 1336): "2",
    (697, 1477): "3",
    (770, 1209): "4",
    (770, 1336): "5",
    (770, 1477): "6",
    (852, 1209): "7",
    (852, 1336): "8",
    (852, 1477): "9",
    (941, 1336): "0",
    (697, 1633): "A",
    (770, 1633): "B",
    (852, 1633): "C",
    (941, 1633): "D",
}


def load_wav_file(filepath):
    with wave.open(filepath, "r") as wav_file:
        params = {
            "n_channels": wav_file.getnchannels(),
            "sampwidth": wav_file.getsampwidth(),
            "framerate": wav_file.getframerate(),
            "n_frames": wav_file.getnframes(),
            "duration": wav_file.getnframes() / wav_file.getframerate(),
        }
        frames = wav_file.readframes(wav_file.getnframes())
        audio_data = np.frombuffer(frames, dtype=np.int16)
    return audio_data, params


def trim_audio(audio_data, framerate, noise_duration):
    start_index = int(noise_duration * framerate)
    return audio_data[start_index:]


def segment_audio(audio_data, framerate, segment_duration):
    segment_length = int(segment_duration * framerate)
    return [
        audio_data[i : i + segment_length]
        for i in range(0, len(audio_data), segment_length)
    ]


def identify_dtmf(signal, framerate):
    fft_spectrum = fft(signal)
    freqs = fftfreq(len(fft_spectrum), d=1 / framerate)
    magnitude = np.abs(fft_spectrum)

    positive_freqs = freqs[freqs > 0]
    positive_magnitude = magnitude[freqs > 0]

    dominant_freqs = positive_freqs[np.argsort(positive_magnitude)[-2:]]

    dominant_freqs = np.round(dominant_freqs).astype(int)

    for (low, high), digit in dtmf_freqs.items():
        if low in dominant_freqs and high in dominant_freqs:
            return digit
    return None


def analyze_wav(filepath):
    audio_data, params = load_wav_file(filepath)
    framerate = params["framerate"]
    trimmed_audio = trim_audio(audio_data, framerate, 12)
    segments = segment_audio(trimmed_audio, framerate, 1)
    detected_digits = []
    for segment in segments:
        digit = identify_dtmf(segment, framerate)
        if digit:
            detected_digits.append(digit)
    return detected_digits


if __name__ == "__main__":
    file_path = "OpsnappetOpkald.wav"
    detected_digits = analyze_wav(file_path)
    print("Detected DTMF sequence:", "".join(detected_digits))
