import docutils
import inspect
import re
import sphinx  # sphinx.util.docutils.LoggingReporter.error
import sys

import util


def pkg_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    -----+-----------------------------------------------------------
    From | :pkg:`core/base`
    -----+-----------------------------------------------------------
    To   | <a href="https://archlinux.org/packages/core/x86_64/base/>
         |     base
         | </a>
         | <sup>
         |     community
         | </sup>
    -----+-----------------------------------------------------------
    """

    assert      name     == 'pkg'
    assert      rawtext  == ':%s:`%s`' % (name,text)
    assert  len(text)    >= len('_/_')
    assert type(inliner) == docutils.parsers.rst.states.Inliner
    assert      options  == {}
    assert      content  == []

    l = text.split('/')
    assert len(l) == 2
    util.hint(l)
    repo = l[0]
    pkg = l[1]
    del l

    # https://archlinux.org/packages/
    # Inspect <select> below "Repository"
    assert repo in [
        'AUR',
        'community',
        'community-testing',
        'core',
        'extra',
        'kde-unstable',
        'multilib',
        'multilib-testing',
        'testing',
    ]

    # https://wiki.archlinux.org/title/Arch_package_guidelines#Package_naming
    s0 = '[' '@'     '_' '+'       'a-z' '0-9' ']'
    s  = '[' '@' '.' '_' '+' '\\-' 'a-z' '0-9' ']'
    p = '(^%s%s*$)' % (s0, s)
    # https://docs.python.org/3/library/re.html#search-vs-match
    # type((pkg))  == str
    # type((pkg,)) == tuple
    assert (pkg,)     == re.match(pattern=p, string=pkg, flags=re.M).groups()
    assert (pkg, pkg) == re.match(pattern=p, string=pkg, flags=re.M).group(0,1)


    # return [], []
    return [
        docutils.nodes.reference(rawsource=pkg,
                                 text=pkg,
                                 internal=False,
                                 # https://docs.python.org/3/reference/expressions.html#conditional-expressions
                                 refuri='https://aur.archlinux.org/packages/%s/'%(pkg)
                                        if repo == 'AUR'
                                        else 'https://archlinux.org/packages/%s/x86_64/%s/'%(repo,pkg)),
        docutils.nodes.superscript(rawsource=repo,
                                   text=repo),
    ],[]


def aur_nonexist_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
    assert type(inliner.reporter) == sphinx.util.docutils.LoggingReporter
    # msg = '\n' \
    #       '  There is no :aur:`package`\n' \
    #       '  use :pkg:`AUR/package`'
    msg = 'There is no :aur:`package`, use :pkg:`AUR/package`!'
    # return [], [inliner.reporter.warning(msg, line=lineno)]
    return [], [inliner.reporter.error(msg, line=lineno)]
    # return [], [inliner.reporter.severe(msg, line=lineno)] # colorless


def setup(app):

    assert __name__ == 'archlinux'
    util.hint(__name__ + '.' + inspect.currentframe().f_code.co_name + '()')  # print(inspect.stack()[0][3])
    assert __name__ in app.config.extensions

    util.verifyapp(app)
    app.add_role(name='pkg', role=pkg_fn,          override=False)
    app.add_role(name='aur', role=aur_nonexist_fn, override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
