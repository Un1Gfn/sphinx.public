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

| `compressor <https://askubuntu.com/questions/31580/is-there-a-way-of-leveling-compressing-the-sound-system-wide>`__
| :wp:`EQ <equalization (audio)>` - boost bass with :wp:`LPF <low-pass filter>` for recognizing :wp:`accompaniment`

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

`好和弦 <https://nicechord.com/>`__

| 青牛踏蓮.\ :yt:`樂譜行進規則/反覆記號/唱歌路徑 <B_Tvp73FnzA>`
| 青牛踏蓮.\ :yt:`反覆記號/詳解/大彙總 <B_Tvp73FnzA>`

.. list-table::
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - |bar| A |bar|  B |bar|  C |rRep|
     - |bar| A |bar|  B |bar|  C |bar|  A |bar| B |bar| C |fin|
   * - |bar| A |bar|  B |rRep| C |bar|  D |fin|
     - |bar| A |bar|  B |bar|  A |bar|  B |bar| C |bar| D |fin|
   * - |bar| A |lRep| B |bar|  C |rRep| D |fin|
     - |bar| A |bar|  B |bar|  C |bar|  B |bar| C |bar| D |fin|
   * - :sup:`"1" over B,C` |nbsp| :sup:`"2" over D,E` |br| |bar| A |bar| B |bar| C |rRep| D |bar| E |bar| F |fin|
     - |br| |bar| A |bar| B |bar| C |bar| A |bar| D |bar| E |bar| F |fin|


:abbr:`chorus (a part of a song that is repeated after each verse typically by more than one singer)`

:wp:`dal segno`
\- U:`DS <https://www.compart.com/en/unicode/U+1D109>`__
\- U:`S <https://www.compart.com/en/unicode/U+1D10B>`__


Theory
======

:wp:`circle of fifths` - :yt:`O43EBVnwNvo`

.. table::
   :align: left
   :widths: auto

   ==== ====  =========================== ===== =====
    C    B#                                Am    Am
    G    G     :abbr:`p5 (perfect five)`   Fbm   Em
    D    D     maj2                        Cbm   Bm
    A    A     maj6                        Gbm   F#m
    Fb   E     maj3                        Dbm   C#m
    Cb   B     maj7                        Abm   G#m
    Gb   F#    aug4/tritone                Ebm   D#m
    Db   C#    min2                        Bbm   A#m
    Ab   G#    min6                        Fm    E#m
    Eb   D#    min3                        Cm    B#m
    Bb   A#    min7                        Gm    Gm
    F    E#    p4                          Dm    Dm
    C    B#                                Am    Am
   ==== ====  =========================== ===== =====

.. table::
   :align: left
   :widths: auto

   ======= ======= ====================================
    C       Cmaj    0 + p5 + maj3
    Cm      Cmin    0 + p5 + min3
    CM7     Cmaj7   0 + p5 + maj3 + maj7
    Cm7     Cmin7   0 + p5 + min3 + min7
    Em7b5           0 + aug4 + min3 min7
    Csus4           0 + p5 + p4
    Csus2           0 + p5 + maj2
    C6/9            0 + p5 + maj2 + maj6 + maj3
    Cdim            0 + min3 + aug4
    Cdim7           0 + min3 + aug4 + maj6
    Caug            0 + maj3 + min6
   ======= ======= ====================================


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

| :ly:`articulation <notation/list-of-articulations>` /aar·ti·kyuh·**lay**·shn/
| |b| staccato /stuh·**kaa**·tow/


`Lilypond`__
============

.. __: http://lilypond.org/

:ly:`front ends <web/easier-editing>`

| :ly:`music-glossary/clef` - Bass/Alto/Treble

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

::

   source ~/music/ly.misc/lilypond.bashrc
   help2
   file /tmp/un1gfn.github.io/current_sheet.pdf
   qrencode -tUTF8 http://192.168.0.223:20688/current_sheet.pdf

:wp:`Arpeggio` ``c e g c' g e``

`break/jump <https://music.stackexchange.com/questions/12066/how-can-i-typeset-a-break-or-jump-in-my-scores>`__
instead of relying on mpv resume

:ly:`notation/bars.en.html#rehearsal-marks`

2-up ::

   pdfjam 04_ame.ly.pdf --nup 2x1 --suffix 2up --a3paper --landscape --frame true --trim '0mm 0mm 0mm 0mm' --outfile temp.pdf
   # pdfbook2 -p a3paper -s -n 04_ame.ly.pdf
   # pdfbook2 -p a3paper -n 04_ame.ly.pdf

`Extending LilyPond <https://extending-lilypond.readthedocs.io/>`__

random id ::

   ~/music/genid.sh


Piano
=====

Nahre Sol `Repeated Notes at the Piano <https://www.youtube.com/watch?v=3XcgoAl5WvI>`__


Hangul
======

.. note::

   Adjust reST table alignment with ``nvim`` or ``less -S ~/sphinx.public/music.rst``

| :wp:`romanization of Korean`
|    :wp:`MR <McCune–Reischauer>`
|    :wp:`RR <Revised Romanization of Korean#Transcription_rules>` |:crown:|
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

`SEEMILE.韓国語.文字と発音編 <https://www.youtube.com/playlist?list=PLAR6PIbgTNh333_flUM97M7wKeWkdnh7s>`__

| 陽性母音 :kbd:`ㅏ` :kbd:`ㅑ` :kbd:`ㅗ` :kbd:`ㅛ`
| 陰性母音 :kbd:`ㅓ` :kbd:`ㅕ` :kbd:`ㅜ` :kbd:`ㅠ`
| 中性母音 :kbd:`ㅡ` :kbd:`ㅣ`
| 合成母音 :kbd:`ㅐ`\ :sub:`e` :kbd:`ㅒ`\ :sub:`ye`
| 合成母音 :kbd:`ㅔ`\ :sub:`e` :kbd:`ㅖ`\ :sub:`ye`
| 合成母音 :kbd:`ㅘ`\ :sub:`wa` :kbd:`ㅚ`\ :sub:`we` :kbd:`ㅙ`\ :sub:`we` :sub:`(陽性母音+陽性母音)`
| 合成母音 :kbd:`ㅝ`\ :sub:`wǝ` :kbd:`ㅟ`\ :sub:`wi` :kbd:`ㅞ`\ :sub:`we` :sub:`(陰性母音+陰性母音)`
| 合成母音 :kbd:`ㅢ`\ :sub:`wi`

ゼロ子音 :kbd:`ㅇ`

.. list-table::
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - 子音・平音
     - 普通に息を出す
     - :kbd:`ㄱ` :kbd:`ㄴ` :kbd:`ㄷ` :kbd:`ㄹ` :kbd:`ㅁ` :kbd:`ㅂ` :kbd:`ㅅ`\ :sub:`s` :kbd:`ㅇ` :kbd:`ㅈ`\ :sub:`ch` :kbd:`ㅎ`\ |br|\ |br|\ :kbd:`ㄱ` :kbd:`ㄷ` :kbd:`ㅂ` :kbd:`ㅈ`\ :sub:`ts`  :kbd:`ㅅ`\ :sub:`s` :kbd:`ㄴ` :kbd:`ㄹ` :kbd:`ㅁ` :kbd:`ㅇ` :kbd:`ㅎ`
   * - 子音・濃音
     - 息を出さない
     - :kbd:`ㄲ`\ :sub:`っg` :kbd:`ㄸ`\ :sub:`っd` :kbd:`ㅃ`\ :sub:`っb` :kbd:`ㅉ`\ :sub:`っtz` :kbd:`ㅆ`\ :sub:`っs`
   * - 子音・激音
     - 強く息を出す
     - :kbd:`ㅋ`\ :sub:`kh` :kbd:`ㅌ`\ :sub:`th` :kbd:`ㅍ`\ :sub:`ph` :kbd:`ㅊ`\ :sub:`tsh`

:wp:`name <hangul consonant and vowel tables#Consonants>`
.
:wp:`order <hangul consonant and vowel tables#Collation>`

.. table::
   :align: left
   :widths: auto

   ==== ======================= ==== =========================
    1    :kbd:`ㄱ` |nbsp| 기역   2    :kbd:`ㄲ` |nbsp| 쌍기역   
    3    :kbd:`ㄴ` |nbsp| 니은
    4    :kbd:`ㄷ` |nbsp| 디귿   5    :kbd:`ㄸ` |nbsp| 쌍디귿   
    6    :kbd:`ㄹ` |nbsp| 리을
    7    :kbd:`ㅁ` |nbsp| 미음
    8    :kbd:`ㅂ` |nbsp| 비읍   9    :kbd:`ㅃ` |nbsp| 쌍비읍   
    10   :kbd:`ㅅ` |nbsp| 시옷   11   :kbd:`ㅆ` |nbsp| 쌍시옷
    12   :kbd:`ㅇ` |nbsp| 이응
    13   :kbd:`ㅈ` |nbsp| 지읏   14   :kbd:`ㅉ` |nbsp| 쌍지읒
    15   :kbd:`ㅊ` |nbsp| 치읓
    16   :kbd:`ㅋ` |nbsp| 키읔
    17   :kbd:`ㅌ` |nbsp| 티읕
    18   :kbd:`ㅍ` |nbsp| 피읖
    19   :kbd:`ㅎ` |nbsp| 히읗
   ==== ======================= ==== =========================

| :wp:`Template:Hangul jamo`
| `틀:한글 낱자 <https://ko.wikipedia.org/wiki/%ED%8B%80:%ED%95%9C%EA%B8%80_%EB%82%B1%EC%9E%90>`__

.. list-table::
   :align: left
   :header-rows: 1
   :stub-columns: 0
   :widths: auto

   * - パッチム・終音
     - 発音
   * - :kbd:`ㄱ` :kbd:`ㅋ` :kbd:`ㄲ` :kbd:`ㄳ` :kbd:`ㄺ`
     - ㄱ
   * - :kbd:`ㄴ` :kbd:`ㄵ` :kbd:`ㄶ`
     - ㄴ
   * - :kbd:`ㄷ` :kbd:`ㅌ` :kbd:`ㅈ` :kbd:`ㅊ` :kbd:`ㅅ` :kbd:`ㅆ` :kbd:`ㅎ`
     - ㄷ
   * - :kbd:`ㄹ` :kbd:`ㄺ` :kbd:`ㄼ` :kbd:`ㄽ` :kbd:`ㄾ` :kbd:`ㅀ`
     - ㄹ
   * - :kbd:`ㅁ` :kbd:`ㄻ`
     - ㅁ
   * - :kbd:`ㅂ` :kbd:`ㅍ` :kbd:`ㄼ` :kbd:`ㄿ`
     - ㅂ
   * - :kbd:`ㅇ`
     - ㅇ

6/8

.. list-table::
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - パッチム + :kbd:`ㅇ`
     - 連音化
     - 만엔 |rarr| 마넨
   * - 二重パッチム + :kbd:`ㅇ`
     - 右のパッチムが連音化
     - 앉아요 |rarr| 안자요
   * - :kbd:`ㄲ`/:kbd:`ㅆ` + :kbd:`ㅇ`
     - まるごと連音化
     - 있어요 |rarr| 이써요
   * - :kbd:`ㅎ` + :kbd:`ㅇ`
     - 連音化せず脱落
     - 좋아요 |rarr| 조아요
   * - :kbd:`ㅇ` + :kbd:`ㅇ`
     - 鼻から息を抜きながら発音
     - 영어 yǝng ǝ |rarr| yǝ ngǝ
   * - :kbd:`ㄴ` + :kbd:`ㄹ`
     - 流音化
     - 편리 |rarr| 펼리
   * - :kbd:`ㄹ` + :kbd:`ㄴ`
     - 流音化
     - 일년 |rarr| 일련

7/8

.. list-table::
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - :kbd:`ㅎ` + :kbd:`ㅇ` |br| |br| :kbd:`ㄶ` + :kbd:`ㅇ` |rarr| :kbd:`ㄴ` |br| |br| :kbd:`ㅀ` + :kbd:`ㅇ` |rarr| :kbd:`ㄹ`
     - 無音化
     - 넣어요 |rarr| 너어요 |br| |br| 싫어요 |rarr| 시러요
   * - :kbd:`ㄴ` + :kbd:`ㅎ` |rarr| :kbd:`ㄴ` |br| :kbd:`ㄹ` + :kbd:`ㅎ` |rarr| :kbd:`ㄹ` |br| :kbd:`ㅁ` + :kbd:`ㅎ` |rarr| :kbd:`ㅁ` |br| :kbd:`ㅇ` + :kbd:`ㅎ` |rarr| :kbd:`ㅇ`
     - 弱音化
     -  전화 |rarr| 저놔  |br| |br| 결혼 |rarr| 겨론
   * - :kbd:`ㄱ` + :kbd:`ㅎ` |rarr| :kbd:`ㅋ` |br| :kbd:`ㅎ` + :kbd:`ㄱ` |rarr| :kbd:`ㅋ` |br| |br| :kbd:`ㄷ` + :kbd:`ㅎ` |rarr| :kbd:`ㅌ` |br| :kbd:`ㅎ` + :kbd:`ㄷ` |rarr| :kbd:`ㅌ` |br| |br| :kbd:`ㅂ` + :kbd:`ㅎ` |rarr| :kbd:`ㅍ` |br| :kbd:`ㅎ` + :kbd:`ㅂ` |rarr| :kbd:`ㅍ` |br| |br| :kbd:`ㅈ` + :kbd:`ㅎ` |rarr| :kbd:`ㅊ` |br| :kbd:`ㅎ` + :kbd:`ㅈ` |rarr| :kbd:`ㅊ`
     - 激音化
     - 육회 |rarr| 유쾨 |br| |br| 입학 |rarr| 이팍 |br| |br| 좋다 |rarr| 조타

8/8

.. list-table::
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - :kbd:`ㄱ` + :kbd:`ㄴ` |rarr| :kbd:`ㅇ` + :kbd:`ㄴ` |br| :kbd:`ㄱ` + :kbd:`ㅁ` |rarr| :kbd:`ㅇ` + :kbd:`ㅁ` |br| |br| :kbd:`ㄷ` + :kbd:`ㄴ` |rarr| :kbd:`ㄴ` + :kbd:`ㄴ` |br| :kbd:`ㄷ` + :kbd:`ㅁ` |rarr| :kbd:`ㄴ` + :kbd:`ㅁ` |br| |br| :kbd:`ㅂ` + :kbd:`ㄴ` |rarr| :kbd:`ㅁ` + :kbd:`ㄴ` |br| :kbd:`ㅂ` + :kbd:`ㅁ` |rarr| :kbd:`ㅁ` + :kbd:`ㅁ`
     - 鼻音化
     - 한국말 |rarr| 한궁말 |br| |br| 십만 |rarr| 심만 |br| |br| 옛날 |rarr| 옌날
   * - :kbd:`ㅁ` + :kbd:`ㄹ` |rarr| :kbd:`ㅁ` + :kbd:`ㄴ` |br| :kbd:`ㅇ` + :kbd:`ㄹ` |rarr| :kbd:`ㅇ` + :kbd:`ㄴ`
     - 鼻音化
     - 음료수 |rarr| 음뇨수 |br| |br| 종로 |rarr| 종노
   * - :kbd:`ㄱ` + :kbd:`ㄱ` |rarr| :kbd:`ㄱ` + :kbd:`ㄲ` |br| :kbd:`ㄷ` + :kbd:`ㄱ` |rarr| :kbd:`ㄷ` + :kbd:`ㄲ` |br| :kbd:`ㅂ` + :kbd:`ㄱ` |rarr| :kbd:`ㅂ` + :kbd:`ㄲ` |br| |br| |br| :kbd:`ㄱ` + :kbd:`ㄷ` |rarr| :kbd:`ㄱ` + :kbd:`ㄸ` |br| :kbd:`ㄷ` + :kbd:`ㄷ` |rarr| :kbd:`ㄷ` + :kbd:`ㄸ` |br| :kbd:`ㅂ` + :kbd:`ㄷ` |rarr| :kbd:`ㅂ` + :kbd:`ㄸ` |br| |br| |br| :kbd:`ㄱ` + :kbd:`ㅂ` |rarr| :kbd:`ㄱ` + :kbd:`ㅃ` |br| :kbd:`ㄷ` + :kbd:`ㅂ` |rarr| :kbd:`ㄷ` + :kbd:`ㅃ` |br| :kbd:`ㅂ` + :kbd:`ㅂ` |rarr| :kbd:`ㅂ` + :kbd:`ㅃ` |br| |br| |br| :kbd:`ㄱ` + :kbd:`ㅅ` |rarr| :kbd:`ㄱ` + :kbd:`ㅆ` |br| :kbd:`ㄷ` + :kbd:`ㅅ` |rarr| :kbd:`ㄷ` + :kbd:`ㅆ` |br| :kbd:`ㅂ` + :kbd:`ㅅ` |rarr| :kbd:`ㅂ` + :kbd:`ㅆ` |br| |br| |br| :kbd:`ㄱ` + :kbd:`ㅈ` |rarr| :kbd:`ㄱ` + :kbd:`ㅉ` |br| :kbd:`ㄷ` + :kbd:`ㅈ` |rarr| :kbd:`ㄷ` + :kbd:`ㅉ` |br| :kbd:`ㅂ` + :kbd:`ㅈ` |rarr| :kbd:`ㅂ` + :kbd:`ㅉ` |br| |br|
     - 農音化
     - 학생 |rarr| 학쌩 |br| |br| 맥주 |rarr| 맥쭈 |br| |br| 잡지 |rarr| 잡찌
   * - :kbd:`ㄷ` + :kbd:`이` |rarr| :kbd:`지` |br| |br| :kbd:`ㅌ` + :kbd:`이` |rarr| :kbd:`지`
     - 口蓋音化
     - 맏이 |rarr| 마지 |br| |br| 같이 |rarr| 가지

|:tada:| |:tada:| |:tada:|

