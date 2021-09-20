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


Lyrics
======

.. highlight:: text

`Ievan Polkka - Loituma`
\| YouTube <https://www.youtube.com/watch?v=7yh9i0PAjck>`__
\| `genius <https://genius.com/Loituma-ievan-polkka-lyrics>`__

::

   0 min 10.5 s

   [Verse 1]
   Nuapurista kuulu-se polokan tahti jalakani pohjii kutku_ _tti
   Ievan äiti-se tyttöösä vahti-vaan kyllähän Ieva-sen jutku_ _tti-Sillä
   ei-meitä silloin kiellot haittaa
   Kun-myö tanssimme laiasta laitaan

   [Refrain]
   Salivili hipput tupput täppy_ _t-äppyt tipput hilija_ _lleen [1]

   [Verse 2]
   Ievan suu-oli vehnä_ _sellä-ko immeise_ _t-onnee toevotti
   Peä-oli märkänä jokai_ _sella-ja viulu-se vinku-ja voevotti (si)
   Ei-tätä poikoo märkyy_ _s-haittaa
   Sillon-ko laskoo laiasta laitaan

   [Refrain]
   Salivili hipput tupput täppy t-äppyt tipput hilija_ _lleen [1]

   [Verse 3]
   Ievan äiti se kammarissa virsiä veisata huijjuutti
   Kun tämä poika naapurissa ämmän tyttöä nuijjuutti
   Eikä tätä poikoo ämmät haittaa
   Sillon ko laskoo laiasta laitaan

   [Refrain]
   Salivili hipput tupput täppyt äppyt tipput hilijalleen
   [Bridge]
   Hilipati hilipati hilipati hillaa
   Hilipati hilipati hilipampaa
   Jalituli jallaa talituli jallaa
   Tilitali tilitali tilitantaa
   Hilipati hillaa hilipati hillaa
   Hilipati hilipati jalituli jallaa
   Tilitali tallaa, tulituli jallaa
   Hilipati hilipati hilipampaa
   Rimpatirillaa ripirapirullaa
   Rumpatirumpa tiripirampuu
   Jamparingaa rimpatiraparan
   Tsupantupiran dillandu
   Japat stilla dipudupu dullaa
   Dumpatidupa lipans dullaa
   Dipidapi dullaa rimpati rukan
   Ribitit stukan dillandu
   Jatsatsa barillas dilla lapadeian dullan deian doo
   Joparimba badabadeia stulla
   Laba daba daba dujan dillandu
   Barillas dilla deiaduu badaba daga daga daga daga dujaduu
   Badu dubi dubi dubi dejaduu
   Badaba dillas dillan dejaduu

   [Verse 4]
   Siellä oli lystiä soiton jäläkeen sain minä kerran sytkyyttee
   Kottiin ko mäntii ni ämmä se riitelj ja Ieva jo alako nyyhkyytteek
   Minä sanon Ievalle mitäpä se haittaa
   Laskemma vielähi laiasta laitaa
   [Refrain]
   Salivili hipput tupput täppyt äppyt tipput hilijalleen

   [Verse 5]
   Muorille sanon jotta tukkee suusi en ruppee sun terveyttäs takkoomaa
   Terveenä peäset ku korjoot luusi ja määt siitä murjuus makkoomaa
   Ei tätä poikoo hellyys haittaa
   Ko akkoja huhkii laiasta laitaan

   [Refrain]
   Salivili hipput tupput täppyt äppyt tipput hilijalleen

   [Verse 6]
   Sen minä sanon jotta purra pittää ei mua niin voan nielasta
   Suat männä ite vaikka lännestä ittään vaan minä en luovu Ievasta
   Sillä ei tätä poikoo kainous haittaa
   Sillon ko tanssii laiasta laitaan

   [Refrain]
   Salivili hipput tupput täppyt äppyt tipput hilijalleen