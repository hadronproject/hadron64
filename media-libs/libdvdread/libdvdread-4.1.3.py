metadata = """
summary @ Provides a simple foundation for reading DVD video disks
homepage @ http://www.mplayerhq.hu/MPlayer/releases/dvdnav/
license @ GPL
src_url @ http://www.mplayerhq.hu/MPlayer/releases/dvdnav/$fullname.tar.bz2
arch @ ~x86
options @ css
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_build = """
css @ media-libs/libdvdcss
"""

def prepare():
    patch(level=1)

def configure():
    system("./autogen.sh --prefix=/usr")
    pass

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "DEVELOPMENT-POLICY.txt", "ChangeLog", "TODO", "README")
