import rhytm_generator
from lilypond_file import get_lilypond_drum_file
import subprocess

hihat = rhytm_generator.get_hh_str()
fin = (rhytm_generator.get_drumbit_str())
filename = get_lilypond_drum_file(hihat, fin)
subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
        '-dinclude-eps-fonts', '--pdf', filename])

#def get_rudim:

#def get_snare:

