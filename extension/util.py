#!/dev/null
# import urllib.parse
import docutils
import re  # re.match
import sphinx
import sphinx.util  # sphinx.util.nodes.split_explicit_title
import sys  # sys.stderr
import termcolor  # termcolor.colored
import typing
import urllib.parse  # urllib.parse.urlparse()
import define


# https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
# import inspect
# def inspect1():
#     print(inspect.currentframe().f_code.co_name)
#     print(inspect.stack()[0][3])
# def inspect2():
#     print(inspect1.__name__)
#     inspect1()
# inspect2()


# _single_leading_underscore:
# weak "internal use" indicator.
# E.g. from M import * does not import objects whose names start with an underscore
def _color(s: str):
    return termcolor.colored(s, color='cyan')


def _verifyurl(url: str):
    # https://stackoverflow.com/a/38020041
    u = urllib.parse.urlparse(url)
    if u.scheme in ['http', 'https']:
        assert u.netloc
    elif u.scheme in ['ftp']:
        assert u.netloc
        assert u.path
    elif u.scheme in ['file', '']:
        assert not u.netloc
        assert u.path
        # assert os.path.exists(u.path)
    else:
        assert False


def hint(*argv):
    # print(type(argv))
    if 1 == len(argv):
        print(_color(argv[0]), file=sys.stderr)
    else:
        assert 0 == len(argv)
        print()


def verifyapp(app: sphinx.application.Sphinx):
    # assert sphinx.version_info == (4, 1, 2, 'final', 0)
    assert type(app) == sphinx.application.Sphinx
    # https://www.sphinx-doc.org/en/master/_modules/sphinx/application.html
    app.require_sphinx(version='4.1')


def wikiprepend(n: str, t: str) -> str:
    if n in define.wikiprepend_dict.keys():
        t = define.wikiprepend_dict[n] + t
    else:
        assert re.match('^[a-z]{2}link$', n)
    _verifyurl(t)
    # https://www.urlencoder.io/python/
    # https://stackoverflow.com/questions/1695183/how-to-percent-encode-url-parameters-in-python
    # help(urllib.parse.quote)
    return t


def inspectchar(s: str) -> str:
    assert len(s) == 1
    return ',%s,%d,'%(s,ord(s),)


# https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_role
# https://docutils.sourceforge.io/docs/howto/rst-roles.html#define-the-role-function
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/parsers/rst/roles.py
# def link_fn(xx, name, rawtext, text, lineno, inliner, options={}, content=[]):
def link_fn(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: docutils.parsers.rst.states.Inliner,
    options: typing.Dict = {},
    content: typing.List[str] = []
) -> typing.Tuple[typing.List[docutils.nodes.reference],
                  typing.List[docutils.nodes.system_message]]:

    # assert (xx.__name__, xx,) in inspect.getmembers(docutils.nodes)
    # assert       name         in ['emlink', 'stlink', 'wp', ...]
    # assert       rawtext      == ':%s:`%s`' % (name, text)  # Fails with scaped space
    # assert   len(text)        >= len('_ <_://_>')  # Fails with if not has_explicit
    assert       options      == {}
    assert       content      == []

    text_neutralized = docutils.nodes.unescape(text)

    # https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/sphinx_toolbox/wikipedia.py
    has_explicit, title, target = sphinx.util.nodes.split_explicit_title(text_neutralized)
    if not has_explicit:
        assert title == target == text_neutralized

    target = wikiprepend(name, target)

    # if name == 'prlink':
    #     hint()
    #     hint(rawtext+'###')
    #     hint()
    #     hint(text+'###')
    #     hint(inspectchar(text[0]))
    #     hint(inspectchar(text[1]))
    #     hint(inspectchar(text[2]))
    #     hint('...')
    #     hint(inspectchar(text[-1]))
    #     hint(inspectchar(text[-2]))
    #     hint(inspectchar(text[-3]))
    #     hint()
    #     hint(inspectchar(text_neutralized[0]))
    #     hint(inspectchar(text_neutralized[1]))
    #     hint(inspectchar(text_neutralized[2]))
    #     hint('...')
    #     hint(text_neutralized+'###')
    #     hint(inspectchar(text_neutralized[-1]))
    #     hint(inspectchar(text_neutralized[-2]))
    #     hint(inspectchar(text_neutralized[-3]))
    #     assert False

    if text[0] == '\0':
        hint('space prefix detected')
        assert text[1] == ' '
        title = ' ' + title

    if text[-1] == ' ':
        hint('space postfix detected')
        assert text[-2] == '\0'
        assert text[-3] == '>'
        title = title + ' '

    ref = docutils.nodes.reference(rawsource=rawtext,
                                   text=title,
                                   internal=False,
                                   refuri=target)

    root = docutils.nodes.emphasis(rawsource=rawtext, text='').__iadd__(ref)    if name == 'emlink' else (
           docutils.nodes.literal(rawsource=rawtext, text='').__iadd__(ref)     if name == 'ltlink' else (
           docutils.nodes.problematic(rawsource=rawtext, text='').__iadd__(ref) if name == 'prlink' else (
           docutils.nodes.strong(rawsource=rawtext, text='').__iadd__(ref)      if name == 'stlink' else (
           ref))))
           # None ))))

    # assert type(inliner.reporter) == sphinx.util.docutils.LoggingReporter
    # msg = [inliner.reporter.warning(result, line=lineno)]
    msg = []
    return [root], msg
    # return ([root], msg,)


def pr_fn(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: docutils.parsers.rst.states.Inliner,
    options: typing.Dict = {},
    content: typing.List[str] = []
) -> typing.Tuple[typing.List[docutils.nodes.reference],
                  typing.List[docutils.nodes.system_message]]:

    root = docutils.nodes.problematic(rawsource=rawtext, text='')

    root += docutils.nodes.literal(rawsource=rawtext, text=docutils.nodes.unescape(text)) if name in [ 'ltpr', 'prlt' ] else (
            None)

    return [root], []
