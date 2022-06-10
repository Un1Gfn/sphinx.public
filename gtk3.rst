.. include:: include/substitution.txt

====
GTK3
====

.. note::

   squeeze Un1Gfn-obj/gtk4/`readme.md <https://github.com/Un1Gfn-obj/gtk4/blob/master/readme.md>`__


Contacts
========

`gtk development blog <https://blog.gtk.org/>`__

`discourse <https://discourse.gnome.org/c/platform/core/>`__


Misc.GTK4
=========

| `Gtk4 2D action game <https://github.com/lavalfils/poc_gtk4_2D_action_game>`__ I(`post <https://discourse.gnome.org/t/proof-of-concept-for-a-gtk4-2d-action-game-using-only-widgets/6541>`__)
| using gtk4 widgets only
| GPU rendered
| ``gcc -std=gnu11 -g -O0 -Wextra -Wall -Winline -Wshadow -fanalyzer $(pkg-config --cflags gtk4) -o game.out game.c $(pkg-config --libs gtk4)``

| `running glib applications <https://docs.gtk.org/glib/running.html>`__
| ``env G_DEBUG=fatal-warnings ./demo.out``

`compiling gtk applications on unix <https://docs.gtk.org/gtk4/compiling.html>`__

:wp:`reverse domain name notation`

gnome/`gtk best practices <https://wiki.gnome.org/Projects/GTK/BestPractices>`__

/usr/bin/gtk4-query-settings ::

                   ...
        gtk-theme-name: "Adwaita"
   gtk-icon-theme-name: "Adwaita"
                   ...
         gtk-font-name: "Cantarell 11"
                   ...

:stlink:`additional documentation <https://docs.gtk.org/gtk4/#extra>`

| GdkPixbuf library - for loading images in a variety of file formats
| GObject Introspection - a framework for making introspection data available to language bindings
| `fontconfig <https://www.freedesktop.org/wiki/Software/fontconfig/>`__ library provides Pango with a standard way of locating fonts and matching them against font names
| libepoxy - an alternative to libglew
| Graphene - vector and matrix types for 2D and 3D transformations

| build and install the GTK libraries in order
| glib |rarr| cairo |rarr| pango |rarr| gtk

/usr/bin/gtk4-demo

`broadway: run gtk applications within a browser <https://blog.desdelinux.net/en/broadway-ejecuta-aplicaciones-gtk-navegador/>`__

`sysprof <https://wiki.gnome.org/Apps/Sysprof>`__ - function call profiling tool

`create_traditional_menubar() <https://github.com/luigifab/awf-extended/blob/3d8e768a5d57f14066a72d19e4f110fe7fc3dbe0/src/awf.c#L2055>`__

`gnome development <https://developer.gnome.org/>`__



::

   # https://wiki.gnome.org/Valgrind
   # /usr/share/gtk-doc/html/glib/glib-running.html (G_DEBUG)
   # --leak-resolution=high
   # --num-callers=20
   demo.log:
   %.log: %.out %.supp
      env \
        G_DEBUG="fatal-warnings fatal_criticals" \
        G_SLICE=always-malloc \
      valgrind \
        --tool=memcheck \
        --log-file=$@ \
        --num-callers=500 \
        -s \
        --suppressions=/usr/lib/valgrind/default.supp \
        --suppressions=/usr/share/glib-2.0/valgrind/glib.supp \
        --suppressions=/usr/share/gtk-4.0/valgrind/gtk.supp \
        --suppressions=./$(word 2,$^) \
        --gen-suppressions=all \
        --leak-check=full \
        --show-leak-kinds=definite \
      ./$<
      subl $@

Misc.GTK3
=========

`Namespace Gtk – 3.0 <https://docs.gtk.org/gtk3/index.html>`__
