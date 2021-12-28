.. include:: include/substitution.txt

============
Cangjie 倉頡
============

雜項 |:hourglass:|
==================

`漢字の正しい書き順(筆順) <https://kakijun.jp/>`__
`國字標準字體筆順學習網 <https://stroke-order.learningweb.moe.edu.tw/characters.do>`__

`glyphwiki <https://glyphwiki.org/>`__ SVG 明朝体の漢字グリフ

gitter - `rime <https://gitter.im/rime/home>`__

開啓無痕式分頁，登入另一google賬號，使用 |:tw:| 區域檢索

`筆順查詢 <https://stroke-order.learningweb.moe.edu.tw/characters.do>`__

| 五代字典
|    `倉頡之友 <http://www.chinesecj.com/>`__ - `倉頡大字典測試版 <http://www.chinesecj.com/cj5dict/>`__
| 三代和五代字典
|    `dict.tw <http://dict.tw/>`__
| 不明代字典
|   `911查询 <https://cangjie.911cha.com/>`__ ( ``毋`` 三代，其他字五代 )
|   `漢文庫典 <http://chidic.eduhk.hk/>`__
| 無倉頡字典
|   `粵典 <https://words.hk/>`__
|   `Pleco CC-Canto <http://cantonese.org/>`__

`hkcards <https://www.hkcards.com/>`__ (拆字)

| `維基教科書 <https://zh.wikibooks.org/wiki/倉頡輸入法>`__
| |b| `取碼字形問題 <https://zh.wikibooks.org/wiki/倉頡輸入法/特別注意#字形問題>`__
| |b| `進階知識 <https://zh.wikibooks.org/wiki/倉頡輸入法/進階知識>`__
      - `標點符號 <https://zh.wikibooks.org/wiki/倉頡輸入法/進階知識#標點符號輸入>`__
| |b| `複合字 <https://zh.wikibooks.org/wiki/倉頡輸入法/例外字#複合字首>`__
| |b| `輔助字形 <https://zh.wikibooks.org/wiki/倉頡輸入法/輔助字形>`__
| |b| `例外字 <https://zh.wikibooks.org/wiki/倉頡輸入法/例外字>`__
| |b| `版本差異#五代與三代的差異 <https://zh.wikibooks.org/wiki/倉頡輸入法/版本差異#五代與三代的差異>`__

`朱邦復工作室 - 著作下載 <http://www.cbflabs.com/?id=5>`__
- 第五代倉頡輸入法手冊
- 下載二（影印版）

.. highlight:: bash

::

   # cat >|/tmp/test.bash <<"EOF"
   # echo "$1"
   # sleep 3
   # EOF
   # printf "%s\n" {0..9} | xargs -I {} -n 1 -P 4 /bin/bash /tmp/test.bash {}
   # rm /tmp/test.bash
   # WARNING:root:Image contains transparency which cannot be retained in PDF.
   # WARNING:root:img2pdf will not perform a lossy operation.
   # WARNING:root:You can remove the alpha channel using imagemagick:
   # WARNING:root:  $ convert input.png -background white -alpha remove -alpha off output.png
   # ERROR:root:error: Refusing to work on images with alpha channel
   cd ~/cangjie && {
      rm -rf 5cjbook
      unzip 5cjbook.zip
      cd ~/cangjie/5cjbook && {
         mkdir -pv ~/cangjie/5cjbook/png
         cd ~/cangjie/5cjbook/gif && {
            echo "converting ... check htop(1)"
            # https://imagemagick.org/script/openmp.php
            ls -A1 | /bin/time --format="\n  wall clock time - %E\n" xargs -I {} -n 1 -P 4 \
               /bin/magick convert {} -limit thread 1 -background white -alpha remove -alpha off ../png/{}.png
         }
         # https://unix.stackexchange.com/questions/172481/how-to-quote-arguments-with-xargs
         cd ~/cangjie/5cjbook/png \
            && ls -A1 | xargs -d$'\n' /bin/img2pdf >~/pdf/5cjbook.pdf \
            && ln -sfv ~/pdf/5cjbook.pdf ~/cgi/cgi-tmp/
      }
   }

`馬來西亞倉頡之友 <http://www.chinesecj.com/forum/forum.php>`__
|vv| `香港倉頡之友 <http://www.cjhk.org/>`__

`香港中文大學 <https://www.fed.cuhk.edu.hk/readwrite/typing/>`__

`HPC教學影片 <https://www.youtube.com/playlist?list=PLDFBC6E544364A540>`__

輔助字形列表

.. highlight:: text

A3 outline ::

   +-------+-------+-------+-------+
   |       |       |       |       |
   |       |       |       |       |
   |034.gif|035.gif|036.gif|037.gif|
   |       |       |       |       |
   |       |       |       |       |
   +-------+-------+-------+-------+
   |       |       |       |       |
   |       |       |       |       |
   |038.gif|039.gif|040.gif|041.gif|
   |       |       |       |       |
   |       |       |       |       |
   +-------+-------+-------+-------+

.. highlight:: bash

`how to improve image output from montage in imagemagick <https://stackoverflow.com/q/34834208>`__
`mode <https://www.imagemagick.org/script/command-line-options.php#mode>`__

::

   # "auxiliary shapes" - https://en.wikipedia.org/wiki/Cangjie_input_method#Keys_and_%22radicals%22
   cd /home/darren/cangjie/5cjbook/gif/ && {
      # magick convert +append {034..037}.gif u.bmp
      # magick convert +append {038..041}.gif l.bmp
      # magick convert -append u.bmp l.bmp auxiliaryshapes_convert.bmp
      # magick montage {034..041}.gif -tile 4x2 -resize $((1240*4))x$((1567*2)) auxiliaryshapes_montage.bmp
      rm -rfv auxiliaryshapes*
      rm -rfv ~/cgi/cgi-tmp/auxiliaryshapes*
      magick montage {034..041}.gif -tile 4x2 -mode Concatenate auxiliaryshapes_full.png
      magick montage 0{34,35,38,39}.gif -tile 2x2 -mode Concatenate auxiliaryshapes_l.png
      magick montage 0{36,37,40,41}.gif -tile 2x2 -mode Concatenate auxiliaryshapes_r.png
      mkdir -v auxiliaryshapes
      mv -v auxiliaryshapes_* auxiliaryshapes/
      cd auxiliaryshapes/
      ls -lh
      zip -r auxiliaryshapes.zip *
      ln -sfv $(realpath *) ~/cgi/cgi-tmp/
   }


字典檔 |:books:|
================

| :zh:`中日韓統一表意文字列表` / :wp:`CJK Unified Ideographs (Unicode block)`
| `unicode-table.com <https://unicode-table.com/en/blocks/cjk-unified-ideographs/>`__
| `The Unicode Standard <https://www.unicode.org/standard/standard.html>`__
  - `Latest Version <http://www.unicode.org/versions/latest/>`__
  - `18 East Asia <https://www.unicode.org/versions/latest/ch18.pdf>`__

| `cangjie5.dict.yaml <https://raw.githubusercontent.com/rime/rime-cangjie/master/cangjie5.dict.yaml>`__
| `cangjie5.txt <https://raw.githubusercontent.com/definite/ibus-table-chinese/master/tables/cangjie/cangjie5.txt>`__
| `倉頡大字典 <https://www.chinesecj.com/cjdict/>`__
| `倉頡平台2012 <https://www.chinesecj.com/forum/forum.php?mod=viewthread&tid=2596>`__ :kbd:`CJSYS-20110919.zip//cjsys/yong/mb/cj5-70000.txt`
| `倉頡平台2022 <https://www.chinesecj.com/forum/forum.php?mod=viewthread&tid=195320>`__

| `倉頡五代補完計劃 <https://github.com/Jackchows/Cangjie5>`__
|    `#184 <https://github.com/Jackchows/Cangjie5/issues/184>`__ - json
|    :download:`Cangjie5_special.txt <https://raw.githubusercontent.com/Jackchows/Cangjie5/master/Cangjie5_special.txt>`
     - `常用字 <https://github.com/Jackchows/Cangjie5/issues/231#issuecomment-962807940>`__
     - ``sha1 f6bd60a4baff8cae2c939bd2aa54dc7e1fad3be3``
|    :download:`Cangjie5.txt <https://raw.githubusercontent.com/Jackchows/Cangjie5/master/Cangjie5.txt>`
     - ``sha1 92f380eae166090ad3397456900b7091813c30a1``
|    :download:`Cangjie5_TC.txt <https://raw.githubusercontent.com/Jackchows/Cangjie5/master/Cangjie5_TC.txt>`


固化 |:file_folder:|
====================

take variable names from :wp:`wp:cangjie input method <cangjie input method>`

:wp:`bson <BSON>`

:file:`~/cangjie/rime_cangjie_dict.sh`

.. highlight:: c

::

   #define RADICALS_PER_KANJI 5

openssl checksum example :file:`~/clash/clash_sip002/main.c` ``EVP_*()``

| :pkg:`community/ibus-table-chinese`
| ``sqlitebrowser /usr/share/ibus-table/tables/cangjie5.db``
|    |rarr| Tables |rarr| phrases
|       ``CREATE TABLE phrases (id INTEGER PRIMARY KEY, tabkeys TEXT, phrase TEXT, freq INTEGER, user_freq INTEGER)``
|       (tabkeys,phrase)

| gdbm sdbm tdb db `libdbh <https://aur.archlinux.org/packages/libdbh2/>`__ (`gnu <https://www.gnu.org/software/libdbh/>`__)
| :wp:`associative array#Permanent_storage`
| :wp:`serialization`
| :wp:`key–value database`
| :wp:`NoSQL#Key–value_store`
| :wp:`DBM (computing)#Implementations`

db key unordered, store keys to a separate fixed array for random picking

| :wp:`Berkeley DB`
| 18.x (AGPL)
|    `downloads <https://www.oracle.com/database/technologies/related/berkeleydb-downloads.html>`__
     :download:`db-18.1.40.tar.gz <https://download.oracle.com/berkeley-db/db-18.1.40.tar.gz>`
|    `tasks <https://docs.oracle.com/database/bdb181/tasks_dev.htm>`__ - Programmatic APIs for C
|    `books <https://docs.oracle.com/database/bdb181/books.htm>`__ - Programmatic APIs - C
|    `books <https://docs.oracle.com/database/bdb181/books.htm>`__ - Getting Started with Data Storage - C |:books:|
| 5.x (?L)
|    :download:`db-5.3.28.tar.gz <https://download.oracle.com/berkeley-db/db-5.3.28.tar.gz>`
     - ``sha1 fa3f8a41ad5101f43d08bc0efb6241c9b6fc1ae9``
|    ``file:///home/darren/cangjie/db-5.3.28/docs/index.html`` - Getting Started with Data Storage - C |:books:|

.. highlight:: text

::

   datum.dptr->

    [0]                [6]                 [12]                 [18]
     a  a  a  a  a  \0  b  b  b  b  \0  \0  c  c  c  \0  \0  \0  d


.. table::
   :align: left
   :widths: auto

   ============================ =========================================
    new                          existing
   ============================ =========================================
    gdbm_store()                 gdbm_store() gdbm_fetch() gdbm_store()
    gdbm_exists() gdbm_store()   gdbm_exists() gdbm_fetch() gdbm_store()
    gdbm_fetch() gdbm_store()    gdbm_fetch() gdbm_store()
   ============================ =========================================

:manpage:`SLIST_ENTRY(3)` -
:manpage:`SLIST_ENTRY(3bsd)` -
singly linked list api


輔助字形練習器
==============

.. tip::

   Use the same build system as the library it depends on (imagemagick)

| svg bezier
| `GeoGebra <https://www.geogebra.org/calculator>`__ Graphing mode
| :menuselection:`Tools --> Slider --> t`
| :menuselection:`Tools --> Point --> P0 P1 P2`

::

   B=(1-t)((1-t)P0+tP1)+t((1-t)P1+tP2)
   loc1=Locus(B,t)

| `<https://stackoverflow.com/questions/1527883/parse-html-using-c>`__
| `pup <https://github.com/ericchiang/pup>`__ |vv|
  `htmlq <https://github.com/mgdm/htmlq>`__ |vv|
  `gumbo-parser <https://github.com/google/gumbo-parser>`__

get html ::

   rm -fv svg.html
   curl -x socks5h://127.0.0.1:1080 'https://zh.wikibooks.org/w/index.php?title=%E5%80%89%E9%A0%A1%E8%BC%B8%E5%85%A5%E6%B3%95%2F%E8%BC%94%E5%8A%A9%E5%AD%97%E5%BD%A2&variant=zh-tw' >|svg.html

extract svg url ::

   # <img ... src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Cjrm-a0.svg/30px-Cjrm-a0.svg.png" ...>
   # https://upload.wikimedia.org/wikipedia/commons/b/ba/Cjem-c2-2.svg
   # https://serverfault.com/a/631000
   cd ~/cangjie/auxiliary_shapes/ && {
      rm -fv paths.txt
      cat svg.html \
         | htmlq 'table:nth-of-type(2)' \
         | htmlq 'td:nth-last-child(3),td:nth-last-child(2)' \
         | htmlq -a src img \
         | cut -d'/' -f7-9 \
         >| paths.txt
      [ "$(wc -l <paths.txt)" -eq "$(sort paths.txt | uniq | wc -l)" ] || echo err
   }

hard-code ::

   # steal tmp.sh

download svg ::

   mkdir -p ~/cangjie/auxiliary_shapes/svg && cd "$_" && (
      printf "total: "
      wc -l ../paths.txt
      rm -I *.svg
      cat ../paths.txt \
         | sed 's,^,https://upload.wikimedia.org/wikipedia/commons/,g' \
         | sponge \
         | parallel --bar -P 10 curl -x socks5h://127.0.0.1:1080 -O --retry-all-errors --retry 99 -s {}
      # make sure no no svg is left out
      comm -3 <(echo "$U" | cut -d/ -f3 | sort) <(ls -1A | sort)
   )

`<https://stackoverflow.com/questions/7540901/scaling-vector-images-through-librsvg>`__

| ``日`` monochrome Cjrm-a0.svg
| ``明`` duotone Cjem-a0-1.svg

`rsvg doc <file:///usr/share/gtk-doc/html/rsvg-2.0/index.html>`__
`[progress] <file:///usr/share/gtk-doc/html/rsvg-2.0/ch03.html>`__

:abbr:`geometric translation (平移)`

::

   make
   make run

\

   Cairo had a notion of "backends": it could render to RGBA buffers, or it could translate its drawing model commands into PDF or PostScript. In Cairo's terms, one creates a cairo_surface_t of a particular kind (in-memory image surface, PDF surface, EPS surface, etc.), and then a cairo_t context for the surface. The context is what makes the drawing commands available.

      | rsvg_handle_get_pixbuf() |rarr|
      | rsvg_handle_render_cairo(handle, cairo_t) |rarr|
      | rsvg_handle_render_document()


Cairo
=====

.. warning::

   | Is is not possible to have cairo paint to framebuffer directly
   | Framebuffer and cairo surface may have different strides

:abbr:`opaque (non-transparent)`
:abbr:`translucent(semitransparent)`
transparent

`CTM <https://www.cairographics.org/manual/cairo-Transformations.html#cairo-Transformations.description>`__

| `docs <https://cairographics.org/documentation/>`__
  |vv| `cookbook <https://cairographics.org/cookbook/>`__
  |vv| `index <https://cairographics.org/manual/index-all.html>`__
| `tutorial <https://cairographics.org/tutorial/>`__ (click images on the right side for source code)

`index <https://cairographics.org/manual/index-all.html>`__

| slow paths
| |b| copy something back from the graphics server, do some operations on the CPU, and then reupload back to the server
| |b| creating too many clipping regions (catch them with *the script surface* or */usr/bin/cairo-trace*)

destination
   | `surface <https://www.cairographics.org/manual/cairo-surfaces.html>`__
   | PixelArray/SVG/PDF/etc.
source
   | |:art:| |:paintbrush:| paint/palette/pattern/`another surface <https://www.cairographics.org/FAQ/#paint_from_a_surface>`__
   | opaque/translucent
mask
   controls where you apply the source to the destination
path
   |:arrow_up_down:| between mask and context
context
   | keeps track of everything that verbs affect
   | source + destination + mask + helpervars ( line width/style font face/size ... ) + path
   | the path it tracks turns into a mask with the next verb-drawing
