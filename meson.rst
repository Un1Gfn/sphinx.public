.. include:: include/substitution.txt

=========
`meson`__
=========

.. __: https://mesonbuild.com/

Misc
====

:kbd:`/home/darren/gtk3/Makefile`

static `sdl2 <https://mesonbuild.com/GuiTutorial.html>`__ from `wrapdb <https://mesonbuild.com/Wrapdb-projects.html>`__

`community <https://mesonbuild.com/index.html#community>`__ |:speech_balloon:|

`List of projects using Meson <https://mesonbuild.com/Users.html>`__


meson.build
===========

`tutorial <https://mesonbuild.com/Tutorial.html>`__

`howtox <https://mesonbuild.com/howtox.html>`__

meson.build `rewriter <https://mesonbuild.com/Rewriter.html>`__

| built-in `options <https://mesonbuild.com/Builtin-options.html>`__
| ``default_options:['option=value']``

arbitrary gcc `-lxxx <https://mesonbuild.com/howtox.html#add-math-library-lm-portably>`__ ::

   cc = meson.get_compiler('c')
   m_dep = cc.find_library('xxx', required : false)
   executable(..., dependencies : m_dep)

`reference tables <https://mesonbuild.com/Reference-tables.html>`__

`An in-depth tutorial <https://mesonbuild.com/IndepthTutorial.html>`__

``run_command()``

::

   # meson init --help
   meson init -n projectname -e hello.out -d json-c,yaml-0.1 -l c --builddir builddir --type library --version 0.1
   # pygmentize -l meson meson.build


Setup
=====

::

   # meson setup -Dsome_option=value builddir
   # meson setup --some_option builddir
   meson setup builddir


Compile
=======

::

   meson compile -C builddir


Test
====

::

   meson test -C builddir


Run
===

::

   ./builddir/projectname_test

:pkg:`community/chrpath`


Install
=======

::

   # mkdir pkg
   meson install -C builddir --destdir "$(realpath pkg)"; find pkg | sort
   # ninja -C builddir uninstall; find pkg | sort # requires builddir/meson-logs/install-log.txt


