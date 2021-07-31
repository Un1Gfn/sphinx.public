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

    app.add_role(name='emlink', role=util.link_fn, override=False)
    app.add_role(name='stlink', role=util.link_fn, override=False)

    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
