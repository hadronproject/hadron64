metadata =  """
summary @ X.org font alias files
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/font/$fullname.tar.bz2
arch @ ~x86
"""

def configure():
    conf("--with-fontrootdir=/usr/share/fonts")

def install():
    raw_install("DESTDIR=%s" % install_dir)
