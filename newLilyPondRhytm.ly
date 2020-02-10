#(define mydrums '(         
(bassdrum        default   #f           -3)
(hihat           cross     #f           4)))
\version "2.18.2"
\paper{
  indent=0\mm
  line-width=120\mm
  oddFooterMarkup=##f
  oddHeaderMarkup=##f
  bookTitleMarkup = ##f
  scoreTitleMarkup = ##f
}

up = \drummode { hh8 hh hh hh <hh> hh hh hh  }
down = \drummode {  r4   r8 bassdrum8 snare4   bassdrum8 bassdrum8  }
    \new DrumStaff <<
    \set DrumStaff.drumStyleTable = #(alist->hash-table mydrums)
    \new DrumVoice { \voiceOne \up }
    \new DrumVoice { \voiceTwo \down }
>>