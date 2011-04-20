metadata = """
summary @ The Berkeley DB embedded database system
homepage @ http://www.oracle.com/technology/software/products/berkeley-db/index.html
license @ OracleDB
src_url @ http://download.oracle.com/berkeley-db/$fullname.tar.gz
arch @ ~x86
"""

def configure():
    cd("build_unix")
    conf("--enable-compat185",
        "--enable-shared", 
        "--enable-static", 
        "--enable-cxx", 
        "--enable-dbm",
        run_dir=joinpath(build_dir, dist))

def build():
    make("LIBSO_LIBS=-lpthread")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    rmdir("/usr/docs")
    insfile(joinpath(build_dir, "LICENSE"), "/usr/share/licenses/db")
