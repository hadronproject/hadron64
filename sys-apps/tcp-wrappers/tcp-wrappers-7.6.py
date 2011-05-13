metadata = """
summary @ Monitors and Controls incoming TCP connections
homepage @ ftp://ftp.porcupine.org/pub/security/index.html
license @ custom
src_url @ ftp://ftp.porcupine.org/pub/security/tcp_wrappers_$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash
"""

srcdir = "tcp_wrappers_%s" % version

def prepare():
	patch("shared_lib_plus_plus-1.patch", level=1)
	patch("01_all_redhat-bug11881.patch", level=1)
	patch("04_all_fixgethostbyname.patch", level=1)
	patch("07_all_sig.patch", level=1)
	patch("09_all_gcc-3.4.patch", level=1)
	patch("10_all_more-headers.patch", level=1)
	patch("02_all_redhat-bug17795.patch")
	patch("03_all_wildcard.patch")
	patch("11_inet6_fixes.patch")
	patch("tcp-wrappers-7.6-ipv6-1.14.patch", level=2)

def build():
	make('REAL_DAEMON_DIR=/usr/sbin STYLE=-DPROCESS_OPTIONS linux')

def install():
    for d in ('include', 'lib' ,'sbin'):
        makedirs("/usr/"+d)
        
    for m in ('3','5','8'):
        makedirs("/usr/share/man/man"+m)
        
    raw_install("DESTDIR=%s" % install_dir)
    
    insfile("%s/hosts.allow" % filesdir, "/etc/hosts.allow")
    insfile("%s/hosts.deny" % filesdir, "/etc/hosts.deny")



