metadata = """
summary @ Library for generating character- and string-glyphs from Adobe Type 1 fonts 
homepage @ http://www.ibiblio.org/pub/Linux/libs/graphics/!INDEX.html 
license @ GPL 
src_url @ http://www.ibiblio.org/pub/Linux/libs/graphics/$name-$version.tar.gz  
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXaw
"""

def build():
	make("without_doc")

def install():
	raw_install("DESTDIR=%s" % install_dir)

