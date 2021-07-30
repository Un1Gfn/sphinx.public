import sphinx
import sys # sys.stderr
import termcolor # termcolor.colored


# https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
# import inspect
# def inspect1():
#     print(inspect.currentframe().f_code.co_name)
#     print(inspect.stack()[0][3])
# def inspect2():
#     print(inspect1.__name__)
#     inspect1()
# inspect2()


def color(s):
    return termcolor.colored(s, color='cyan')


def hint(*argv):
    # print(type(argv))
    if 1 == len(argv):
        print(color(argv[0]), file=sys.stderr)
    else:
        assert 0 == len(argv)
        print()


def verifyapp(app):
    assert sphinx.version_info == (4, 1, 2, 'final', 0)
    assert type(app) == sphinx.application.Sphinx
    # https://www.sphinx-doc.org/en/master/_modules/sphinx/application.html
    app.require_sphinx(version='4.1')
