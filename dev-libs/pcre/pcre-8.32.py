metadata = """
summary @ A library that implements Perl 5-style regular expressions
homepage @ http://www.pcre.org
license @ BSD
src_url @ ftp://ftp.csx.cam.ac.uk/pub/software/programming/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

def configure():
    conf("--enable-utf8",
        "--enable-pcre16",
        "--enable-pcre32",
        "--enable-jit",
        "--enable-unicode-properties")

def build():
    append_cflags("-fPIC")
    make()

def install():
    raw_install("DESTDIR=%s install" % install_dir)
