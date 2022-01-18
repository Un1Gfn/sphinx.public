.. include:: include/substitution.txt

===============
ncurses/termios
===============

Examples
========

| `tracursepoint/ <https://github.com/Un1Gfn/tracursepoint>`__
| `parallel/tree/master/exp02/ <https://github.com/Un1Gfn/parallel/tree/master/exp02/>`__
| `df/tree/master/exp05/ <https://github.com/Un1Gfn-electronics/df/tree/master/exp05/>`__
| ~/x200/box.c
| ~/cangjie/key.c
| ~/clash/examples/framebuffer.c


ncurses
=======

| `<https://gist.github.com/alan-mushi/bdc831e0c33ad5db8025>`__
| `<https://stackoverflow.com/questions/13707137/resizing-glitch-with-ncurses>`__
| `<https://forums.justlinux.com/showthread.php?137431-ncurses-detect-when-the-terminal-has-been-resized>`__
| `<https://unix.stackexchange.com/questions/489491/resize-window-in-multi-thread-ncurses-program>`__
| :r:`C_Programming/comments/b6gv0g/ncurses_window_resize_trigger`
| `<https://invisible-island.net/ncurses/ncurses.faq.html#handle_resize>`__

list of ncurses `routines <https://man.archlinux.org/man/ncurses.3x#Routine_Name_Index>`__

color -
:manpage:`curs_color(3x)`
:manpage:`default_colors(3x)`
:manpage:`curs_attr(3x)`

``KEY_*`` :kbd:`/usr/include/ncurses.h:1505`


termios
=======

| `build your own text editor <https://viewsourcecode.org/snaptoken/kilo/index.html>`__
|    `entering raw mode <https://viewsourcecode.org/snaptoken/kilo/02.enteringRawMode.html>`__
|    `3-byte / 4-byte escape sequence <https://viewsourcecode.org/snaptoken/kilo/02.enteringRawMode.html#display-keypresses>`__

wikibooks
- `serial programming <https://en.wikibooks.org/wiki/Serial_Programming>`__
- `termios <https://en.wikibooks.org/wiki/Serial_Programming/termios>`__

| `the TTY demystified <http://www.linusakesson.net/programming/tty/>`__
|    raw mode |larr| vim/readline/ncurses
|    cooked/canonical mode |larr| scanf default
|    TTY device = UART driver + line discipline + TTY driver
|    ``/bin/login`` chmods ``/dev/ttyN``

| Linux
     :manpage:`ioctl_console(2)`
     :manpage:`ioctl_tty(2)`
     :manpage:`console_ioctl(4)`
     :manpage:`tty_ioctl(4)`
| POSIX :emlink:`termios.h(0p) <https://man.archlinux.org/man/termios.h.0p>` :manpage:`termios(3)`
| :manpage:`ttyname(3)`
| :manpage:`stty(1)`
     ``sane``
     ``[-]echo``
     ``intr ^O``

.. table::
   :align: left
   :widths: auto

   ========================== =============== =================================== ===================================
    \                          |enter|         :guilabel:`Ctrl-C`                  |bksp|                            
   ========================== =============== =================================== ===================================
    cooked\ |equiv|\ -raw      |:bricks:|      |:stop_sign:|                       |:wastebasket:|                   
    cbreak\ |equiv|\ -icanon   |:zap:|         |:stop_sign:|                       ``^?``                            
    raw\ |equiv|\ -cooked      |:zap:|         ``^C``                              ``^?``                            
   ========================== =============== =================================== ===================================

.. table::
   :align: left
   :widths: auto

   ============================================ ============================================
    ``000 0100`` = 0x04 = :guilabel:`^D` (EOT)   ``100 0100`` = 0x44 = :guilabel:`D`        
    ``000 1000`` = 0x08 = :guilabel:`^H` (\\b)   ``100 1000`` = 0x48 = :guilabel:`H`        
    ``011 1111`` = 0x3F = :guilabel:`?`          ``111 1000`` = 0x7F = :guilabel:`^?` (DEL) 
   ============================================ ============================================

``^(SOMETHING) = (SOMETHING) ^ 100_0000``

::

   gcc -std=gnu11 -g -O0 -Wextra -Wall -Winline -Wshadow -fanalyzer termios.c && ./a.out

| glibc ch17 Low-Level Terminal Interface
|    `subtitles <https://www.gnu.org/software/libc/manual/html_node/index.html#:~:text=how%20to%20determine%20if%20a%20file%20is%20a%20terminal%20device>`__
|    `toc <https://www.gnu.org/software/libc/manual/html_node/index.html#toc-Low_002dLevel-Terminal-Interface-1>`__

.. table::
   :align: left
   :widths: auto

   ======================= ======= =====
    struct termios.\_\_\_   level   I/O
   ======================= ======= =====
    c_iflag                 L       I
    c_oflag                 L       O
    c_lflag                 H       I
   ======================= ======= =====
