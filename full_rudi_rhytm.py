from note import Note
import notation
from rudiments import Rudiments
from lilypond_file import get_lilypond_drum_file
from pdf2image import convert_from_path
import random
import subprocess

def get_rudiments():
    fill = []
    obj = Rudiments()
    arr = obj.get_random_rudim()
    str = ""
    for l in arr:
        str += l;
    arr = str[:16] + (str[16:] and "")
    arr = list(arr)
    for i in arr:
        hit = Note(16, 'snare')
        hit.add_hand(i)
        fill.append(hit)
    snare = notation.get_string(fill)
    filename = get_lilypond_drum_file(snare, "")
    subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
            '-dinclude-eps-fonts', '--pdf', filename])
    image = convert_from_path('rhytm.pdf')
    image[0].save('rhytm.png')

