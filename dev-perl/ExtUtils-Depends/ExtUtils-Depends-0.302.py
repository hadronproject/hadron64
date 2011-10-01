metadata = """
summary @ The Perl depends module
homepage @ http://gtk2-perl.sourceforge.net/
license @ PerlArtistic
src_url @ http://downloads.sourceforge.net/sourceforge/gtk2-perl/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl
"""

def configure():
	pass

def build():
	system("perl Makefile.PL INSTALLDIRS=vendor")
	make()

def install():
	raw_install("DESTDIR=%s" % install_dir)

