# meld ~/beaglebone/Documentation/extension/helloworld.py <(yapf ~/beaglebone/Documentation/extension/helloworld.py)

# import docutils.nodes
# import os  # os.path.exists()
import docutils
import inspect  # getmembers
import re
import sphinx
import sphinx.util  # sphinx.util.nodes.split_explicit_title
import urllib.parse  # urllib.parse.urlparse()

import util


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

    # https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/sphinx_toolbox/wikipedia.py
    has_explicit, title, target = sphinx.util.nodes.split_explicit_title(text)
    if not has_explicit:
        assert title == target

    # assert type(inliner.reporter) == sphinx.util.docutils.LoggingReporter
    # msg = [inliner.reporter.warning(result, line=lineno)]
    msg = []

    root = docutils.nodes.emphasis(rawsource='', text='') if name == 'emlink' else (
           docutils.nodes.strong(rawsource='', text='')   if name == 'stlink' else
           None )
    root += docutils.nodes.reference(rawsource=title,
                                     text=title,
                                     internal=False,
                                     refuri=target)
    return [root], msg
    # return ([root], msg,)


def setup(app):

    assert __name__ == 'xxlink'
    util.hint(__name__ + '.' + inspect.currentframe().f_code.co_name + '()') # print(inspect.stack()[0][3])
    assert __name__ in app.config.extensions
    util.verifyapp(app)

    app.add_role(name='emlink', role=xxlink_fn, override=False)
    app.add_role(name='stlink', role=xxlink_fn, override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
