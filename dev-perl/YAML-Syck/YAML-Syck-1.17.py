metadata = """
summary @ Fast, lightweight YAML loader and dumper
homepage @ http://search.cpan.org/dist/YAML-Syck
license @ MIT
src_url @ http://www.cpan.org/authors/id/A/AV/AVAR/$fullname.tar.gz
arch @ ~x86_64
"""

def configure():
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

def install():
    raw_install("DESTDIR=%s" % install_dir)
