metadata = """
summary @ Python2 bindings for the cairo graphics library
homepage @ http://www.cairographics.org/pycairo
license @ LGPL + MPL
src_url @ http://cairographics.org/releases/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ x11-libs/cairo dev-lang/python
"""

def configure():
	system("JOBS=2 ./waf configure --prefix=/usr")
	system("JOBS=2 ./waf build")
	system("JOBS=2 ./waf install --destdir=%s" % install_dir)
	pass

def build():
	pass

def install():
	pass
