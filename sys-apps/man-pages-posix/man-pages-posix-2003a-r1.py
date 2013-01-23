metadata = """
summary @ POSIX man-pages(0p, 1p, 3p)
homepage @ http://www.kernel.org/doc/man-pages/
license @ man-pages-posix
src_url @ http://hadronproject.org/distfiles/$fullname.tar.bz2
arch @ ~x86_64
"""

standard_procedure = False

srcdir = "man-pages-posix-2003-a"

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("man-pages-*.Announce", "README", "Changes*")
