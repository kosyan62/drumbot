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

up = \drummode { hh8 hh hh hh <hh snare> hh hh hh hh8 hh hh hh <hh snare> hh hh hh hh8 hh hh hh <hh snare> hh hh hh hh8 hh hh hh <hh snare> hh hh hh  }
down = \drummode {  bassdrum4   r8 bassdrum8 \skip 8 bassdrum8 bassdrum4    r8 bassdrum8 r8 bassdrum8 \skip 8 bassdrum8 r8 bassdrum8  r4   bassdrum4   \skip 8 bassdrum8 bassdrum4    bassdrum4   r8 bassdrum8 \skip 8 bassdrum8 bassdrum8 bassdrum8  }
    \new DrumStaff <<
    \set DrumStaff.drumStyleTable = #(alist->hash-table mydrums)
    \new DrumVoice { \voiceOne \up }
    \new DrumVoice { \voiceTwo \down }
>>