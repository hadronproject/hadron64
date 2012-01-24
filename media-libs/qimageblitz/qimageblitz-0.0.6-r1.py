metadata = """
summary @ An interm image effect library
homepage @ http://sourceforge.net/projects/qimageblitz
license @ GPL-2
src_url @ http://download.kde.org/stable/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/qt   
build @	dev-util/cmake dev-util/pkg-config
"""

get("main/cmake_utils")

prepare = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir))
build = lambda: (cd("build"), make())
install = lambda: (cd("build"), installd())

