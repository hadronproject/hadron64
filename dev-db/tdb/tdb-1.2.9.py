get("main/waf")

metadata = """
summary @ A Trivia Database similar to GDBM but allows simultaneous commits
homepage @ http://tdb.samba.org/
license @ GPL3
src_url @ http://samba.org/ftp/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-libs/libxslt
"""

def configure():
    raw_configure("--prefix=/usr \
            --localstatedir=/var \
            --sysconfdir=/etc/samba")
