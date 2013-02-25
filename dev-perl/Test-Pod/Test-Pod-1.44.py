metadata = """
summary @ Check for POD errors in files
homepage @ http://search.cpan.org/dist/Test-Pod
license @ GPL + PerlArtistic
src_url @ http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/$fullname.tar.gz
arch @ ~x86_64
"""

def configure():
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

def install():
    raw_install("DESTDIR=%s" % install_dir)
