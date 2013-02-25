metadata = """
summary @ A programming environment providing object and heap memory sizing, profiling and analysis.
homepage @ http://http://guppy-pe.sourceforge.net
license @ MIT
src_url @ http://pypi.python.org/packages/source/g/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ <dev-lang/python-3
buile @ <dev-lang/python-3
"""

get("main/python_utils")

standard_procedure = False

def install():
    python_utils_install()
