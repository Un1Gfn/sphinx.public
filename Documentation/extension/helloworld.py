# meld ~/beaglebone/Documentation/extension/helloworld.py <(yapf ~/beaglebone/Documentation/extension/helloworld.py)

import docutils
import sphinx

import termcolor
import sys

import re

def color(s):
    return termcolor.colored(s, color='cyan')

def hint(*argv):
    # print(type(argv))
    if 1 == len(argv):
        print(color(argv[0]), file=sys.stderr)
    else:
        assert 0 == len(argv)
        print()


class HelloWorldDirective(docutils.parsers.rst.Directive):
    def run(self):
        # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_node
        return [docutils.nodes.paragraph(text='nnn')]


# https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_role
# https://docutils.sourceforge.io/docs/howto/rst-roles.html#define-the-role-function
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/parsers/rst/roles.py
def emlink_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
    assert name =='emlink'
    assert len(text) >= len('_ <_://_._>')
    assert rawtext == ':%s:`%s`'%(name,text)
    assert inliner
    assert options == {}
    assert content == []
    # hint({
    #     'lineno': lineno,
    #     'name': name,
    #     'text': text})

    pattern='([^<]+) +<([^>]+)>'
    # p = re.search(pattern,text,0)
    p = re.compile(pattern)
    m = p.search(text)

    # print(m.group(0))
    # print(m.group(1))
    # print(m.group(2))
    g = m.groups()
    assert len(g) == 2
    hint({
        'title': g[0],
        'url': g[1]})

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

    return [], []
    # return ['<strong>','123','</strong>'], [color('emlink_fn()')]


def setup(app):

    hint()

    # hint(type())
    hint('setup()')
    assert sphinx.application.Sphinx == type(app)
    hint()

    # print(sys.path)
    app.require_sphinx(version='4.1') # https://www.sphinx-doc.org/en/master/_modules/sphinx/application.html
    assert sphinx.version_info == (4, 1, 2, 'final', 0)
    assert 'helloworld' in app.config.extensions
    # hint()

    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    app.disconnect(listener_id=app.connect(event='source-read',
                                           callback=lambda app, docname, source: hint('source-read\n'),
                                           priority=500))

    # app.add_config_value()

    # app.add_directive(name="code", cls=None, override=True)
    app.add_directive(name='helloworld_directive',
                      cls=HelloWorldDirective,
                      override=False)

    app.add_role(name='emlink',
                 role=emlink_fn,
                 override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }