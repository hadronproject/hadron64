metadata = """
summary @ The Apache Portable Runtime
homepage @ http://apr.apache.org/
license @ APACHE
src_url @ http://www.apache.org/dist/$name/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ >=sys-apps/util-linux-2.16
"""

def configure():
    export("apr_cv_accept4", "no")

    raw_configure("--prefix=/usr --includedir=/usr/include/apr-1",
            "--with-installbuilddir=/usr/share/apr-1/build",
            "--enable-nonportable-atomics",
            "--with-devrandom=/dev/urandom")

def install():
    raw_install("DESTDIR=%s" % install_dir)
