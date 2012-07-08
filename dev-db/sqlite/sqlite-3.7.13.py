metadata = """
summary @ A C library that implements an SQL database engine
homepage @ http://www.sqlite.org
license @ as-is
src_url @ http://www.sqlite.org/sqlite-autoconf-3071300.tar.gz
arch @ ~x86_64
"""
srcdir="sqlite-autoconf-3071300"

depends = """
build @ sys-libs/readline
"""

def configure():
    append_cflags("-DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 \
            -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_SECURE_DELETE")
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insfile("%s/LICENSE" % filesdir, "/usr/share/doc/sqlite/LICENSE")
