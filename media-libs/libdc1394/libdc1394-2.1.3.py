metadata = """
summary @ High level programming interface to control IEEE 1394 based cameras
homepage @ http://sourceforge.net/projects/libdc1394/
license @ LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/libdc1394/$name-$version.tar.gz
arch @ ~x86
options @ X doc
"""

depends = """
runtime @ sys-libs/libraw1394 dev-libs/libusb
"""

opt_runtime = """
X @ x11-libs/libSM x11-libs/libXv
doc @ app-doc/doxygen
"""

def configure():
    conf(
    "--disable-examples",
    config_enable("doc", "doxygen-html"),
    config_with("X", "x"))

def build():
    make()
    if opt("doc"):
        make("doc")

#doc problem install?
