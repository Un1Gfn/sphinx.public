======================
|ico| reStructuredText
======================

.. Include in the beginning, otherwise get [WARNING: Unknown interpreted text role "raw-html"]
.. include:: substitution.txt

.. image:: https://img.shields.io/badge/%F0%9F%9B%A1%EF%B8%8F-shield-success
  :target: https://shields.io/
  :alt: [shield]

|

.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives
.. warning::
  A plain text ``README`` in ``$(git rev-parse --show-toplevel)`` points here. There is **NO** ``readme.rst.``

Contacts
========

| `Docutils Mailing Lists <https://docutils.sourceforge.io/docs/user/mailing-lists.html>`__
| |b| `Developing extensions <https://docutils.sourceforge.io/docs/user/mailing-lists.html#docutils-develop>`__

`Bugs <https://docutils.sourceforge.io/BUGS.html>`__

Readings
========

`awesome-sphinxdoc <https://github.com/yoloseem/awesome-sphinxdoc>`__

.. | |b| ` <>`__

| Tutorials from `Docutils`_
| |b| :raw-html:`<a style="text-decoration:line-through;" href="https://docutils.sourceforge.io/docs/user/rst/quickref.html">Quick reStructuredText</a>`
| |b| `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`__
| |b| `reStructuredText Cheat Sheet <https://docutils.sourceforge.io/docs/user/rst/cheatsheet.txt>`__
| |b| `Docutils FAQ <https://docutils.sourceforge.io/FAQ.html>`__

| Tutorials from `Sphinx`_
| |b| `Getting Started <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`__
| |b| `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__
| |b| `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
| |b| `Sphinx tutorial <https://www.sphinx-doc.org/en/master/tutorial/index.html>`__

| Tutorials from others
| |b| `Read the Docs - Getting Started with Sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`__
| |b| `TYPO3 - Writing documentation <https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/Index.html>`__
| |b| `Publishing sphinx-generated docs on github <https://daler.github.io/sphinxdoc-test/includeme.html>`__
| |b| `RST | Sphinx | Sublime | GitHub <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html>`__
| |b| `Sampledoc <https://matplotlib.org/sampledoc/>`__
| |b| `Sample reStructuredText PEP Template <https://www.python.org/dev/peps/pep-0012/>`__

| Documentations from `Docutils`_
| |b| `reStructuredText Markup Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`__
| |b| `reStructuredText Interpreted Text Roles <https://docutils.sourceforge.io/docs/ref/rst/roles.html>`__
| |b| `reStructuredText Directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`__

| Documentations from `Sphinx`_
| |b| `Sphinx documentation <https://www.sphinx-doc.org/en/master/contents.html>`__
| |b| `Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`__
| |b| `Directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`__
| |b| `Domains <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html>`__

`Extensions`__
==============

.. __: https://www.sphinx-doc.org/en/master/usage/extensions/index.html

`The Python Language Reference <https://docs.python.org/3/reference/>`__ -
`BNF <https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form>`__

| `sphinx.ext.todo <https://www.sphinx-doc.org/en/master/usage/extensions/todo.html>`__
| `sphinxcontrib-emojicodes <https://github.com/sphinx-contrib/emojicodes>`__

| `sphinx.ext.ifconfig <https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html>`__
| `sphinx.ext.graphviz <https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html>`__
| `sphinxcontrib-plantuml <https://github.com/sphinx-contrib/plantuml>`__
| `sphinxcontrib-tikz <https://github.com/sphinx-contrib/tikz>`__

| `sphinxcontrib-video <https://github.com/sphinx-contrib/video>`__
| `sphinxcontrib-youtube <https://github.com/sphinx-contrib/youtube>`__

| `sphinxcontrib-doxylink <https://github.com/sphinx-contrib/doxylink>`__
| `sphinxcontrib-examplecode <https://github.com/sphinx-contrib/examplecode>`__

| Create [#]_ [#]_ [#]_ [#]_ [#]_ [#]_ [#]_ an `extension`__
| |b| Define a custom role ``:emlink:``, similar to `\:download\:`__
| |b| Render |emlink_role| to |emlink_html|
| |b| Post to `SO/q/9645321`__

.. |emlink_role| replace:: :code:`:emlink:`x <y>``
.. |emlink_html| replace:: :code:`<em><a style="font-style:italic;" href="y">x</em>`

.. __: https://www.sphinx-doc.org/en/master/usage/extensions/index.html
.. __: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-download
.. __: https://stackoverflow.com/questions/9645321/insert-a-link-into-bold-text-in-restructuredtext

Misc
====

Ongoing Transition from GitHub Flavored Markdown to reStructuredText ...

:download:`Sphinx Favicon (SVG)<https://raw.githubusercontent.com/sphinx-doc/sphinx/master/doc/_static/favicon.svg>`.

`live reST online <http://rst.ninjs.org>`__


.. :tree:`x/y/z`
.. https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks

| Unicode
| |b| :tree:`Documentation/substitution.txt`
| |b| `<http://www.amp-what.com/>`__
| |b| `<https://www.toptal.com/designers/>`__

| rtd_linux
| |b| `conf.py`__
| |b| `theme_overrides.css`__
| |b| `Specific guidelines for the kernel documentation`__

.. __: https://github.com/torvalds/linux/blob/master/Documentation/conf.py
.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/sphinx-static/theme_overrides.css
.. __: https://www.kernel.org/doc/html/latest/doc-guide/sphinx.html#specific-guidelines-for-the-kernel-documentation

h2 Chapters
===========

h3 Section
----------

h4 Subsection
~~~~~~~~~~~~~

h5 ?
""""

h6 ?
^^^^

h7 ?
****

h8 ?
++++

h9 ?
####

.. = - ` : ' " ~ ^ _ * + # < >

|

Build
=====

| Build to ``~/beaglebone.gh-pages`` and push to ``gh-pages`` branch
| |b| `GitHub Pages with Python Sphinx <https://www.docslikecode.com/articles/github-pages-python-sphinx>`__
| |b| `sphinx.ext.githubpages <https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html>`__

.. code:: bash

  cd ~/beaglebone/Documentation
  sphinx-quickstart

.. code:: bash

  rm -rf ~/beaglebone/Documentation/_build
  rm -rf ~/cgi/cgi-tmp/sphinx

`sphinx-build(1) <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`__

.. code:: bash

  cd ~/beaglebone/Documentation
  ls -d1 conf.py *rst *txt extension/* | entr sphinx-build -b html . _build
  ls -d1 conf.py *rst *txt extension/* | entr sphinx-build -b html . ~/cgi/cgi-tmp/sphinx
  printf "\n  file://%s\n\n" "$(realpath _build/index.html)"

Syntax
======

Other Syntax
------------

`link1`_ `link2`__
(combination of `Anonymous Hyperlink <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks>`__
and `Indirect Hyperlink <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#indirect-hyperlink-targets>`__ ) [#]_

.. __: link1_

.. _link1: https://www.example.org

`Enumerated List`_ |l| Click to go to the `internal hyperlink target with empty link block`__ |hit|\ iht

.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#internal-hyperlink-targets

.. _Enumerated List:

:raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists">Enumerated List</a>` |hit|\ iht

1. li
2. li
#. li w/ auto-enumerator
#. li w/ auto-enumerator

(The following is a :raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks">Line Block</a>`)

| The following are missing syms :rtdissue:`1115` :rtdissue:`1145`
| |b| :raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists">Bullet List</a>`
| |b| arabic numerals: 1, 2, 3, ... (no upper limit)
| |b| uppercase alphabet characters: A, B, C, ..., Z
| |b| lower-case alphabet characters: a, b, c, ..., z
| |b| uppercase Roman numerals: I, II, III, IV, ..., MMMMCMXCIX (4999)
| |b| lowercase Roman numerals: i, ii, iii, iv, ..., mmmmcmxcix (4999)

:raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists">Field List</a>`

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer

:raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists">Option List</a>`

-a      Output all.
-b      Output both (this description is
        quite long).
-c arg  Output just arg.
--long  Output all day long.

:raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks">Literal Block</a>`

::

     block.
    literal
   a
  is
 This


  This
    is
      a
       block
        quote
  https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes

:raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks">Doctest Block</a>`

>>> print "This is a doctest block."
This is a doctest block.


|d| :raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions">Transition</a>`

----

`Roles`__ / Inline Elements
---------------------------

| :raw-html:`<a style="font-style:italic;" href="https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-manpages_url">Cross-reference manpage</a>`
| Man page of :manpage:`uname(1)`

.. __: https://docutils.sourceforge.io/docs/ref/rst/roles.html

| :raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#implicit-hyperlink-targets">Implicit Hyperlink Target</a>`
| Go to `Misc`_
| Go to `#Misc`_

.. _#Misc: Misc_

.. role:: raw-html(raw)

    :format: html

raw html style :raw-html:`<span style="text-align: center; color: green;">green</span>`

(The following is a `definition list <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists>`__)

\:doc:\`Hardware`
  `Direct link to documents <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc>`__

\:file:\`default.conf`
  File

\:kbd:\`Ctrl+C`
  Key press

.. https://stackoverflow.com/q/9645321/insert-a-link-into-bold-text-in-restructuredtext/63394243#63394243
.. _it: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup
.. |it| replace:: *italic link*

*italic text* |it|_ *italic text*

| `Inline Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup>`__
| |b| \*emphasis\*
| |b| \*\*strong emphasis\*\*
| |b| \`interpreted text\`
| |b| \`\`inline literals\`\`
| |b| \|substitution reference\|
| |b| `Hyperlink Reference`_ |l| Click to go to the `inline internal target`__ |hit|\ iit
| |b| \_\`inline internal target\`

.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-internal-targets

| _`Hyperlink Reference` |hit|\ iit
| |b| \`phrase\`\_
| |b| singleword\_
| |b| \`anonymous phrase\`\_\ **_**
| |b| anonymous_singleword\_\ **_**

:raw-html:`<a style="font-style:italic;" href="https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnotes">Footnote</a>`

| \[\#lb\]\_ [#lb]_
| \[\99\]\_ [99]_
| \[\#\]\_ [#]_
  \[\#\]\_ [#]_
  \[\#\]\_ [#]_
| \[\*\]\_ [*]_
  \[\*\]\_ [*]_
  \[\*\]\_ [*]_

`Directives`__ / Block Elements
-------------------------------

.. __: https://docutils.sourceforge.io/docs/ref/rst/directives.html

`Admonitions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives>`__

.. | `directives`_ - block elements

.. danger::
  danger

.. error::
  error

.. warning::
  warning

.. caution::
  caution

.. attention::
  attention

.. important::
  important

.. hint::
  hint

.. tip::
  tip

.. note::
  note

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions

`Footnotes`__
=============

.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnotes

----

.. [#] https://www.sphinx-doc.org/en/master/extdev/index.html
.. [#] https://www.sphinx-doc.org/en/master/extdev/appapi.html
.. [#] https://www.sphinx-doc.org/en/master/extdev/markupapi.html
.. [#] https://www.sphinx-doc.org/en/master/development/index.html
.. [#] https://docutils.sourceforge.io/docs/howto/rst-roles.html
.. [#] https://protips.readthedocs.io/link-roles.html
.. [#] https://doughellmann.com/posts/defining-custom-roles-in-sphinx/

.. [#] https://docutils.sourceforge.io/docs/user/rst/quickref.html#indirect-hyperlink-targets

----

.. [#lb] This is a manually *labeled*  footnote.
.. [99]  This is a manually *numbered* footnote

The numbering is determined by the order of the footnotes (here), not by the order of the references (above).

.. [#] This is     an      auto-numbered footnote.
.. [#] This is     another auto-numbered footnote.
.. [#] This is yet another auto-numbered footnote.

.. [*] This is     an      auto-symbol footnote.
.. [*] This is     another auto-symbol footnote.
.. [*] This is yet another auto-symbol footnote.

----

.. include:: link.txt
