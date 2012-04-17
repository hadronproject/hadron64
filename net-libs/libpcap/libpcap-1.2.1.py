metadata = """
summary @ A system-independent interface for user-level packet capture
homepage @ http://www.tcpdump.org/
license @ BSD
src_url @ http://www.tcpdump.org/release/$fullname.tar.gz
arch @ ~x86
options @ ipv6 libnl
"""

depends = """
common @ sys-devel/flex
"""

opt_runtime = """
libnl @ dev-libs/libnl:1.1
"""
def configure():
    conf(
    config_enable("ipv6"),
    config_with("libnl"),
    "--with-libdnet=included",
    "--without-zenmap")

def build():
    make("all shared")
    
def install():
	
	insdoc("CREDITS", "CHANGES", "VERSION", "TODO", "README*")

	installd()
