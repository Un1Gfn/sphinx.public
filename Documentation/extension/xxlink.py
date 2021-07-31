# meld ~/beaglebone/Documentation/extension/helloworld.py <(yapf ~/beaglebone/Documentation/extension/helloworld.py)

# import docutils.nodes
# import os  # os.path.exists()
import docutils
import inspect  # getmembers
import re
import sphinx
import urllib.parse  # urllib.parse.urlparse()

import util


# class HelloWorldDirective(docutils.parsers.rst.Directive):
#     def run(self):
#         # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_node
#         return [docutils.nodes.paragraph(text='nnn')]


def parse(s):

    # Avoid regex
    # https://docs.python.org/3/library/stdtypes.html?#str.rfind

    # s='  < y<x>slsd< >sdlkq3 > <    s         <asd>  f> <sdf><k>'
    # print(re.compile(pattern=split, flags=re.M).search(s).group())

    # https://docs.python.org/3/library/re.html
    # https://docs.python.org/3/howto/regex.html
    # https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
    split = '^(.+)<(.*?)>$'
    g = re.compile(pattern=split, flags=re.M).search(s).groups()
    assert len(g) == 2
    # print(g)

    strip = '^\s*(.+?)\s*$'
    gg = re.compile(pattern=strip, flags=re.M).search(g[0]).groups()
    assert len(gg) == 1
    # print(gg)

    # https://stackoverflow.com/a/38020041
    u = urllib.parse.urlparse(g[1])
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

    return {'title': gg[0], 'url': g[1]}

    # util.hint(result)
    # title=''
    # url=''
    # i=0

    # while True:
    #     assert i < len(text)
    #     if text[i] == '<':
    #         break
    #     assert text[i].isalpha() or text[i].isdigit() or text[i] == ' ':
    #     title += text[i]
    #     i = i + 1

    # assert text[i] == '<'
    # i = i + 1

    # while True:
    #     assert i < len(text)
    #     if text[i] == '>':
    #         break
    #     url += text[i]
    #     i = i + 1

    # assert len(url) >= 1


# https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_role
# https://docutils.sourceforge.io/docs/howto/rst-roles.html#define-the-role-function
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/parsers/rst/roles.py
# def xxlink_fn(xx, name, rawtext, text, lineno, inliner, options={}, content=[]):
def xxlink_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):

    # assert (xx.__name__, xx,) in inspect.getmembers(docutils.nodes)
    assert       name         in ['emlink', 'stlink']
    assert       rawtext      == ':%s:`%s`' % (name, text)
    assert   len(text)        >= len('_ <_://_>')
    assert  type(inliner)     == docutils.parsers.rst.states.Inliner
    assert       options      == {}
    assert       content      == []
    # util.hint({'lineno': lineno, 'name': name, 'text': text})

    result = parse(text)

    # assert type(inliner.reporter) == sphinx.util.docutils.LoggingReporter
    # msg = [inliner.reporter.warning(result, line=lineno)]
    msg = []

    # root = docutils.nodes.literal('<strong>strong2</strong>')
    # root = docutils.nodes.paragraph(rawsource='<strong>strong1</strong>')
    # root = docutils.nodes.paragraph(text='<strong>strong2</strong>')
    # root = docutils.nodes.paragraph(text=str(result))
    # root = docutils.nodes.strong(text='asdf')

    # https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/parsers/rst/roles.py
    # register_generic_role('strong', nodes.strong)
    # root = docutils.nodes.strong()
    # root += docutils.nodes.emphasis(text='asdf')
    # root += docutils.nodes.superscript(text='2')

    # import docutils.nodes
    # help(docutils.nodes.reference)
    # https://github.com/sphinx-doc/sphinx/blob/ee612ffdeb922ded72e6e3a11bcdc25223abdd53/sphinx/ext/extlinks.py#L75
    # root += docutils.nodes.reference(rawsource='rawsource', text='text', internal=False, refuri='https://example.org')

    root = docutils.nodes.emphasis(rawsource='', text='') if name == 'emlink' else (
           docutils.nodes.strong(rawsource='', text='')   if name == 'stlink' else
           None )
    root += docutils.nodes.reference(rawsource=result['title'],
                                     text=result['title'],
                                     internal=False,
                                     refuri=result['url'])
    return ([root], msg)


# https://stackoverflow.com/a/3137022
# def emlink_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     return xxlink_fn(docutils.nodes.emphasis, **locals())
# def stlink_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     return xxlink_fn(docutils.nodes.strong,   **locals())


def setup(app):

    assert __name__ == 'xxlink'
    util.hint(__name__ + '.' + inspect.currentframe().f_code.co_name + '()') # print(inspect.stack()[0][3])
    assert __name__ in app.config.extensions
    util.verifyapp(app)

    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    # app.disconnect(listener_id=app.connect(event='source-read',
    #                                        callback=lambda app, docname, source: util.hint('source-read\n'),
    #                                        priority=500))

    # app.add_config_value()

    # app.add_directive(name="code", cls=None, override=True)
    # app.add_directive(name='helloworld_directive',
    #                   cls=HelloWorldDirective,
    #                   override=False)

    # app.add_role(name='emlink', role=emlink_fn, override=False)
    # app.add_role(name='stlink', role=stlink_fn, override=False)
    app.add_role(name='emlink', role=xxlink_fn, override=False)
    app.add_role(name='stlink', role=xxlink_fn, override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }