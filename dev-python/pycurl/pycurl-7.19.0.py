metadata = """
summary @ A Python interface to libcurl
homepage @ http://pycurl.sourceforge.net
license @ GPL
src_url @ http://pycurl.sourceforge.net/download/$fullname.tar.gz
arch @ ~x86
"""

depends = """
common @ dev-lang/python net-misc/curl
"""

get("python_utils")

standard_procedure = False

def install():
    python_utils_install("--curl-config=/usr/bin/curl-config")
