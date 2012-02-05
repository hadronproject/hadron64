metadata = """
summary @ Programs for reading man pages.
license @ GPL
homepage @ http://primates.ximian.com/~flucifredi/man/
src_url @ http://primates.ximian.com/~flucifredi/man/man-1.6g.tar.gz
arch @ x86
"""

depends = """
runtime @ sys-devel/gettext sys-apps/groff
conflict @ sys-apps/man-db
"""

def configure():
    raw_configure("-default")

def install():
    raw_install("DESTDIR=%s" % install_dir)
