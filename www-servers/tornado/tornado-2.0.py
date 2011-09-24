metadata = """
summary @ Scalable, non-blocking web server and tools
homepage @ http://www.tornadoweb.org/ http://pypi.python.org/pypi/tornado
license @ Apache-2.0
src_url @ http://github.com/downloads/facebook/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
common @ dev-python/pycurl
"""

get("python_utils")

standard_procedure = False

def install():
    python_utils_install()

