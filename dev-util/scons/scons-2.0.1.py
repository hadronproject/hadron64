metadata = """
summary @ Extensible Python-based build utility
homepage @ http://scons.org
license @ MIT
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ <dev-lang/python-3
build @ <dev-lang/python-3
"""

get("python_utils")

standard_procedure = False

def install():
    python_utils_install("--install-data=/usr/share",
            "--standard-lib")
