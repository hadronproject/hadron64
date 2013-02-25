metadata = """
summary @ uncompile an rgb color-name database
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-proto/xproto
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
