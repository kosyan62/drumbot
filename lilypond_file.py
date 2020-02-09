def get_lilypond_drum_file(line1, line2):
    str = """#(define mydrums '(         
(bassdrum        default   #f           -3)
(hihat           cross     #f           4)))
\paper{
  indent=0\mm
  line-width=120\mm
  oddFooterMarkup=##f
  oddHeaderMarkup=##f
  bookTitleMarkup = ##f
  scoreTitleMarkup = ##f
}

up = \drummode { %s }
down = \drummode { %s }
    \\new DrumStaff <<
    \\set DrumStaff.drumStyleTable = #(alist->hash-table mydrums)
    \\new DrumVoice { \\voiceOne \up }
    \\new DrumVoice { \\voiceTwo \down }
>>""" % (line1, line2)
    filename = 'newLilyPondRhytm.ly'
    lilyfile = open(filename, "w+")
    lilyfile.write(str)
    lilyfile.close()
    return filename
