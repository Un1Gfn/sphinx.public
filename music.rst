.. include:: include/substitution.txt

======================
Music |:musical_note:|
======================

:raw-html:`<details><summary>emoji</summary>`

|:musical_keyboard:|
|:musical_note:|
|:musical_score:|
|:notes:|
|:banjo:|
|:violin:|
|:saxophone:|
|:accordion:|
|:guitar:|
|:drum:|
|:drum_with_drumsticks:|
|:cd:|
|:trumpet:|
|:postal_horn:|

:raw-html:`</details>`

.. tip::

   Grab text from :file:`~/Music/{music.bashrc,readme.md}`

Misc
====

.. code:: text

   [Binks' Sake](https://www.youtube.com/watch?v=e9eN_hhFtVw)

   [music21](http://web.mit.edu/music21/) ([AUR](https://aur.archlinux.org/packages/python-music21/)) - Python+ABC+Lilypond

   <https://www.youtube.com/results?search_query=boogie+woogie+piano> \
   [You can't play WRONG notes this fast!](https://www.youtube.com/watch?v=6_2UHz8OsJI)

   Visualiser
   [Sonic Visualiser]
   https://www.sonicvisualiser.org/
   https://code.soundsoftware.ac.uk/projects/sonic-visualiser/
   https://github.com/sonic-visualiser/sonic-visualiser
   Melodic Range Spectrogram
   Peak Frequency Spectrogram
   https://www.sonicvisualiser.org/videos.html
   https://vimeo.com/qmlivemusiclab
   https://charm.rhul.ac.uk/analysing/p9_1.html
   https://www.izotope.com/en/learn/understanding-spectrograms.html

   AI
   [piano scribe](https://piano-scribe.glitch.me/) \
   [audiveris](https://github.com/Audiveris/audiveris)

   Notation
   [MuseScore](https://github.com/musescore/MuseScore)

   http://lilypond.org/doc/v2.18/Documentation/notation/creating-midi-files
   https://lilypond.org/doc/v2.23/Documentation/notation/piano#piano-pedals
   https://wiki.archlinux.org/title/Timidity++#Convert_files
   timidity sustain.mid -Ow -o sustain.wav

   https://wiki.archlinux.org/title/List_of_applications#Audio_analyzers
   community/sonic-visualiser
   https://wiki.archlinux.org/title/List_of_applications#Scorewriters
   LilyPond
   https://wiki.archlinux.org/title/List_of_applications#Sound_generators
   https://tldp.org/HOWTO/MIDI-HOWTO-8.html#ss8.2
   FluidSynth
   TiMidity++

   http://linux-sound.org/

   Legal
   https://www.mutopiaproject.org/ - Free Sheet Music for Everyone
   https://imslp.org/wiki/Main_Page - Sharing the world’s public domain music.
   https://musopen.org/sheetmusic/

   Gray
   https://sheetmusic-free.com/
   https://www.free-scores.com/
   https://sheet.host/

   fuck musescore
   https://www.theregister.com/2021/07/20/muse_group_deportation_threat/
   https://news.ycombinator.com/item?id=27005385


Codec/Container
===============

| `MDN <https://developer.mozilla.org>`__
| `Media container formats (file types) guide <https://developer.mozilla.org/docs/Web/Media/Formats/Containers>`__
| `Web video codec guide <https://developer.mozilla.org/docs/Web/Media/Formats/Video_codecs>`__
| `Web audio codec guide <https://developer.mozilla.org/docs/Web/Media/Formats/Audio_codecs>`__


Whishlist
=========

| piano - PvZ day
| piano - PvZ rooftop
| piano - Tokyo Hot


8bit
====

`music.sh <https://tldp.org/LDP/abs/html/devref1.html#MUSICSCR>`__

| :wp:`A440 (pitch standard)`
| :wp:`piano key frequencies`
| http://log.fundamental-code.com/2011/07/31/using-dev-dsp.html
| https://sources.debian.org/src/abs-guide/
| https://tldp.org/LDP/abs/html/devref1.html#MUSICSCR

:manpage:`aplay(1)`

::

   AVG_PRODUCT="$(bc <<<'
      scale=7
      ( \
         23 * 698.4565 + \
         24 * 659.2551 + \
         27 * 587.3295 + \
         30 * 523.2511 + \
         32 * 493.8833 + \
         36 * 440.0000 + \
         41 * 391.9954 + \
         49 * 329.6276 \
      ) / 8
   ')"
   echo
   echo "  $AVG_PRODUCT" # 15913.7351000
   echo; \
   FREQ=( \
      1975.533
      1760.000
      1661.219
      1567.982
      1396.913
      1318.510
      1174.659
      1046.502
      x \
      1046.502 \
      x \
      987.7666 \
      880.0000 \
      783.9909 \
      698.4565 \
      659.2551 \
      587.3295 \
      523.2511 \
      x \
      493.8833 \
      440.0000 \
      391.9954 \
      349.2282 \
      329.6276 \
      293.6648 \
      261.6256 \
   ); \
   for i in ${FREQ[*]}; do \
      if [ "$i" = "x" ]; then \
         echo; \
      else \
         printf "  %.2f - %s\n" \
            "$(bc <<<"scale=7;$AVG_PRODUCT/$i")" \
            "$i"; \
      fi; \
   done; \
   echo


`Lilypond`__
============

.. __: http://lilypond.org/


| `LilyPond <http://lilypond.org/>`__
| \
  :aw:`archwiki <LilyPond>` |vv|
          `Music Glossary     <http://lilypond.org/doc/stable/Documentation/music-glossary/>`__ |vv|
            **Learning Manual**
           (:emlink:`progress <http://lilypond.org/doc/stable/Documentation/learning/working-on-input-files>`) |vv|
          `Notation Reference <http://lilypond.org/doc/stable/Documentation/notation/>`__ |vv|
          `Usage              <http://lilypond.org/doc/stable/Documentation/usage/>`__

:aw:`FluidSynth`

:ltlink:`--no-pause <https://github.com/mpv-player/mpv/issues/4641#issuecomment-320532181>`

::

   for i in 1; do
      R=44100
      F=/tmp/pvz_root_$(uuidgen).wav
      echo
      cd ~/music
      lilypond pvz_roof.ly || break
      echo
      rm -f /tmp/pvz_root_*.wav
      fluidsynth \
         -l \
         -r $R \
         -T wav \
         -o synth.cpu-cores=4 \
         -F $F \
         /usr/share/soundfonts/FluidR3_GM.sf2 \
         pvz_roof.midi \
         || break
      echo
      sync
      mpv --no-pause $F
      # aplay -t wav $F
   done

:wp:`Arpeggio` (cegc'ge)
