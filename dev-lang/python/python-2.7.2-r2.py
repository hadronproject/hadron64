metadata = """
summary @ A high-level scripting language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://www.python.org/ftp/python/$version/Python-$version.tar.bz2
options @ gdbm berkdb ncurses readline ssl xml ipv6 threads wide-unicode examples
arch @ ~x86
slot @ 2.7
"""
srcdir = "Python-2.7.2"

# TODO:
# tk support

depends = """
common @ dev-db/sqlite app-arch/bzip2 >=sys-libs/zlib-1.1.3 
dev-libs/libffi dev-util/intltool
"""

opt_common = """
berkdb @ sys-libs/db
gdbm @ sys-libs/gdbm
ncurses @ >=sys-libs/ncurses-5.2
    readline @ >=sys-libs/readline-4.1
ssl @ dev-libs/openssl
xml @ dev-libs/expat
"""

def prepare():
    sed('-i "/progname =/s/python/python2.7/" Python/pythonrun.c')
    patch(location="%s/2.7.2" % filesdir)
    for i in ('expat', 'zlib', '_ctypes/darwin', '_ctypes/libffi'):
        rmdir('Modules/%s' % i)

def configure():
    disable = []; dbmliborder=[]
    if not opt("berkdb") and not opt("gdbm"):
        disable.append("dbm")
    
    if not opt("gdbm"):
        disable.append("gdbm")
    else:
        dbmliborder.append("gdbm")
    if not opt("berkdb"):
        disable.append("_bsddb")
    else:
        dbmliborder.append("bdb")

    if not opt("ncurses"):
        disable.append("_curses _curses_panel")
    if not opt("readline"):
        disable.append("readline")
    if not opt("ssl"):
        export("PYTHON_DISABLE_SSL", "1")
    if not opt("xml"):
        warn("you have configured Python without XML support")
        warn("this is not recommended configuration as you")
        disable.append("_elementtree pyexpat")
    
    if disable:
        export("PYTHON_DISABLE_MODULES", " ".join(disable))

    raw_configure("--prefix=/usr",
            "--with-fpectl",
            "--infodir=/usr/share/info",
            "--mandir=/usr/share/man",
            "--with-libc=''",
            config_enable("ipv6"),
            config_with("threads"),
            "--enable-unicode=ucs4" if opt("wide-unicode") \
                    else "--enable-unicode=ucs2",
            "--with-dbmliborder=%s" % ":".join(dbmliborder),
            "--enable-shared",
            "--with-system-expat",
            "--with-system-ffi")

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s altinstall maninstall" % install_dir)

    libdir = "/usr/lib/python%s" % slot
    
    # the spec no support tk
    rmfile("/usr/bin/idle")
    for item in ('idlelib', 'lib-tk'):
        rmdir(joinpath(libdir, item))

    if not opt("berkdb"):
        rmfile(joinpath(libdir, "dbhash.py"))
        rmfile(joinpath(libdir, "test/test_bsddb*"))
        rmdir(joinpath(libdir, "bsddb"))

    if not opt("threads"):
        rmdir(joinpath(libdir, "multiprocessing"))

    if opt("examples"):
        makedirs("/usr/share/doc/%s" % fullname)
        copy("Tools", "/usr/share/doc/%s" % fullname)

    insdoc("LICENSE", "README")
    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
