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

#get("cmake_utils")

#prepare = lambda: makedirs("build")
#configure = lambda: (cd("build"), cmake_conf())
#install = lambda: (cd("build"), installd())

def configure():
    pass

def build():
    makedirs("build")
    cd("build")
    system("cmake ../ \
            -DCMAKE_BUILD_TYPE=Release \
            -DCMAKE_INSTALL_PREFIX=/usr")

def install():
    cd("build")
    installd()

