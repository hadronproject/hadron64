metadata = """
summary @ Base class for creating POD filters and translators
homepage @ http://search.cpan.org/~marekr/$fullname/
license @ PerlArtistic GPL
src_url @ http://search.cpan.org/CPAN/authors/id/M/MA/MAREKR/Pod-Parser-1.38.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl
build @ dev-lang/perl
"""

def configure():
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)
