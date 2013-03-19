metadata = """
summary @ virtualenvwrapper is a set of extensions to Ian Bicking's virtualenv tool
homepage @ http://www.doughellmann.com/projects/virtualenvwrapper http://pypi.python.org/pypi/virtualenvwrapper
license @ BSD
src_url @ https://pypi.python.org/packages/source/v/virtualenvwrapper/virtualenvwrapper-$version.tar.gz
arch @ ~x86_64
"""

# FIXME: Python3 support

get("python_utils")

depends = """
runtime @ dev-python/virtualenv dev-python/stevedore dev-python/virtualenv-clone
build @ dev-python/distribute
"""

configure = lambda: ""
