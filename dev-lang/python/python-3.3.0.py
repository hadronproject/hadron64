metadata = """
summary @ A high-level scripting language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://www.python.org/ftp/python/$version/Python-$version.tar.xz
options @ gdbm ncurses readline ssl xml ipv6 threads wide-unicode examples
arch @ ~x86_64
slot @ 3.3
"""

srcdir = "Python-3.3.0"

# TODO:
# tk support

depends = """
common @ dev-db/sqlite app-arch/bzip2 >=sys-libs/zlib-1.1.3 
dev-libs/libffi dev-util/intltool
"""

opt_common = """
gdbm @ sys-libs/gdbm
ncurses @ >=sys-libs/ncurses-5.2
    readline @ >=sys-libs/readline-4.1
ssl @ dev-libs/openssl
xml @ dev-libs/expat
"""

def prepare():
    patch(location="%s/3.3.0" % filesdir)
    for i in ('expat', 'zlib', '_ctypes/darwin', '_ctypes/libffi'):
        rmdir('Modules/%s' % i)
    rmfile("Lib/distutils/command/*.exe")

def configure():
    disable = []; dbmliborder=[]
    
    if not opt("gdbm"):
        disable.append("gdbm")
    else:
        dbmliborder.append("gdbm")

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
            config_with("wide-unicode"),
            "--with-computed-gotos",
            "--enable-loadable-sqlite-extensions",
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
    
    # Fix collisions between different slots of Python.
    rmfile("/usr/bin/2to3")
    rmfile("/usr/bin/pydoc3")
    rmfile("/usr/bin/python3-config")
    rmfile("/usr/lib/pkgconfig/python3.pc")
    rmfile("/usr/lib/libpython3.so")
    rmfile("/usr/bin/python3")

    # the spec no support tk
    rmdir(joinpath(libdir, "tkinter"))
    rmdir(joinpath(libdir, "idlelib"))
    rmfile("/usr/bin/idle*")

    if not opt("threads"):
        rmdir(joinpath(libdir, "multiprocessing"))

    if opt("examples"):
        makedirs("/usr/share/doc/%s" % fullname)
        copy("Tools", "/usr/share/doc/%s" % fullname)

    insdoc("LICENSE", "README")
    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
