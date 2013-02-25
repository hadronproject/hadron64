metadata = """
summary @ Perl HTML parser class
homepage @ http://search.cpan.org/dist/HTML-Parser
license @ LGPL
src_url @ http://www.cpan.org/authors/id/G/GA/GAAS/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl dev-perl/HTML-Tagset
"""

def configure():
	pass

def build():
	system("perl Makefile.PL INSTALLDIRS=vendor")
	make()

def install():
	raw_install("DESTDIR=%s" % install_dir)

