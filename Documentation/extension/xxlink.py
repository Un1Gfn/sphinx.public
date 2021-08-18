#!/dev/null
# meld ~/beaglebone/Documentation/extension/helloworld.py <(yapf ~/beaglebone/Documentation/extension/helloworld.py)
import inspect
import sphinx

import util


def setup(app: sphinx.application.Sphinx):

    assert __name__ == 'xxlink'
    util.hint(__name__ + '.' + inspect.currentframe().f_code.co_name + '()')  # print(inspect.stack()[0][3])
    assert __name__ in app.config.extensions
    util.verifyapp(app)

    for n in [
        'emlink',
        'ltlink',
        'prlink',  # => docutils.nodes.problematic -> span class="problematic" -> problematic.css -> strikethrough
        'stlink',
    ]: app.add_role(name=n, role=util.link_fn, override=False)

    for n in [
        'prlt',
    ]: app.add_role(name=n, role=util.pr_fn, override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
