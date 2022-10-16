.. include:: include/substitution.txt

.. highlight:: text

======================
Music |:musical_note:|
======================

Misc
====

emoji
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

.. tip::

   Grab text from :file:`~/Music/{music.bashrc,readme.md}`

| mit/`music21 <http://web.mit.edu/music21/>`__ (:pkg:`AUR/python-music21`)
| python+abc+lilypond

| :aw:`timidity++#Convert_files`
| ``timidity sustain.mid -Ow -o sustain.wav``

| tldp/`MIDI howto <https://tldp.org/HOWTO/MIDI-HOWTO-8.html#ss8.2>`__
| `Sound & MIDI Software For Linux <http://linux-sound.org/>`__

| Legal
|    `mutopia project - free sheet music for everyone <https://www.mutopiaproject.org/>`__
|    `Sharing the world’s public domain music. <https://imslp.org/wiki/Main_Page>`__
|    :ly:`web/productions`
| Gray
|    `<https://sheetmusic-free.com/>`__
|    `<https://www.free-scores.com/>`__
|    `<https://sheet.host/>`__

piano stores @ sphinx.private/places.rst

| `compressor <https://askubuntu.com/questions/31580/is-there-a-way-of-leveling-compressing-the-sound-system-wide>`__
| :wp:`EQ <equalization (audio)>` - boost bass with :wp:`LPF <low-pass filter>` for recognizing :wp:`accompaniment`

:wp:`circle of fifths` - :yt:`O43EBVnwNvo`

| :aw:`list of applications#Audio_analyzers`
| :aw:`list of applications#Scorewriters`
| :aw:`list of applications#Sound_generators`

:wp:`Audacity`

:wp:`MIDI`


| sound fonts
| :pkg:`community/freepats-general-midi`
| :pkg:`community/soundfont-fluid`
| :pkg:`AUR/soundfont-unison`
| :pkg:`AUR/soundfont-generaluser` (`demo <http://www.schristiancollins.com/generaluser.php>`__)
| :pkg:`AUR/soundfont-arachno`
| :pkg:`AUR/fluidplug-git`


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


Whishlist |:memo:|
==================

| pvz (synthesia)
| :yt:`all bgm <RkRzTF3K9-Q>`
| graze the roof
  |vv| :yt:`complex <gSwkElCgfz4>`
  |vv| :yt:`piano <BiJMBstqIZ8>`

| `Amelia Watson bgm <https://chordify.net/chords/amelia-watson-s-bgm-piano-kotailri>`__
| `Yukihana Lamy bgm <_eXR6gXx4KE>`__

夢を\ :pr:`かなえて`\ かなえないドラえもん - :yt:`小尾巴 <sqoy5qkxuWE>`

harry potter main theme
|vv| :yt:`glockenspiel <iZjJbHUTXbc>`
|vv| :yt:`piano <jTPXwbDtIpA>`

jojo - il vento d'oro
|vv| :yt:`synthesia <OMQYhCtaK-s>`
|vv| :yt:`pan piano <Yjznza9B3rA>`

:yt:`ビンクスの酒 <e9eN_hhFtVw>`

:yt:`boogie woogie <6_2UHz8OsJI>`


Sonic Visualiser
================

:wp:`wikipedia <Sonic Visualiser>`
\- `official site org <https://www.sonicvisualiser.org/>`__
\- `official site uk  <https://code.soundsoftware.ac.uk/projects/sonic-visualiser/>`__
\- `github <https://github.com/sonic-visualiser/sonic-visualiser>`__

Melodic Range Spectrogram

Peak Frequency Spectrogram

| `<https://www.sonicvisualiser.org/videos.html>`__
| `<https://vimeo.com/qmlivemusiclab>`__
| `<https://charm.rhul.ac.uk/analysing/p9_1.html>`__
| `<https://www.izotope.com/en/learn/understanding-spectrograms.html>`__


Codec/Container
===============

| `MDN <https://developer.mozilla.org>`__
| `Media container formats (file types) guide <https://developer.mozilla.org/docs/Web/Media/Formats/Containers>`__
| `Web video codec guide <https://developer.mozilla.org/docs/Web/Media/Formats/Video_codecs>`__
| `Web audio codec guide <https://developer.mozilla.org/docs/Web/Media/Formats/Audio_codecs>`__


Terms
=====

:wp:`list of musical symbols`

:wp:`legato`/:wp:`slur <slur (music)>`

:wp:`mode <mode (music)>` - key signature

| :wp:`note <note value>`
|    :wp:`beam <beam (music)>`
     - :wp:`dot <dotted note>`
     -      flag
     - :wp:`head <notehead>`
     -      hook
     - :wp:`stem <stem (music)>`
     -      tail

:ly:`staff  <music-glossary/staff>` *pl.* staves |rarr| :ly:`system <music-glossary/system>`

::

   background mpv --fs --pause --vo=gpu --hwdec=vaapi --keep-open=yes "/home/darren/music/Amelia Watson's BGM - Piano [DSgaKAChGQg].mp4"

| :ly:`articulation <notation/list-of-articulations>` /aar·ti·kyuh·**lay**·shn/
| |b| staccato /stuh·**kaa**·tow/


`Lilypond`__
============

.. __: http://lilypond.org/

:ly:`front ends <web/easier-editing>`

| :ly:`music-glossary/bass-clef`

| :ly:`learning/multiple-notes-at-once`
| :ly:`learning/real-music-example`
| :ly:`learning/staff-groups`
| :ly:`fingering <learning/within_002dstaff-objects#fingering>`

| :ly:`usage/common-errors`
| :ly:`usage/troubleshooting`

| :ly:`notation/common-notation-for-keyboards`
| :ly:`notation/creating-and-referencing-contexts#index-_005cnew`
| :ly:`notation/creating-midi-output`
| :ly:`notation/displaying-pitches#clef`
| :ly:`notation/keeping-contexts-alive`
| :ly:`notation/keeping-contexts-alive`
| :ly:`notation/lilypond-index`
| :ly:`notation/piano#piano-pedals`
| :ly:`notation/piano`
| :ly:`notation/simultaneous-notes`
| :ly:`notation/displaying-chords`
| :ly:`notation/chord-name-chart`

:aw:`archwiki <LilyPond>`

| :ly:`manuals <web/manuals.html>`
  |vv| :ly:`music glossary <music-glossary>`
  |vv| **Text Input**      `[progress]`__
  |vv| **Learning Manual** `[progress]`__
  |vv| :ly:`notation reference <notation>`
       (`index <https://lilypond.org/doc/stable/Documentation/notation/lilypond-command-index>`__)
  |vv| ...

.. __: http://lilypond.org/doc/v2.22/Documentation/web/text-input#Pop-music
.. __: http://lilypond.org/doc/v2.22/Documentation/learning/clickable-examples

:wp:`General MIDI`
- `list of instruments <https://soundprogramming.net/file-formats/general-midi-instrument-list/>`__

:aw:`FluidSynth`

mpv
:ltlink:`--no-pause <https://github.com/mpv-player/mpv/issues/4641#issuecomment-320532181>`
:ltlink:`--no-resume-playback <https://mpv.io/manual/master/#options-no-resume-playback>`

.. code:: shell

   source ~/music/lilypond/lilypond.bashrc
   help2

.. command-output:: file /tmp/un1gfn.github.io/current_sheet.pdf

.. command-output:: qrencode -tUTF8 http://192.168.0.223:20688/current_sheet.pdf

:wp:`Arpeggio` ``c e g c' g e``

`break/jump <https://music.stackexchange.com/questions/12066/how-can-i-typeset-a-break-or-jump-in-my-scores>`__
instead of relying on mpv resume

2-up ::

   pdfjam 04_ame.ly.pdf --nup 2x1 --suffix 2up --a3paper --landscape --frame true --trim '0mm 0mm 0mm 0mm' --outfile temp.pdf
   # pdfbook2 -p a3paper -s -n 04_ame.ly.pdf
   # pdfbook2 -p a3paper -n 04_ame.ly.pdf


Piano
=====

Nahre Sol `Repeated Notes at the Piano <https://www.youtube.com/watch?v=3XcgoAl5WvI>`__


Hangul
======

| :wp:`outline of Korean language`
|    :wp:`Korean language#Phonology`
|    :wp:`Korean phonology`

| phonetics |vv| syllable
|    :wp:`origin of Hangul`
|    :wp:`Hangul consonant and vowel tables`
|    :wp:`Korean language#Symbol_chart`
|    :wp:`List of Hangul jamo`

| :wp:`romanization of Korean`
|    :wp:`MR <McCune–Reischauer>`
|    :wp:`RR <Revised Romanization of Korean#Transcription_rules>` |:thumbup:|
|    :wp:`YR <Yale romanization of Korean>`

| :wp:`KS X 1001` |vv| :wp:`UHC <Unified Hangul Code>`/MS949/CP949 |vv| :wp:`IBM-949 <code page 949 (IBM)>`
| :wp:`Hangul#Unicode`

| :wp:`BMP <plane (Unicode)#Basic_Multilingual_Plane>` / :wp:`Hangul Syllables`
| :wp:`Korean language and computers#Hangul_syllables_block`
| ``[(initial) × 588 + (medial) × 28 + (final)] + 44032``

| `SampleRz <https://princessoftea.wordpress.com/2012/07/30/why-%EC%9A%B4%EB%AA%85-fate-lyrics-full-house-ost-hangeul-romanization-translation/>`__
  |larr| `운명/이경섭 <https://music.bugs.co.kr/track/80383075>`__
| `SampleRz <https://genius.com/Genius-romanizations-shaun-way-back-home-romanized-lyrics>`__
  |larr| `way back home/숀 (SHAUN) <https://music.bugs.co.kr/track/5262784>`__
  |larr| `google <https://www.google.com/search?as_q=way+back+home+가사&as_epq=&as_eq=&as_filetype=&as_nhi=&as_nlo=&as_occt=any&as_oq=&as_qdr=all&as_sitesearch=&cr=countryKR&lr=lang_ko&safe=images&tbs=>`__
| `새 <https://music.bugs.co.kr/track/61962>`__

::

   멈 CVC m_eo_m     ㅁㅓㅁ
   춘 CVC ch(j)_u_n  ㅊㅜㄴ
   .
   시 CV  s_i        ㅅㅣ
   간 CVC g_a_n      ㄱㅏㄴ
   .
   속 CVC s_o_k      ㅅㅗㄱ

   Meom-chun si-gan sok

::

   사 CV  s_a      ㅅㅏ
   랑 CVC r_a_ng   ㄹㅏㅇ
   을 CVC ._eu_l   ㅇㅡㄹ
   .
   잘 CVC j_a_l    ㅈㅏㄹ
   .
   모 CV  m_o      ㅁㅗ
   르 CV  r_eu     ㄹㅡ
   겠 CVC g_e_t    ㄱㅔㅆ
   어 CV  ss(.)_eo ㅇㅓ

   Sa-rang-eul jal mo-reu-get-sseo
