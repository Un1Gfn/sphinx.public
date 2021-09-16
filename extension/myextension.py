#!/dev/null
# meld ~/beaglebone/Documentation/extension/helloworld.py <(yapf ~/beaglebone/Documentation/extension/helloworld.py)
# https://sphinx-toolbox.readthedocs.io/en/latest/extensions/wikipedia.html
# https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/sphinx_toolbox/wikipedia.py
# https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/sphinx_toolbox/utils.py

# from urllib.parse import quote
import inspect
import sphinx
import typing
import util
import define
import archlinux


def setup(app: sphinx.application.Sphinx):

    assert __name__ == 'myextension'
    assert __name__ in app.config.extensions
    util.hint(__name__ + '.' + inspect.currentframe().f_code.co_name + '()')  # print(inspect.stack()[0][3])
    util.verifyapp(app)

    for n in define.wikiprepend_dict.keys():
        app.add_role(name=n, role=util.link_fn, override=False)

    # ArchWiki :aw: is provided in wikilink.py, not here
    # Use :pkg:`AUR/package` instead of :aur:`package`
    app.add_role(name='aur', role=archlinux.aur_nonexist_fn, override=False)
    app.add_role(name='pkg', role=archlinux.pkg_fn,          override=False)

    for n in [
        'emlink',
        'ltlink',
        'prlink',  # => docutils.nodes.problematic -> span class="problematic" -> problematic.css -> strikethrough
        'stlink',
    ]: app.add_role(name=n, role=util.link_fn, override=False)

    for n in [
        'ltpr',
        'prlt',
    ]: app.add_role(name=n, role=util.pr_fn, override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
