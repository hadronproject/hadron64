metadata = """
summary @ ODBC is an open specification for providing application developers with a predictable API with which to access Data Sources
homepage @ http://www.unixodbc.org/
license @ GPL2 + LGPL2.1
src_url @ http://www.unixodbc.org/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/readline sys-devel/libtool
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

