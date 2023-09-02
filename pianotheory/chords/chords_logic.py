import random

# Notes:
# C - 0
# C# - 1
# D - 2
# D# - 3
# E - 4
# F - 5
# F# - 6
# G - 7
# G# - 8
# A - 9
# A# - 10
# B - 11
LENNOTE = 12
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#","B"]

def generate_random_chord(level: int):
    if level == 1:
        # generate either a major or minor chord
        if random.randint(0, 1) == 0:
            generatedNote = generate_random_major_chord()
            return [NOTES[index % LENNOTE] for index in generatedNote], "major"
        else:
            generatedNote = generate_random_minor_chord()
            return [NOTES[index % LENNOTE] for index in generatedNote], "minor"
    else:
        return [], "perfect"


# returns a list of notes in a major chord
def generate_random_major_chord():
    root_note = random.randint(0, 11)  # Randomly select a root note
    major_interval = [0, 4, 7]
    return [root_note + interval for interval in major_interval]

# returns a list of notes in a minor chord
def generate_random_minor_chord():
    # Similar to above, but for minor chords
    root_note = random.randint(0, 11)  # Randomly select a root note
    minor_interval = [0, 3, 7]
    return [root_note + interval for interval in minor_interval]

