metadata = """
summary @ Virtual Python Environment builder
homepage @ http://www.virtualenv.org/
license @ MIT
src_url @ http://pypi.python.org/packages/source/v/virtualenv/virtualenv-$version.tar.gz
arch @ ~x86
"""

# FIXME: Python3 support

get("python_utils")

configure = lambda: ""
