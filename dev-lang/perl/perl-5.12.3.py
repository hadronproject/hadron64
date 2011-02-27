metadata = """
summary @ A highly capable, feature-rich programming language
homepage @ http://www.perl.org
license @ PerlArtistic GPL-1 GPL-2 GPL-3
src_url @ http://www.cpan.org/src/5.0/$name-$version.tar.gz
options @ berkdb build debug doc gdbm ithreads
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

    system("./Configure",
    "-des",
    "-Duseshrplib",
    "-Doptimize='%s'" % get_env('CFLAGS'),
    "-Dldflags='%s'" % get_env('LDFLAGS'),
    "-Dprefix=/usr",
    "-Dinstallprefix=%s/usr" % install_dir,
    "-Dvenderprefix=/usr",
    "-Dprivlib=/usr/share/perl5/core_perl",
    "-Darchlib=/usr/lib/perl5/core_perl",
    "-Dsitelib=/usr/share/perl5/site_perl",
    "-Dsitearch=/usr/lib/perl5/site_perl",
    "-Dvendorlib=/usr/share/perl5/vendor_perl", 
    "-Dvendorarch=/usr/lib/perl5/vendor_perl", 
    "-Dscriptdir=/usr/bin/core_perl",
    "-Dsitescript=/usr/bin/site_perl",
    "-Dvendorscript=/usr/bin/vendor_perl" 
    "-Dinc_version_list=none",
    "-Dcf_by='Hadron'",
    "-Dman1ext=1perl -Dman3ext=3perl")

