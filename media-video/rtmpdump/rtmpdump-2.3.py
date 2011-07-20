metadata = """
summary @ A tool to download rtmp streams 
homepage @ http://rtmpdump.mplayerhq.hu/ 
license @ LGPL 
src_url @ http://rtmpdump.mplayerhq.hu/download/$name-$version.tgz 
arch @ ~x86
"""

depends = """
runtime @ dev-libs/openssl
"""

def configure():
	system("sed -i 's/^install_so.0:.*/& install_base/' librtmp/Makefile")
	pass

def build():
	pass

def install():
	raw_install("prefix=/usr MANDIR=%s/usr/share/man DESTDIR=%s" % (install_dir, install_dir))

	insdoc("README", "ChangeLog")

