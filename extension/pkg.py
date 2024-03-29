#!/dev/null

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
    assert      rawtext  == ':%s:`%s`' % (name, text)
    assert  len(text)    >= len('_/_')
    assert type(inliner) == docutils.parsers.rst.states.Inliner
    assert      options  == {}
    assert      content  == []

    l = text.split('/')
    assert len(l) == 2
    # util.hint(l)
    repo = l[0]
    pkg = l[1]
    del l

    # https://archlinux.org/packages/
    # Inspect <select> below "Repository"
    assert repo in [
        'AUR',
        'alarm',
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

    # https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
    refuri='https://example.com/'
    match repo:
        case 'core'|'extra'|'community'|'multilib':
            refuri=f'https://archlinux.org/packages/{repo}/x86_64/{pkg}/'
        case 'AUR':
            refuri=f'https://aur.archlinux.org/packages/{pkg}'
        case 'alarm':
            refuri=f'https://archlinuxarm.org/packages/armv7h/{pkg}'
        # case 'alpine.main'|'alpine.repo':
            # refuri=f'https://pkgs.alpinelinux.org/package/edge/{repo}/aarch64/{pkg}'
        case _:
            assert False

    return [
        docutils.nodes.reference(rawsource=pkg,
                                 text=pkg,
                                 internal=False,
                                 # https://docs.python.org/3/reference/expressions.html#conditional-expressions
                                 # refuri=''+pkg if repo == '' else ()
                                 refuri=refuri),
        docutils.nodes.superscript(rawsource=repo,
                                   text=repo),
    ],[]


def aur_nonexist_fn(name: str, rawtext: str, text: str, lineno, inliner, options={}, content=[]):
    assert type(inliner.reporter) == sphinx.util.docutils.LoggingReporter
    # msg = '\n' \
    #       '  There is no :aur:`package`\n' \
    #       '  use :pkg:`AUR/package`'
    msg = 'There is no :aur:`package`, use :pkg:`AUR/package`!'
    # return [], [inliner.reporter.warning(msg, line=lineno)]
    return [], [inliner.reporter.error(msg, line=lineno)]
    # return [], [inliner.reporter.severe(msg, line=lineno)] # colorless
