metadata = """
summary @ X.Org Trap protocol headers
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.bz2
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
