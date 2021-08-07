.. include:: substitution.txt

==========
Cheatsheet
==========

Bash
========

WIP move everything from :file:`~/cheatsheet.sh`

assertion

.. code:: bash

   [ ] || { notify-send "${BASH_SOURCE[0]}" "${FUNCNAME[0]}${LF}line ${BASH_LINENO[0]}"; return 1; }
   [ ] || { echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; return 1; }
   [ ] || { echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; exit 1; }

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

:manpage:`console_codes(4)`

.. code:: bash

   printf "\n\e[31m%s\e[0m\n\n" "red error"
   printf "\n\e[32m%s\e[0m\n\n" "green ok"
   printf "\n\e[33m%s\e[0m\n\n" "brown warning"
   printf "\n\e[34m%s\e[0m\n\n" "blue info"

C
===

WIP move everything from :file:`~/cheatsheet.c`

| `Sparse, Smatch, and Coccinelle <https://thenewstack.io/checking-linuxs-code-with-static-analysis-tools/>`__\ [#]_
| |b| :wp:`Coccinelle_(software)`
| gcc `-fanalyzer <https://developers.redhat.com/blog/2020/03/26/static-analysis-in-gcc-10>`__
| `splint <https://github.com/splintchecker/splint>`__

Makefile
========

WIP move everything from :file:`~/cheatsheet.Makefile`

Verilog
=======

WIP move everything from :file:`~/cheatsheet.v`

Footnotes
=========

.. [#] Used by U-Boot. ``make help | grep cocci``