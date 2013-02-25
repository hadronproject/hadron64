metadata = """
summary @ Data tables useful in parsing HTML
homepage @ http://search.cpan.org/dist/HTML-Tagset
license @ LGPL
src_url @ http://www.cpan.org/authors/id/P/PE/PETDANCE/$fullname.tar.gz
arch @ ~x86_64
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

