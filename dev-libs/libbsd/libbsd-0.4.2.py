metadata = """
summary @ Provides useful functions commonly found on BSD systems like strlcpy()
homepage @ http://libbsd.freedesktop.org
license @ BSD BSD-2 BSD-4 ISC
src_url @ http://libbsd.freedesktop.org/releases/$fullname.tar.gz
options @ static-libs
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

def configure():
    conf("--disable-silent-rules",
            config_enable("static-libs", "static"))

install = lambda: installd()
