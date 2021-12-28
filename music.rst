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

piano stores - :file:`/sphinx.private/places.rst`

| `compressor <https://askubuntu.com/questions/31580/is-there-a-way-of-leveling-compressing-the-sound-system-wide>`__
| :wp:`EQ <equalization (audio)>` - boost bass with :wp:`LPF <low-pass filter>` for recognizing :wp:`accompaniment`


Codec/Container
===============

| `MDN <https://developer.mozilla.org>`__
| `Media container formats (file types) guide <https://developer.mozilla.org/docs/Web/Media/Formats/Containers>`__
| `Web video codec guide <https://developer.mozilla.org/docs/Web/Media/Formats/Video_codecs>`__
| `Web audio codec guide <https://developer.mozilla.org/docs/Web/Media/Formats/Audio_codecs>`__


Whishlist |:memo:|
==================

| piano - PvZ day
| piano - PvZ rooftop
| piano - Tokyo Hot
| `Amelia Watson BGM <https://chordify.net/chords/amelia-watson-s-bgm-piano-kotailri>`__
| :zh:`高嘉瑜`\ x\ :zh:`隱形的翅膀` :yt:`bhZZVmAdpt8` :yt:`hOo3JX93Op8`
| 夢を\ :pr:`かなえて`\ かなえないドラえもん - `YTShorts <https://www.youtube.com/shorts/sqoy5qkxuWE>`__


8bit
====

| `music.sh <https://tldp.org/LDP/abs/html/devref1.html#MUSICSCR>`__

:raw-html:`<details><summary>music.sh - generate parameters for mknote()</summary>`

::

   {
      echo
      FREQ=(
         1975.533
         1760.000
         1661.219
         1567.982
         1396.913
         1318.510
         1174.659
         1046.502
         x
         1046.502
         x
         987.7666
         880.0000
         783.9909
         698.4565
         659.2551
         587.3295
         523.2511
         x
         493.8833
         440.0000
         391.9954
         349.2282
         329.6276
         293.6648
         261.6256
      )
      for i in "${FREQ[@]}"; do
         if [ x"$i" = xx ]; then
            echo
         else
            printf \
               "  %.2f - %s\n" \
               "$(bc <<<"scale=7;16000.0/$i")" \
               "$i"
         fi
      done
      echo
   }

:raw-html:`</details>`

| :wp:`A440 (pitch standard)`
| :wp:`piano key frequencies`
| http://log.fundamental-code.com/2011/07/31/using-dev-dsp.html
| https://sources.debian.org/src/abs-guide/

:manpage:`aplay(1)`


Terms
=====

:wp:`list of musical symbols`

:wp:`Legato` - :wp:`slur <slur (music)>`

:wp:`mode <mode (music)>` - key signature

:wp:`note <note value>`
- :wp:`beam <beam (music)>`
- :wp:`dot <dotted note>`
-      flag
- :wp:`head <notehead>`
-      hook
- :wp:`stem <stem (music)>`
-      tail


`Lilypond`__
============

.. __: http://lilypond.org/

`<https://lilypond.org/doc/v2.22/Documentation/music-glossary/bass-clef>`__
`<https://lilypond.org/doc/v2.22/Documentation/notation/lilypond-index>`__
`<https://lilypond.org/doc/v2.22/Documentation/notation/creating-and-referencing-contexts#index-_005cnew>`__
`<https://lilypond.org/doc/v2.22/Documentation/notation/displaying-pitches#clef>`__
`<https://lilypond.org/doc/v2.22/Documentation/notation/common-notation-for-keyboards>`__
`<https://lilypond.org/doc/v2.22/Documentation/notation/keeping-contexts-alive>`__
`<https://lilypond.org/doc/v2.21/Documentation/learning/staff-groups>`__
`<https://lilypond.org/doc/v2.21/Documentation/notation/common-notation-for-keyboards>`__
`<https://lilypond.org/doc/v2.21/Documentation/notation/keeping-contexts-alive>`__
`<https://lilypond.org/doc/v2.21/Documentation/notation/piano>`__

:aw:`archwiki <LilyPond>`

| `Manuals <http://lilypond.org/doc/stable/Documentation/web/manuals.html>`__
  |vv| `Music Glossary     <http://lilypond.org/doc/stable/Documentation/music-glossary/>`__
  |vv| **Text Input**      `[progress]`__
  |vv| **Learning Manual** `[progress]`__
  |vv| `Notation Reference <http://lilypond.org/doc/stable/Documentation/notation/>`__ \
       (`index <https://lilypond.org/doc/stable/Documentation/notation/lilypond-command-index>`__)
  |vv| ...

.. __: http://lilypond.org/doc/v2.22/Documentation/web/text-input#Pop-music
.. __: http://lilypond.org/doc/v2.22/Documentation/learning/clickable-examples

| `<http://lilypond.org/doc/v2.22/Documentation/usage/troubleshooting>`__
| `<http://lilypond.org/doc/v2.22/Documentation/usage/common-errors>`__
| `<http://lilypond.org/doc/v2.22/Documentation/learning/multiple-notes-at-once>`__
| `<http://lilypond.org/doc/v2.22/Documentation/notation/simultaneous-notes>`__
| `<http://lilypond.org/doc/v2.22/Documentation/learning/real-music-example>`__

:wp:`General MIDI`
- `list of instruments <https://soundprogramming.net/file-formats/general-midi-instrument-list/>`__

:aw:`FluidSynth`

mpv
:ltlink:`--no-pause <https://github.com/mpv-player/mpv/issues/4641#issuecomment-320532181>`
:ltlink:`--no-resume-playback <https://mpv.io/manual/master/#options-no-resume-playback>`

::

   cd ~/music/lilypond
   source ./lilypond.bashrc
   # ly <TAB><TAB>

.. command-output:: file /tmp/un1gfn.github.io/current_sheet.pdf

`current_sheet.pdf </current_sheet.pdf>`__

:wp:`Arpeggio` (cegc'ge)


Piano
=====

Nahre Sol `Repeated Notes at the Piano <https://www.youtube.com/watch?v=3XcgoAl5WvI>`__
