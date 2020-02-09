from lilypond_file import get_lilypond_drum_file
import subprocess
import tempfile
from pdf2image import convert_from_path, convert_from_bytes
import rhytm_generator

basndsnare = rhytm_generator.get_drumbit_str()
hihat = rhytm_generator.get_hh_str()
filename = get_lilypond_drum_file(hihat, basndsnare)
subprocess.call(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', \
        '-dinclude-eps-fonts', '--pdf', filename])
