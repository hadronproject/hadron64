metadata = """
summary @ The Apache Portable Runtime
homepage @ http://apr.apache.org/
license @ APACHE
src_url @ http://www.apache.org/dist/apr/$fullname.tar.bz2
arch @ ~x86_64
options @ berkdb sqlite3
"""

depends = """
runtime @ dev-libs/apr dev-libs/expat
"""

opt_runtime = """
berkdb @ >=sys-libs/db-4
sqlite3 @ dev-db/sqlite
"""

def configure():
    myconf = ""

    if opt("berkdb"):
        myconf += "--with-berkeley-db=/usr"
    else:
        myconf += "--without-berkeley-db"

    # Hadron does not involve sqlite:2 series for now.
    # config_with("sqlite", "sqlite2"),
    conf("--with-apr=/usr",
            "--without-pgsql --without-mysql",
            config_with("sqlite3", "sqlite3"),
            "--with-gdbm=/usr", "--without-ldap",
            myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)
