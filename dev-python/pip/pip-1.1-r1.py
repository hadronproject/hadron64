metadata = """
summary @ An easy_install replacement for installing pypi python packages
homepage @ http://www.pip-installer.org/
license @ MIT
src_url @ http://pypi.python.org/packages/source/p/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-lang/python:2* dev-python/setuptools
"""

get("python_utils")

configure = lambda: ""
