from lilypond_file import get_lilypond_drum_file
import subprocess
import tempfile
from pdf2image import convert_from_path, convert_from_bytes
import rhytm_generator

hard = 3
hihat = rhytm_generator.get_hh_str()
fin = (rhytm_generator.get_drumbit_str())
if hard == 2:
    hihat *= 2
    fin += (rhytm_generator.get_drumbit_str())
elif hard == 3:
    hihat *= 4
    fin += (rhytm_generator.get_drumbit_str())
    fin += (rhytm_generator.get_drumbit_str())
    fin += (rhytm_generator.get_drumbit_str())

filename = get_lilypond_drum_file(hihat, fin)
subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
        '-dinclude-eps-fonts', '--pdf', filename])
