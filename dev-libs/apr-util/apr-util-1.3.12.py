metadata = """
summary @ The Apache Portable Runtime
homepage @ http://apr.apache.org/
license @ APACHE
src_url @ http://www.apache.org/dist/apr/$fullname.tar.bz2
arch @ ~x86
options @ berkdb sqlite sqlite3
"""

depends = """
runtime @ dev-libs/apr dev-libs/expat
"""

opt_runtime = """
berkdb @ >=sys-libs/db-4
sqlite @ dev-db/sqlite:2
sqlite3 @ dev-db/sqlite:3
"""

def configure():
    myconf = ""

    if opt("berkdb"):
        myconf += "--with-berkeley-db=/usr"
    else:
        myconf += "--without-berkeley-db"

    conf("--with-apr=/usr",
            "--without-pgsql --without-mysql",
            config_with("sqlite", "sqlite2"),
            config_with("sqlite3", "sqlite3"),
            "--with-gdbm=/usr", "--without-ldap",
            myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)
