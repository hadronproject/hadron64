metadata = """
summary @ Next generation of the Python. A high-level scripting language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://www.python.org/ftp/python/$version/Python-$version.tar.bz2
arch @ ~x86
slot @ 3.2
"""
srcdir = "Python-3.2.1"

depends = """
runtime @ dev-db/sqlite dev-libs/expat sys-libs/gdbm
          dev-libs/openssl sys-libs/zlib app-arch/bzip2
          dev-libs/libffi
"""

def configure():
    #export("OPT", "%s -fPIC -fwrapv" % get_env('CFLAGS'))
    for _dir in ('expat', 'zlib', '_ctypes/darwin', \
            '_ctypes/libffi'):
        if isdir("Modules/%s" % _dir):
            rmdir("Modules/%s" % _dir)

    export("OPT", get_env('CFLAGS'))
    raw_configure("--prefix=/usr",
        "--enable-shared",
        "--with-threads",
        "--with-computed-gotos",
        "--enable-ipv6",
        "--with-wide-unicode",
        "--with-system-ffi",
        "--with-system-expat")

def install():
    raw_install("DESTDIR=%s altinstall maninstall" % install_dir)

    insdoc("LICENSE", "README")
    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
