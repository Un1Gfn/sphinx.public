.. include:: include/substitution.txt

====
Bash
====

|:link:| Cheatsheet:\ :ref:`cheatsheet:Bash`


Exec
====

::

   # Normal
   (exec    bash -c "tr '\0' '\n' </proc/\$\$/environ")
   (exec    bash -c '/bin/printenv')
   (exec    bash -c 'builtin declare -x')
   (exec    bash -c 'builtin export -p')
   (exec    bash -c 'builtin set')
   # Empty environmet
   (exec -c bash -c "tr '\0' '\n' </proc/\$\$/environ")
   (exec -c bash -c '/bin/printenv')
   (exec -c bash -c 'builtin declare -x')
   (exec -c bash -c 'builtin export -p')
   (exec -c bash -c 'builtin set')


`Redirection`__
===============

.. __: https://www.gnu.org/software/bash/manual/html_node/Redirections.html

|    :file:`~/ios.bashrc`
|    [#40907888]_

experiment
----------

1. spawn a terminal
#. ``cd /tmp/ && tput reset && echo $$ >|/tmp/pid_redir_exp && clear && echo && echo "  $(tty)" && echo && echo "  \$\$ = $$" && echo``
#. ``exec REDIRECTION [REDIRECTION...]``
#. spawn another terminal
#. ``ls -Al /proc/"$(< /tmp/pid_redir_exp)"/fd; echo``
#. ``kill -SIGABRT "$(< /tmp/pid_redir_exp)"; rm -v /tmp/pid_redir_exp``

::

   file /proc/$$/fd/*

| ``exec >file 2>&1``
|    |rarr| |equiv| ``1>file 2>&1``
|    |rarr| first redirect stdout to file, then copy stderr to stdout (which is redirected to file)
|    |rarr| result:

.. code:: text

   /proc/*1/fd/1:   symbolic link to /tmp/file
   /proc/*1/fd/2:   symbolic link to /tmp/file

| ``exec 2>&1 >file``
|    |rarr| |equiv| ``2>&1 1>file``
|    |rarr| first copy stderr to stdout (no effect), then redirect stdout to file
|    |rarr| result

.. code:: text

   /proc/*/fd/1:   symbolic link to /tmp/file
   /proc/*/fd/2:   symbolic link to /dev/pts/1

synopsis
--------

\I\. *fd number* + *redirection*

| \I\I\.\
  ``{VAR}`` + *redirection* (|:green_circle:| ``<`` ``>|``) (|:no_entry_sign:| ``>``)
|    allocate a file descriptor greater than 10
|    assign its number to ``$VAR``

\III\. *redirection*

*redirection*
-------------

.. note::

   | ``L`` - *natural number* / ``{VAR}``
   | ``R`` - *natural number* / ``$VAR`` / *file*


``<...``
   |equiv| ``0<...``

``>...``
   |equiv| ``1>...``

:ltpr:`$VAR` ``{VAR}`` + ``>&-``/``<&-``
   close file descriptor ``$VAR``

``&>...``
   | |equiv| ``1>... 2>&1``
   | |equiv| ``1>... 2>...``

``L<&R``
   | `dup2`_\ (R,L)
   | ``L`` defaults to ``0`` (stdin)

``L>&R``
   | `dup2`_\ (R,L)
   | ``L`` defaults to ``1`` (stdout)

.. _dup2: https://man.archlinux.org/man/dup2.2#dup2()

`practical use for moving file descriptors <https://unix.stackexchange.com/q/65000/>`__

``L<&R-``
   |equiv| ``L<&R R<&-``

``L>&R-``
   |equiv| ``L>&R R>&-``

``L<>R``
   | open ``R`` for both reading and writing on file descriptor ``L``
   | ``L`` defaults to ``0``/stdin

`dialog`__
--------------------

.. __: https://man.archlinux.org/man/dialog.1

| `<http://mywiki.wooledge.org/BashFAQ/002>`__
| `<https://askubuntu.com/questions/491509/how-to-get-dialog-box-input-directed-to-a-variable>`__
| `<https://ss64.com/bash/syntax-redirection.html>`__
| `<https://stackoverflow.com/questions/13426908/dialog-in-bash-is-not-grabbing-variables-correctly>`__
| `<https://stackoverflow.com/questions/40907888/linux-bash-how-to-open-a-websocket-connection-as-client>`__
| `<https://stackoverflow.com/questions/962255/how-to-store-standard-error-in-a-variable>`__
| `<https://tldp.org/LDP/abs/html/io-redirection.html>`__
| `<https://unix.stackexchange.com/questions/42728/what-does-31-12-23-do-in-a-script>`__
| `<https://www.configserverfirewall.com/linux-tutorials/bash-standard-error-variable/>`__

items ::

   N=6; \
   cat >/tmp/items <<EOF
   0 "AZKi"
   1 "Baelz"
   2 "Calliope"
   3 "Dorayaki"
   4 "EnMa"
   5 "alksdjfljslfjsljflsjdlfkjsldkfjsfd"
   EOF

approach A ::

   exec 3>&1; \
   result="$(xargs env TERM=xterm-256color dialog \
     --default-item 2 \
     --menu "title" \
     $((2+1+N+7+1)) 0 $N \
     0</tmp/items 2>&1 1>&3 \
   )"; \
   printf "\n\n%s\n\n" "$result"

.. table::
   :align: left
   :widths: auto

   ================================================== ===================== ============= ============= =============
    \                                                  0/stdin               1/stdout      2/stderr      3           
   ================================================== ===================== ============= ============= =============
    \                                                  |:desktop:|          |:desktop:|   |:desktop:|   \-           
    :command:`exec 3>&1`                               |:desktop:|          |:desktop:|   |:desktop:|   |:desktop:|  
    :command:`$(...)`\ |br|\ :command:`0</tmp/items`   |:page_facing_up:|   ``|``         |:desktop:|   |:desktop:|  
    :command:`2>&1`                                    |:page_facing_up:|   ``|``         ``|``         |:desktop:|  
    :command:`1>&3`                                    |:page_facing_up:|   |:desktop:|   ``|``         |:desktop:|  
    :command:`exec 3>&-`                               |:page_facing_up:|   |:desktop:|   ``|``         \-           
   ================================================== ===================== ============= ============= =============

approach B ::

   result="$(xargs env TERM=xterm-256color dialog \
     --default-item 2 \
     --menu "title" \
     $((2+1+N+7+1)) 0 $N \
     0</tmp/items {VAR}>&2- 2>&1- 1>&${VAR}- \
   )"; printf "\n\n%s\n\n" "$result"

.. table::
   :align: left
   :widths: auto

   ==================================================== ==================== ============= ============= =============
    \                                                    0/stdin              1/stdout      2/stderr      $VAR        
   ==================================================== ==================== ============= ============= =============
    \                                                    |:desktop:|          |:desktop:|   |:desktop:|   \-          
    :command:`$(...)`\ |br|\ :command:`0</tmp/items`     |:page_facing_up:|   ``|``         |:desktop:|   \-          
    :command:`3>&2-`                                     |:page_facing_up:|   ``|``         \-            |:desktop:| 
    :command:`2>&1-`                                     |:page_facing_up:|   \-            ``|``         |:desktop:| 
    :command:`1>&3-`                                     |:page_facing_up:|   |:desktop:|   ``|``         \-          
   ==================================================== ==================== ============= ============= =============

.. code:: shell-session

   $ ls -a -p <bash_PID>
   $ ls -a -p <dialog_PID>
   $ ls -a -p <xargs_PID>
   COMMAND FD  TYPE DEVICE SIZE/OFF     NODE NAME
   ...

:abbr:`LIFO (last-in, first-out)`


Completion
==========

| `5.2 Bash Variables <https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html>`__
  - ``COMP_*``
| `8.6 Programmable Completion           <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion.html>`__
| `8.7 Programmable Completion Builtins  <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>`__
| `8.8 A Programmable Completion Example <https://www.gnu.org/software/bash/manual/html_node/A-Programmable-Completion-Example.html>`__


Footnotes
=========

.. include:: include/footnote.txt

