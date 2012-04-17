metadata = """
summary @ A network exploration tool and security/port scanner
homepage @ http://www.nmap.org
license @ GPL
src_url @ http://www.nmap.org/dist/$fullname.tar.bz2
arch @ ~x86
options @ gtk ssl lua
"""

depends = """
common @ dev-libs/pcre net-libs/libpcap
"""

opt_runtime = """
gtk @ dev-python/pygtk
lua @ dev-lang/lua
ssl @ dev-libs/openssl
"""

def configure():
    conf(
    config_with("lua", "liblua"),
    config_with("ssl", "openssl"),
    "--with-libdnet=included",
    "--without-zenmap")
    
def install():
	
	insdoc("CHANGELOG", "HACKING", "docs/README", "docs/*.txt")

	installd()
