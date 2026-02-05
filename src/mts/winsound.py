import sounddevice as sd
import numpy as np

def Beep(frequency: float, duration_in_seconds: float):

    # Duration and frequency of the sound
    # duration = 1.0  # in seconds
    # frequency = 432.0  # in Hz, A4 note

    # Generate a time array
    sample_rate = 44_100  # samples per second
    t = np.linspace(0, duration_in_seconds, int(sample_rate * duration_in_seconds), endpoint=False)

    # Generate a sine wave
    y = np.sin(2 * np.pi * frequency * t)

    # Play the sound
    sd.play(y, sample_rate)

    # Wait for the sound to finish playing
    sd.wait()
