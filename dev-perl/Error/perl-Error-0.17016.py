metadata = """
summary @ Perl/CPAN Error module - Error/exception handling in an OO-ish way
homepage @ http://search.cpan.org/dist/${_realname}/
license @ PerlArtistic GPL
src_url @ http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/Error-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl
build @ dev-lang/perl
"""

srcdir = "Error-%s" % version

def configure():
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)
