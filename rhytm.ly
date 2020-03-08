#(define mydrums '(         
(bassdrum        default   #f           -3)
(hihat           cross     #f           4)))
\version "2.18.2"
\paper{
  indent=10\mm
  oddFooterMarkup=##f
  oddHeaderMarkup=##f
  bookTitleMarkup = ##f
  scoreTitleMarkup = ##f
}

up = \drummode { hh8 hh <hh> hh hh8 hh <hh> hh  }
down = \drummode {  bassdrum4 snare4  r8. bassdrum16 snare16 bassdrum16 bassdrum16 bassdrum16  }
    \new DrumStaff <<
    \set DrumStaff.drumStyleTable = #(alist->hash-table mydrums)
    \new DrumVoice { \voiceOne \up }
    \new DrumVoice { \voiceTwo \down }
>>