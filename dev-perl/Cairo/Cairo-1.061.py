metadata = """
summary @ Perl wrappers for cairo
homepage @ http://gtk2-perl.sourceforge.net/
license @ LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/gtk2-perl/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc dev-lang/perl x11-libs/cairo
build @ dev-perl/ExtUtils-Depends dev-perl/ExtUtils-PkgConfig
"""

def configure():
	pass

def build():
	system("perl Makefile.PL INSTALLDIRS=vendor")
	make()

def install():
	raw_install("DESTDIR=%s" % install_dir)

