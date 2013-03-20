metadata = """
summary @ A fast and secure web browser and Internet suite
homepage @ http://www.opera.com/browser/
license @ custom:opera
src_url @ http://get.geo.opera.com/pub/opera/linux/1214/$fullname-1738.x86_64.linux.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gcc x11-libs/libXt x11-libs/libXext media-libs/freetype
"""

def configure():
	pass

def build():
	pass

def install():
	system("../opera-12.14-*/install --prefix /usr --repackage %s/usr" % install_dir)

def post_install():
	system("%s/post" % filesdir)

#hatali license + optional deps
