metadata = """
summary @ Filter that can be run between an arbitrary application and a UTF-8 terminal emulator
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/luit-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libfontenc
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
