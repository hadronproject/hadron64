metadata = """
summary @ A highly capable, feature-rich programming language
homepage @ http://www.perl.org
license @ PerlArtistic GPL-1 GPL-2 GPL-3
src_url @ http://www.cpan.org/src/5.0/$fullname.tar.gz
options @ berkdb gdbm ithreads
arch @ ~x86
"""

# FIXME: build, doc and debug options will be added.

depends = """
runtime @ sys-libs/gdbm sys-libs/glibc sys-apps/coreutils
        sys-apps/groff sys-libs/zlib app-shells/bash
"""

def configure():
    myndbm='U'; mygdbm='U'; mydb='U'

    if opt("berkdb"): mydb = 'D'
    if opt("gdbm"):
        mygdbm='D'
        myndbm='D'

    myconf = '-%si_ndbm" "-%si_gdbm" "-%si_db' % (myndbm, mygdbm, mydb)

    if opt("ithreads"):
        myconf += "-Dusethreads"

    system("sh Configure \
    -des -Duseshrplib  -Doptimize='%s' -Dldflags='%s' \
    -Dlddlflags='-shared %s' \
    -Dprefix=/usr  \
    -Dvendorprefix=/usr \
    -Dprivlib=/usr/share/perl5/core_perl \
    -Darchlib=/usr/lib/perl5/core_perl \
    -Dsitelib=/usr/share/perl5/site_perl \
    -Dsitearch=/usr/lib/perl5/site_perl \
    -Dvendorlib=/usr/share/perl5/vendor_perl \
    -Dvendorarch=/usr/lib/perl5/vendor_perl \
    -Dscriptdir=/usr/bin/core_perl \
    -Dsitescript=/usr/bin/site_perl \
    -Dvendorscript=/usr/bin/vendor_perl \
    -Dinc_version_list=none \
    -Dcf_by='Hadron' \
    -Dman1ext=1perl -Dman3ext=3perl" % (get_env("CFLAGS"), get_env("LDFLAGS"), get_env("LDFLAGS")))

def build():
    patch(level=1)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
