from note import Note
import notation
from rudiments import Rudiments
from lilypond_file import get_lilypond_drum_file
import random
import subprocess

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
for i in range(4):
    l = random.randint(1,4)
    notation.add_accent(fill, (i * 4) + l)
snare = notation.get_string(fill)
filename = get_lilypond_drum_file(snare, "")
subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
        '-dinclude-eps-fonts', '--pdf', filename])

