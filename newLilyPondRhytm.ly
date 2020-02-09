#(define mydrums '(         
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

up = \drummode { hh4 hh hh hh }
down = \drummode {  r8 bassdrum r4 snare4 bassdrum4  }
    \new DrumStaff <<
    \set DrumStaff.drumStyleTable = #(alist->hash-table mydrums)
    \new DrumVoice { \voiceOne \up }
    \new DrumVoice { \voiceTwo \down }
>>