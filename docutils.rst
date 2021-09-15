.. include:: include/substitution.txt

==============
|ico| Docutils
==============

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

.. | |b| ` <>`__

| Tutorials from `Docutils`_
| |b| :raw-html:`<a style="text-decoration:line-through;" href="https://docutils.sourceforge.io/docs/user/rst/quickref.html">Quick reStructuredText</a>`
| |b| `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`__
| |b| `reStructuredText Cheat Sheet <https://docutils.sourceforge.io/docs/user/rst/cheatsheet.txt>`__
| |b| `Docutils FAQ <https://docutils.sourceforge.io/FAQ.html>`__

| Tutorials from others
| |b| `Publishing sphinx-generated docs on github <https://daler.github.io/sphinxdoc-test/includeme.html>`__
| |b| `Sampledoc <https://matplotlib.org/sampledoc/>`__
| |b| `Sample reStructuredText PEP Template <https://www.python.org/dev/peps/pep-0012/>`__

| Documentations from `Docutils`_
| |b| `reStructuredText Markup Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`__
| |b| `reStructuredText Interpreted Text Roles <https://docutils.sourceforge.io/docs/ref/rst/roles.html>`__
| |b| `reStructuredText Directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`__


Misc
====

Ongoing Transition from GitHub Flavored Markdown to reStructuredText ...

`Open links in new window <https://stackoverflow.com/a/57733265>`__

`live reST online <http://rst.ninjs.org>`__

.. :tree:`x/y/z`
.. https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks

| Unicode
| |b| :tree:`substitution.txt`
| |b| `<http://www.amp-what.com/>`__
| |b| `<https://www.toptal.com/designers/>`__

that damn hr

.. code:: reStructuredText

   .. \:orphan:

   .. include:: include/substitution.txt

   ========================================================================
   :raw-html:`<del>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<del>`
   ========================================================================

   `Close #8201: Emit a warning if toctree contains duplicated entries #8203 <https://github.com/sphinx-doc/sphinx/pull/8203>`__

   .. horizontal line for navbar
   .. float:
   .. line-height:
   .. margin:
   .. padding:
   .. height:
   .. width:
   .. \|hrop|  replace:: :raw-html:`<span style="background:#777777;float:left;height:2px;width:100%;">&nbsp;</span>`
   .. \|hred|  replace:: :raw-html:`<span style="background:#777777;float:left;height:2px;width:100%;">&nbsp;</span>`
   .. \|hrmid| replace:: :raw-html:`<span style="float:left;width:100%;"><s>xxxx</s></span>`
   .. \|hrmid| replace:: :raw-html:`<hr display=inline />`
   .. :raw-html:`<s><span style="background:#888888;width:100%;float:left;">&nbsp;</span></s><br />Hardware`
   .. :raw-html:`<s>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</s><br />Hardware`
   .. :raw-html:`<span style="text-decoration:overline">Hardware</span>`
   .. :raw-html:`<hr />` Hardware
   .. :raw-html:`<span style="float:left;text-decoration:overline;width:100%;">Hardware</span>`
   .. https://codepen.io/ericrasch/pen/Irlpm


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


Syntax.Others
=============

`link1`_ `link2`__
(combination of `Anonymous Hyperlink`__ and `Indirect Hyperlink`__ ) [#]_

.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks
.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#indirect-hyperlink-targets

.. __: link1_

.. _link1: https://www.example.org

`Enumerated List`_ |:point_left:| Click to go to the `internal hyperlink target with empty link block`__ |:dart:|\ iht

.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#internal-hyperlink-targets

.. _Enumerated List:

:emlink:`Enumerated List <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists>` |:dart:|\ iht

1. li
2. li
#. li w/ auto-enumerator
#. li w/ auto-enumerator

(The following is a :emlink:`Line Block <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks>`)

| The following are missing syms :rtdissue:`1115` :rtdissue:`1145`
| |b| :emlink:`Bullet List <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists>`
| |b| arabic numerals: 1, 2, 3, ... (no upper limit)
| |b| uppercase alphabet characters: A, B, C, ..., Z
| |b| lower-case alphabet characters: a, b, c, ..., z
| |b| uppercase Roman numerals: I, II, III, IV, ..., MMMMCMXCIX (4999)
| |b| lowercase Roman numerals: i, ii, iii, iv, ..., mmmmcmxcix (4999)

:emlink:`(F/FOD) Field List <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists>`

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

:emlink:`(O/FOD) Option List <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists>`

-a      Output all.
-b      Output both (this description is
        quite long).
-c arg  Output just arg.
--long  Output all day long.

:emlink:`Literal Block <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks>`

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

:emlink:`Doctest Block <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks>`

>>> print "This is a doctest block."
This is a doctest block.


|:point_down:| :emlink:`Transition <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions>`
(`<hr> <https://www.w3schools.com/TAGS/tag_hr.asp>`__)


Syntax.\ `Roles`__\ :raw-html:`<br />`\ Inline Elements
====================================================================

.. __: https://docutils.sourceforge.io/docs/ref/rst/roles.html

| :emlink:`Implicit Hyperlink Target <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#implicit-hyperlink-targets>`
| Go to `Misc`_
| Go to `#Misc`_

.. _#Misc: Misc_

.. role:: raw-html(raw)

    :format: html

raw html style :raw-html:`<span style="text-align: center; color: green;">green</span>`

:emlink:`(D/FOD) Definition List <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists>`

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

| :emlink:`Inline Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup>`
| |b| \*emphasis\*
| |b| \*\*strong emphasis\*\*
| |b| \`interpreted text\`
| |b| \`\`inline literals\`\`
| |b| :emlink:`|substitution reference| <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references>`
| |b| `Hyperlink Reference`_
      |:point_left:| Click to go to the
      :emlink:`Inline Internal Target <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-internal-targets>`
      |:dart:|\ iit
| |b| \_\`inline internal target\`

| _`Hyperlink Reference` |:dart:|\ iit
| |b| \`phrase\`\_
| |b| singleword\_
| |b| \`anonymous phrase\`\_\ **_**
| |b| anonymous_singleword\_\ **_**

:emlink:`Footnote <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnotes>`

| \[\#lb\]\_ [#lb]_
| \[\99\]\_ [99]_
| \[\#\]\_ [#]_
  \[\#\]\_ [#]_
  \[\#\]\_ [#]_
| \[\*\]\_ [*]_
  \[\*\]\_ [*]_
  \[\*\]\_ [*]_


Reorder Footnotes
=================

| `viewing the entire file with highlighted matches <https://stackoverflow.com/q/981601>`__
| |b| `GREP_COLORS <https://askubuntu.com/q/1042234>`__

::

   export GREP_COLORS='ms=00;34:mc=00;34'
   echo
   egrep \
     -o \
     -e '<a class="footnote-reference brackets" href="#[^>]+>' \
     ~/cgi/cgi-tmp/sphinx/ALARM.html \
     | egrep -e '^.*href="#id[0-9]+".*$|$'
   echo
   egrep \
     -o \
     -e '<dt class="label" id="[^>]+>' \
     -e '<dt class="label" id="id[0-9]+[^>]+>' \
     ~/cgi/cgi-tmp/sphinx/ALARM.html \
     | egrep -e '^.*id="id[0-9]+".*$|$'
   echo
   unset -v GREP_COLORS


`Footnotes`__
=============

.. __: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnotes

----

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

.. include:: include/link.txt
