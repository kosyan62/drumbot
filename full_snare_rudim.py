from note import Note
import notation
from lilypond_file import get_lilypond_drum_file
from pdf2image import convert_from_path
import random
import subprocess

def get_snare():
    fill = []
    arr = "RLRLRLRLRLRLRLRL"
    arr = list(arr)
    for i in arr:
        hit = Note(16, 'snare')
        hit.add_hand(i)
        fill.append(hit)
    for i in range(4):
        l = random.randint(1,4)
        notation.add_accent(fill, (i * 4) + l)
    snare = notation.get_string(fill)
    filename = get_lilypond_drum_file(snare, "")
    subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
            '-dinclude-eps-fonts', '--pdf', filename])
    image = convert_from_path('rhytm.pdf')
    image[0].save('rhytm.png')

