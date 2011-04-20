metadata = """
summary @ Pluggable Authentication Modules
homepage @ http://www.kernel.org/pub/linux/libs/pam/
license @ PAM
src_url @ http://www.kernel.org/pub/linux/libs/pam/library/Linux-PAM-$version.tar.bz2
arch @ ~x86
"""

srcdir = "Linux-PAM-%s" % version

def configure():
    append_cflags("-fPIC -D_GNU_SOURCE")
    libtoolize("-f")
    autoreconf()
    raw_configure("--disable-prelude",
            "--disable-dependency-tracking",
            "--enable-audit",
            "--enable-db=no",
            "--enable-nls",
            "--enable-securedir=/lib/security",
            "--enable-isadir=/lib/security")

def install():
    raw_install("DESTDIR=%s" % install_dir)
