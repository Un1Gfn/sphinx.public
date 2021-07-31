#!/dev/null
# https://sphinx-toolbox.readthedocs.io/en/latest/extensions/wikipedia.html
# https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/sphinx_toolbox/wikipedia.py
# https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/sphinx_toolbox/utils.py

# from urllib.parse import quote
import sphinx
import inspect
import typing
import util


def setup(app: sphinx.application.Sphinx):

    assert __name__ == 'wikilink'
    util.hint(__name__ + '.' + inspect.currentframe().f_code.co_name + '()')  # print(inspect.stack()[0][3])
    assert __name__ in app.config.extensions
    util.verifyapp(app)

    app.add_role(name='wp', role=util.link_fn, override=False)  # wp - Wikipedia
    app.add_role(name='aw', role=util.link_fn, override=False)  # aw - ArchWiki

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
