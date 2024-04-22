import numpy as np
import pygame
import time

# Initialize Pygame Mixer
pygame.mixer.init(44100, -16, 1, 512)

# ASCII Art representations for notes
ascii_art = {
    'C': '''
    -----
   |     |
 C |     |
   |     |
    -----
    ''',
    'E': '''
    -----
   |  E  |
   |     |
   |  E  |
    -----
    ''',
    'G': '''
    -----
   |  G  |
   |     |
   |  G  |
    -----
    '''
}

# Define a function to play a note and display ASCII Art
def play_note(frequency, duration, note_name):
    # Print ASCII Art for the note
    print(f"Playing note {note_name}:")
    print(ascii_art[note_name])

    # # size = 44100
    # # buffer = pygame.sndarray.array(
    # #     (4096 * np.sin(2.0 * np.pi * np.arange(int(duration * 44100)) * frequency / 44100)).astype(np.int16)
    # # )
    # # buffer = np.repeat(buffer.reshape(size, 1), 2, axis = 1)

    # # Generate a sound at a given frequency (Hz)
    # sound = pygame.sndarray.make_sound(pygame.sndarray.array(
    #     (4096 * np.sin(2.0 * np.pi * np.arange(int(duration * 44100)) * frequency / 44100)).astype(np.int16)
    # ))
    # # sound = pygame.sndarray.make_sound(buffer)
    # sound.play(-1)
    # time.sleep(duration)
    # sound.stop()

    # Generate a mono sound array
    mono_sound = (4096 * np.sin(2.0 * np.pi * np.arange(int(duration * 44100)) * frequency / 44100)).astype(np.int16)
    
    # Duplicate the mono sound in both channels for stereo effect
    stereo_sound = np.empty((len(mono_sound), 2), dtype=np.int16)
    stereo_sound[:, 0] = mono_sound
    stereo_sound[:, 1] = mono_sound
    
    # Generate and play the stereo sound
    sound = pygame.sndarray.make_sound(stereo_sound)
    sound.play(-1)
    time.sleep(duration)
    sound.stop()

# Define the musical sequence
def play_sequence():
    # Notes dictionary (simplified frequencies for demo)
    notes = {
        'C': 261.63,  # Frequency of Middle C in Hz
        'E': 329.63,  # E note
        'G': 392.00   # G note
    }
    sequence = [
        ('C', 0.5), ('C', 0.5), ('C', 0.5), ('G', 0.5), 
        ('C', 0.5), ('C', 0.5), ('C', 0.5), ('C', 0.5), 
        ('C', 0.5), ('C', 0.5), ('C', 0.5), ('C', 0.5), 
        ('C', 0.5), ('G', 0.5), ('C', 0.5), ('C', 0.5), 
        ('C', 0.5), ('C', 0.5), ('C', 0.5), ('C', 0.5)
    ]
    for note, dur in sequence:
        play_note(notes[note], dur, note)

# Play the sequence
if __name__ == '__main__':
    play_sequence()