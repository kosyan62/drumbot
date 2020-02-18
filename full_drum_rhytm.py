import rhytm_generator
from lilypond_file import get_lilypond_drum_file
import subprocess
from pdf2image import convert_from_bytes

def get_rhytm(x):
    hihat, fin = '', ''
    for i in range(x):
        hihat += rhytm_generator.get_hh_str()
        fin += (rhytm_generator.get_drumbit_str())
    filename = get_lilypond_drum_file(hihat, fin)
    subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
            '-dinclude-eps-fonts', '--pdf', filename])
    images = convert_from_bytes(open('rhytm.pdf', 'rb').read())
    images[0].save('rhytm.png')

#def get_rudim:

#def get_snare:

