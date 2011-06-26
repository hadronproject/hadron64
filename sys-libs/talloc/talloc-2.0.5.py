get("waf")

metadata = """
summary @ A hierarchical pool based memory allocator with destructors
homepage @ http://talloc.samba.org/
license @ GPL3
src_url @ http://samba.org/ftp/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/python
"""

def configure():
	raw_configure("--prefix=/usr --sysconfdir=/etc/samba \
	   --localstatedir=/var \
	   --enable-talloc-compat1")
