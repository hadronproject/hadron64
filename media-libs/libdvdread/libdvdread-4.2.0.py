metadata = """
summary @ Provides a simple foundation for reading DVD video disks
homepage @ http://www.mplayerhq.hu/MPlayer/releases/dvdnav/
license @ GPL
src_url @ http://dvdnav.mplayerhq.hu/releases/$fullname.tar.bz2
arch @ ~x86_64
options @ css
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_build = """
css @ media-libs/libdvdcss
"""

def configure():
    system("./autogen.sh --prefix=/usr")
    pass

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "DEVELOPMENT-POLICY.txt", "ChangeLog", "TODO", "README")
