metadata = """
summary @ A highly capable, feature-rich programming language
homepage @ http://www.perl.org
license @ PerlArtistic GPL-1 GPL-2 GPL-3
src_url @ http://www.cpan.org/src/5.0/$fullname.tar.gz
options @ berkdb gdbm ithreads debug
arch @ ~x86
"""

depends = """
runtime @ sys-apps/coreutils sys-apps/groff 
common @ sys-libs/zlib app-arch/bzip2
"""

opt_common = """
gdbm @ sys-libs/gdbm
berkdb @ sys-libs/db
"""

def prepare():
    # http://www.linuxfromscratch.org/lfs/view/stable/chapter06/perl.html
    sed('-i -e "s|BUILD_ZLIB\s*= True|BUILD_ZLIB = False|"           \
        -e "s|INCLUDE\s*= ./zlib-src|INCLUDE    = /usr/include|" \
        -e "s|LIB\s*= ./zlib-src|LIB        = /usr/lib|"         \
        cpan/Compress-Raw-Zlib/config.in')

def configure():
    myndbm='U'; mygdbm='U'; mydb='U'

    if opt("berkdb"): 
        mydb = 'D'
    
    if opt("gdbm"):
        mygdbm='D'
        myndbm='D'

    myconf = '-%si_ndbm -%si_gdbm  -%si_db' % (myndbm, mygdbm, mydb)

    if opt("ithreads"):
        myconf += " -Dusethreads"

    if opt("debug"):
        append_cflags("-g")
        myconf += " -DDEBUGGING"
    elif has_cflags("-g"):
        myconf += " -DDEBUGGING=-g"
    else:
        myconf += " -DDEBUGGING=none"

    system("sh Configure \
    -des \
    -Duseshrplib  \
    -Doptimize='%s' \
    -Dldflags='%s' \
    -Dlddlflags='-shared %s' \
    -Dprefix=/usr  \
    -Dsiteprefix=/usr \
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
    -Dlocincpth =' ' \
    -Duselargefiles \
    -Dd_semctl_semun \
    -Ud_csh \
    -Uusenm \
    -Dcf_by='Hadron' \
    -Dmyhostname='localhost' \
    -Dperladmin='root@localhost'\
    -Dpager='/usr/bin/less -isR' \
    -Dman1ext='1' -Dman3ext='3pm' %s" % (get_env("CFLAGS"), get_env("LDFLAGS"), get_env("LDFLAGS"), myconf))


build = lambda: (patch(level=1), make())

def install():
    # FIXME: remove all pod and packlist files from perl package or all perl packages??
    raw_install("DESTDIR=%s" % install_dir)
    makedirs("/etc/ld.so.conf.d")
    echo("/usr/lib/perl5/core_perl/CORE", "/etc/ld.so.conf.d/perl.conf")
