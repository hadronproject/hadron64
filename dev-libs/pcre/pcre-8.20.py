metadata = """
summary @ A library that implements Perl 5-style regular expressions
homepage @ http://www.pcre.org
license @ BSD
src_url @ ftp://ftp.csx.cam.ac.uk/pub/software/programming/$name/$fullname.tar.bz2
arch @ ~x86
"""

def configure():
    conf("--enable-utf8",
        "--enable-unicode-properties", 
        "--enable-unicode-properties")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    #makedirs("lib")
    #move("%s/usr/lib/libpcre.so.*" % install_dir, "lib/")
    #makesym("%s/lib/libpcre.so.0" % install_dir, "usr/lib/libpcre.so")
