metadata = """
summary @ Advanced version control system
homepage @ http://subversion.apache.org/
license @ Subversion
src_url @ http://apache.mirror.rafal.ca/subversion/$fullname.tar.bz2
arch @ ~x86_64
options @ berkdb perl python sasl
"""

get("perl_utils")

depends = """
runtime @ net-libs/neon dev-libs/apr-util dev-libs/apr
build @ sys-devel/autoconf
"""

opt_build = """
python @ dev-lang/python
perl @ dev-lang/perl
#sqlite @ dev-db/sqlite
berkdb @ sys-libs/db
sasl @ dev-libs/cyrus-sasl
"""

def prepare():
    patch("subversion.rpath.fix.patch")
    autoreconf()

def configure():
    myconf = ""
    #if opt("sqlite"):
    #    myconf += "--with-sqlite=/usr "
    #else:
    #    myconf += "--without-sqlite "

    if opt("berkdb"):
        myconf += "--with-berkeley-db=:/usr/include/:/usr/lib:db-5.1 "
    else:
        myconf += "--without-berkeley-db "

    conf("--with-apr-util=/usr",
            "--with-apr=/usr",
            "--with-sqlite=/usr",
            config_with("berkdb", "berkeley-db"),
            config_enable("nls"),
            config_with("sasl"),
            "--with-ssl",
            "--with-neon=/usr",
            "--disable-javahl",
            "--without-gnome-keyring",
            "--without-kwallet",
            myconf)

def build():
    # build svn
    make()

    # python bindings
    if opt("python"):
        make("swig-py")

    if opt("perl"):
        make("swig-pl", j=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    if opt("python"):
        raw_install("DESTDIR=%s INSTALLDIRS=vendor" % install_dir, "install-swig-py")

    if opt("perl"):
        raw_install("DESTDIR=%s" % install_dir, "install-swig-pl")


    insexe("%s/svnserve" % filesdir, "/etc/rc.d/svnserve")
    insfile("%s/svn" % filesdir,  "/etc/xinetd.d/svn")
    insfile("%s/svnserve.conf" % filesdir,  "/etc/conf.d/svnserve")
    insexe("%s/svnmerge.py" % filesdir, "/usr/bin/svnmerge")

    insexe("%s/tools/client-side/bash_completion" % build_dir, \
            "/etc/bash_completion.d/subversion")

    fixlocalpod()
