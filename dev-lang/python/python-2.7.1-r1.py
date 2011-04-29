metadata = """
summary @ A high-level scripting language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://www.python.org/ftp/python/2.7.1/Python-2.7.1.tar.bz2 
arch @ ~x86
slot @ 2.7
"""
srcdir = "Python-2.7.1"

depends = """
runtime @ dev-db/sqlite dev-libs/expat sys-libs/gdbm
          dev-libs/openssl sys-libs/zlib app-arch/bzip2
"""

def configure():
    #export("OPT", "%s -fPIC -fwrapv" % get_env('CFLAGS'))
    export("OPT", get_env('CFLAGS'))
    raw_configure("--prefix=/usr", 
        "--enable-shared", 
        "--with-threads", 
        "--enable-ipv6", 
        "--enable-unicode=ucs4", 
        "--with-system-expat")

def install():
    raw_install("DESTDIR=%s altinstall maninstall" % install_dir)

    insdoc("LICENSE", "README")
    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
