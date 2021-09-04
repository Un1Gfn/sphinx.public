.. include:: include/substitution.txt

==========
Cheatsheet
==========

Bash
====

WIP move everything from :file:`~/cheatsheet.sh`

`sysfs <https://www.kernel.org/doc/html/latest/filesystems/sysfs.html>`__ kernal doc - :manpage:`sysfs(5)`

assertion or error handling

.. code:: bash

   # trap 'echo "SIGINT"; exit 0' SIGINT
   [ ] || { notify-send "${BASH_SOURCE[0]}" "${FUNCNAME[0]}${LF}line ${BASH_LINENO[0]}"; return 1; }
   [ ] || { echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; return 1; }
   [ ] || { echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; exit 1; }
   # ${BASH_COMMAND}

.. code:: bash

   [ ] || @ABRTEXIT@
   [ ] || @ABRTRET@
   ABRTEXIT='{ echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; return 1; }'
   ABRTRET='{ echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; exit 1; }'
   TMP="$(mktemp /tmp/mktemp-XXX.sh)"
   sed \
      -e "s/@ABRTEXIT@/$ABRTEXIT/g" \
      -e "s/@ABRTRET@/$ABRTRET/g" \
      SCRIPT.sh \
      > "$TMP"
   printf "\e[32m%s\e[0m\n" "running $TMP ..."
   bash "$TMP"

when you have no choice but to pass executable as ``$1``

.. code:: shell-session

   $ /usr/lib/ld-linux-x86-64.so.2 "$(which uname)" -r
   Linux

change terminal emulator title

.. code:: bash

   printf "\033]0;TITLE\007"

horizontal separator ruler / transition line / <hr>

.. code:: bash

   for _ in $(seq 1 "$(tput cols)"); do
     echo -n '-'
   done
   echo
   unset -v _

| :manpage:`console_codes(4)`
| |:red_circle:|
| :file:`printf "\\n\\e[31m%s\\e[0m\\n\\n" "  err"`
| |:green_circle:|
| :file:`printf "\\n\\e[32m%s\\e[0m\\n\\n" "  ok"`
| |:brown_circle:|
| :file:`printf "\\n\\e[33m%s\\e[0m\\n\\n" "  warning"`
| |:blue_circle:|
| :file:`printf "\\n\\e[34m%s\\e[0m\\n\\n" "  info"`

zip archive mojibake

.. code:: bash

   unzip -O sjis SHIFTJIS.ZIP
   unzip -O cp936 GBK.ZIP

`fd abuse HTTP <https://unix.stackexchange.com/q/436200#comment788048_436200>`__ ::

   { \
      echo -e "GET / HTTP/1.0\r\nHost: www.example.com\r\n\r" >&3; \
      cat <&3 ; \
   } 3<> /dev/tcp/www.example.org/80

:aw:`fd abuse tcping <NFS#Automatic_mount_handling>` ::

   if timeout 1 bash -c ": < /dev/tcp/${SERVER}/80"; then
      printf "\n\e[32m  %s\e[0m\n\n" "reached"
   else
      printf "\n\e[31m  %s\e[0m\n\n" "timeout"
   fi

`process tree better than pstree <https://unix.stackexchange.com/a/436579>`__ ::

   ps -aef --forest | less -SRM +%

reverse video time stamp ::

   printf "\n\e[7m  %s  \e[0m\n\n" "$(date)"

`kernel module parameters <https://askubuntu.com/q/59135>`__ ::

   modinfo nfsd \
     | grep '^parm:' \
     | cut -d' ' -f12- \
     | sed -E -e 's/^([^:]+):(.+)$/\1:\n  \2\n/g' \
     | less -F +X -S

::

   modinfo -p nfs \
     | sed -E -e 's/^([^:]+):(.+)$/\1:\n  \2\n/g' \
     | less -F +X -S

`How to read the whole shell script before executing it? <https://unix.stackexchange.com/q/331837/>`__

.. code:: bash

   #!/bin/bash
   function main {
      foo
      bar
   }
   main "$@"; exit

.. code:: bash

   #!/bin/bash
   {
      foo
      bar
   }; exit

test symbolic link

.. code:: bash

   echo
   cd /tmp
   rm -rf /tmp/x
   mkdir $_
   cd $_
   mkdir dir
   ln -sv "dir" lnk
   function test2 {
      printf -- "%5s " "$1"
      for o in -d -e -f -L; do
         if [ "$o" "$1" ]; then
            printf -- "$o true  ";
         else
            printf -- "$o false ";
         fi
      done
      echo
   }
   test2 dir
   test2 lnk
   echo
   rmdir -v dir
   test2 lnk
   echo

.. table::
   :align: left
   :widths: auto

   ================================= ================== ================== ================== ==================
    type                              -d                 -e                 -f                 -L
   ================================= ================== ================== ================== ==================
    \
    file                              |:red_circle:|     |:green_circle:|   |:green_circle:|   |:red_circle:|
    dir                               |:green_circle:|   |:green_circle:|   |:red_circle:|     |:red_circle:|
    \
    symlink2file                      |:red_circle:|     |:green_circle:|   |:green_circle:|   |:green_circle:|
    symlink2dir                       |:green_circle:|   |:green_circle:|   |:red_circle:|     |:green_circle:|
    \
    deadlink2file |br| deadlink2dir   |:red_circle:|     |:red_circle:|     |:red_circle:|     |:green_circle:|
    \
    nonexist                          |:red_circle:|     |:red_circle:|     |:red_circle:|     |:red_circle:|
   ================================= ================== ================== ================== ==================


C
===

WIP move everything from :file:`~/cheatsheet.c`

:wp:`C11 extensions <C11_(C_standard_revision)#Changes_from_C99>`

`cdecl: C gibberish ↔ English <https://cdecl.org/>`__

| `Sparse, Smatch, and Coccinelle <https://thenewstack.io/checking-linuxs-code-with-static-analysis-tools/>`__\ [#]_
| |b| :wp:`Coccinelle_(software)`
| gcc `-fanalyzer <https://developers.redhat.com/blog/2020/03/26/static-analysis-in-gcc-10>`__
| `splint <https://github.com/splintchecker/splint>`__

compile flags

.. code:: text

   -std=gnu11 -g -O0 -Wextra -Wall -Winline -Wshadow -fanalyzer

stringify macro

.. code:: C

   #define STR0(x) #x
   #define STR(x) STR0(x)

range-based for loop macro

.. code:: C

   #define for_range_int(var,range) for(size_t var=0;var<sizeof(range)/sizeof(int);++var)
   int arr[]={19,89,6,4}
   for_range_int(i,arr){
      printf("%d ",arr[i]);
   }
   puts("");

instant linked list

.. code:: C

   typedef struct _Node{
     int ele;
     struct _Node *next;
   } Node;
   #define M malloc(sizeof(Node))
   Node *root=M;
   *(*(*(*
     root=(Node){1,M}
   ).next=(Node){2,M}
   ).next=(Node){3,M}
   ).next=(Node){4,M};

eprintf macro

.. code:: C

   #define eprintf(...) fprintf(stderr,__VA_ARGS__)

lambda macro

.. code:: C

   
   #define LAMBDA(X) ({ X f;})
   g_array_sort(edges,LAMBDA(gint f(const void *x,const void *y){
     return ((Edge*)x)->weight - ((Edge*)y)->weight ;
   }));


Git
===

convert shallow clone to full

.. code:: bash

   git clone --depth=1 https://github.com/libgit2/libgit2
   cd libgit2
   git fetch --unshallow

`drop changes from staging area <https://stackoverflow.com/q/66465810#comment121377736_66470532>`__

.. code:: bash

   git restore -SW -- FILE


ImageMagick
===========

misc (please split this blob)

.. code:: bash

   #!/dev/null

   convert -size 4096x2048 xc:#0000AA Blue.png

   convert -size 4096x4096 -background 'rgb(0,0,170)' Emblem_of_the_Kuomintang.svg Emblem_of_the_Kuomintang.png
   convert -size 1024x1024 -background 'rgb(0,0,170)' -blur 0x64 Emblem_of_the_Kuomintang.svg Emblem_of_the_Kuomintang.blurred.png

   cd /tmp
   convert -size 1024x1024 -background 'rgb(255,255,255)' Network-e72c038278.svg Network-e72c038278.png
   convert -size 1024x1024 -background 'rgb(255,255,255)' Network-8f37df9f10.svg Network-8f37df9f10.png

   rm -fv Emblem_of_Okinawa_County*
   P="Emblem_of_Okinawa_Prefecture"
   C1="Emblem_of_Okinawa_County1"
   C2="Emblem_of_Okinawa_County2"
   cat "$T.svg" \
     | sed -e "s/fill:#ffffff/fill:#0000AA/g" \
     | sed -e "s/fill:#c90037/fill:#ffffff/g" \
     > "$C1.svg"
   cat "$T.svg" \
     | sed -e "s/fill:#c90037/fill:#0000AA/g" \
     > "$C2.svg"
   convert -size 2048x2048 -background 'rgb(  0,  0,170)' "$C1.svg" "$C1.png"
   convert -size 2048x2048 -background 'rgb(255,255,255)' "$C2.svg" "$C2.png"

   Hsiao-Feng_Yin
   Hiu-Fung_Wan ♂️ ♂
   尹曉風 ♂️ ♂
   尹曉風 ♂️
   1949年17歲 生日1932-02-18
   https://home.gamer.com.tw/creationDetail.php?sn=3670959
   https://truth.bahamut.com.tw/s01/201708/8148c7ea0e4fd05a31d1b39875709bf5.JPG?w=1000
   convert -define jpeg:size=401x696 Hiu-Fung_Wan.jpeg -thumbnail 401x401^ -gravity North -extent 401x401 Hiu-Fung_Wan.png

crop and resize

.. code:: bash

   W=$((360*2))
   H=$((480*2))
   I="$HOME/Telegram Desktop/photo_2021-09-01_14-17-35.jpg"
   O="/tmp/resize.jpg"
   echo
   magick convert "$F" -gravity center -crop 3:4 -resize "${W}x${H}" "$O"
   echo
   file "$O"
   echo
   ls -lh "$O"
   echo


Makefile
========

`Appendix A Quick Reference <https://www.gnu.org/software/make/manual/html_node/Quick-Reference.html>`__

`Special Built-in Target Names <https://www.gnu.org/software/make/manual/html_node/Special-Targets.html>`__

`Functions for String Substitution and Analysis
<https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#Text-Functions>`__

.. code:: Makefile

   $(word 2,$^)
   $(filter-out $<,$^)
   $(filter-out $(word 3,$^),$^)

recursively remove binary

.. code:: Makefile
   
   clean:
   	find . -type f -a \( -name "*.o" -o -name "*.out" \) -exec rm -v {} \;

`PlantUML <https://plantuml.com/>`__

.. code:: Makefile

   clean:
   	@find .                                          \
   		-type f                                       \
   		-a                                            \
   		\(                                            \
   			-name 'DUMMY'                              \
   			-o -name "*.o"                             \
   			-o -name "*.out"                           \
   			-o -name "puml_*.eps"                      \
   			-o -name "puml_*.pdf"                      \
   			-o -name "puml_*.png"                      \
   			-o -name "puml_*.svg"                      \
   		\)                                            \
   		-a                                            \
   		\(                                            \
   			-not -name 'DUMMY'                         \
   			-a -not -name "puml_cdecl.svg"             \
   			-a -not -name "puml_submit_divl_lib32.svg" \
   			-a -not -name "puml_utos.svg"              \
   		\)                                            \
   		-exec rm -v {} \;


`MediaWiki`__
=============

.. __: https://www.mediawiki.org/

`Manual:Date_formatting <https://www.mediawiki.org/wiki/Manual:Date_formatting>`__

`{{cite web}} <https://en.wikipedia.org/wiki/Template:Cite_web>`__

`zh_xx conversion <https://zh.wikipedia.org/wiki/Wikipedia:%E7%B9%81%E7%AE%80%E5%A4%84%E7%90%86>`__

`force rename title <https://zh.wikipedia.org/wiki/Help:%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E7%9A%84%E7%B9%81%E7%AE%80%E3%80%81%E5%9C%B0%E5%8C%BA%E8%AF%8D%E5%A4%84%E7%90%86#%E6%8E%A7%E5%88%B6%E8%87%AA%E5%8A%A8%E8%BD%AC%E6%8D%A2%E7%9A%84-{zh-cn:%E4%BB%A3%E7%A0%81;zh-tw:%E7%A8%8B%E5%BC%8F%E7%A2%BC}->`__

.. WARNING: Pygments lexer name 'mediawiki' is not known
.. code:: text

   -{T|New Title}-

Verilog
=======

`assertion <https://stackoverflow.com/a/31302223>`__

.. code:: verilog

   `define assert(signal,value) \
   if(signal!==value)begin \
       $display("ASSERTION FAILED in %m: signal != value"); \
       $finish; \
   end

   // ui.out: ui.c:21: shm_connect: Assertion `shmid>=0' failed.

   if()begin
     $display("%s:%03d: %m: Assertion failed.",`__FILE__,`__LINE__);
     $finish();
   end

timeout

.. code:: verilog

   initial begin #100 $finish;

conditional VCD dump

.. code:: verilog
   
   `ifdef VCD
     initial begin
       $dumpfile(`VCD);
       $dumpvars;
     end
   `endif

Footnotes
=========

.. [#] Used by U-Boot. ``make help | grep cocci``