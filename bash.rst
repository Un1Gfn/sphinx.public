.. include:: include/substitution.txt

====
Bash
====

|:link:| Cheatsheet:\ :ref:`cheatsheet:Bash`


`Redirection`__
===============

.. __: https://www.gnu.org/software/bash/manual/html_node/Redirections.html

|    :file:`~/ios.bashrc`
|    [#40907888]_
|    `putorius <https://www.putorius.net/exec-command.html>`__ - exec
|    `tldp <https://tldp.org/LDP/abs/html/x17974.html>`__ - exec

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

   | ``NV`` - *natural number* / ``{VAR}``
   | ``NF`` - *natural number* / *file*


``<...``
   |equiv| ``0<...``

``>...``
   |equiv| ``1>...``

:ltpr:`$VAR` ``{VAR}`` + ``>&-``/``<&-``
   close file descriptor ``$VAR``

``&>...``
   | |equiv| ``1>... 2>&1``
   | |equiv| ``1>... 2>...``

``NV<&NF``
   | duplicate file descriptor ``NF`` to ``NV``
   | ``NV`` defaults to ``0``/stdin

``NV>&NF``
   | duplicate output file descriptor ``NF`` to ``NV``
   | ``NV`` defaults to ``1``/stdout

`practical use for moving file descriptors <https://unix.stackexchange.com/q/65000/>`__

``NV<&NF-``
   |equiv| ``NV<&NF NF<&-``

``NV>&NF-``
   |equiv| ``NV>&NF NF>&-``

``NV<>NF``
   | open ``NF`` for both reading and writing on file descriptor ``NV``
   | ``NV`` defaults to ``0``/stdin


Footnotes
=========

.. include:: include/footnote.txt

