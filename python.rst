======
Python
======

Misc
====

.. highlight:: py3

`docs.python.org <https://docs.python.org/3/>`__

`regex <https://docs.python.org/3/library/re.html#regular-expression-syntax>`__
`rawstring <https://docs.python.org/3/library/re.html#raw-string-notation>`__
::

   import re

   x = "a\nb"
   y = r"a\nb"
   print(x)
   print(y)
   print()

   print(bool(re.match(r"^a\nb\Z", x)))
   print(bool(re.match( "^a\nb\\Z", x)))
   print()

   print(bool(re.match(r"^a\\nb\Z", y)))
   print(bool(re.match( "^a\\\\nb\\Z", y)))
   print()

`interactive <https://stackoverflow.com/questions/13432717/>`__ ::

   code.interact(local=locals())

.. highlight:: pycon

`with statement <https://docs.python.org/3/reference/compound_stmts.html#the-with-statement>`__ ::

   >>> f = open("/dev/null",'w')
   >>> f.write("garbage")
   7
   >>> f.__del__()
   >>> f.write("")
   ValueError: I/O operation on closed file.

   >>> f = open("/dev/null",'w')
   >>> f.write("garbage")
   7
   >>> f.__exit__()
   >>> f.write("")
   ValueError: I/O operation on closed file.

   >>> with open("/dev/null",'w') as f:
   ...     f.write("garbage")
   ...
   7

| table
| community/python-texttable
| community/python-prettytable
| community/python-terminaltables
| community/python-rich


Not Tried Yet
=============

.. highlight:: py3

| `the python standard library <https://docs.python.org/3/library/>`__
| `papthlib.PosixPath <https://docs.python.org/3/library/pathlib.html>`__
| `id(os.path) == id(posixpath) <https://docs.python.org/3/library/os.path.html>`__
| `id(os.unlink) == id(posix.unlink) <https://docs.python.org/3/library/posix.html>`__

::

   # not achievable with posix.mkdir()
   # mkdir -p
   os.makedirs()
   pathlib.*Path.makedir(parent=True)

::

   pathlib.*Path("x").joinpath("y")
   posixpath.join(posix.getcwd(), "x", "y")

::

   pathlib.*Path.glob()
   pathlib.*Path.rglob()

::

   pathlib.*Path.parents
   pathlib.*Path.parent
   pathlib.*Path.name
   pathlib.*Path.suffix
   pathlib.*Path.suffixes
   pathlib.*Path.stem

::

   # pathlib.*Path.__str__()
   pathlib.*Path.as_posix()

::

   tempfile.mkstemp()
   tempfile.mkdtemp()

::

   posix.listdir()



