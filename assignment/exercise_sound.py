#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)
    
# frequencies note:
notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88,
    "C5": 523.25
}

melody = [
    ("C", 0.5), ("C", 0.5), ("G", 0.5), ("G", 0.5),  # Twinkle, Twinkle
    ("A", 0.5), ("A", 0.5), ("G", 1.0),             # Little Star
    ("F", 0.5), ("F", 0.5), ("E", 0.5), ("E", 0.5),  # How I Wonder
    ("D", 0.5), ("D", 0.5), ("C", 1.0)              # What You Are
]


# play the melody
print("Playing melody:")

for note, duration in melody:
    if note in notes:
        frequency = notes[note]
        print(f"Playing: {note} ({frequency} Hz)")
        playtone(frequency, duration)
    quiet()
    utime.sleep(0.1)


quiet() # turn off the PWM
