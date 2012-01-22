metadata = """
summary @ A qt-based library that maps JSON data to QVariant objects 
homepage @ http://qjson.sourceforge.net 
license @ GPL-2 
src_url @ http://downloads.sourceforge.net/$name/$name-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/qt
build @ dev-util/cmake
"""

srcdir = "qjson"

get("cmake_utils")

prepare = lambda: makedirs("build")

configure = lambda: (cd("build"), cmake_conf())

install = (cd("build"), installd())
