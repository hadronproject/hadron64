metadata = """
summary @ A somewhat comprehensive collection of Linux man pages
homepage @ http://man7.org/linux/man-pages/index.html
license @ as-is GPL-2 BSD
src_url @ http://www.kernel.org/pub/linux/docs/man-pages/$fullname.tar.gz
arch @ ~x86_64
"""

#depends = """
#postmerge @ sys-apps/man-pages-posix
#"""

standard_procedure = False

def install():
    raw_install("DESTDIR=%s prefix=%s" % (install_dir, "/usr"))
    rmfile("/usr/share/man/man5/passwd.5")
    rmfile("/usr/share/man/man3/getspnam.3")
    insdoc("man-pages-*.Announce", "README", "Changes*")
