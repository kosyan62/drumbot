import rhytm_generator
from lilypond_file import get_lilypond_drum_file
import subprocess
from pdf2image import convert_from_path

def get_rhytm(x):
    fin = '' 
    hihat = rhytm_generator.get_hh_str()
    for i in range(x):
        fin += (rhytm_generator.get_drumbit_str())
    hihat *= x
    filename = get_lilypond_drum_file(hihat, fin)
    subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
            '-dinclude-eps-fonts', '--pdf', filename])
    image = convert_from_path('rhytm.pdf')
    image[0].save('rhytm.png')

#def get_rudim:

#def get_snare:

