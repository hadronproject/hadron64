metadata = """
summary @ GIT - the stupid content tracker, the revision control system heavily used by the Linux kernel team
homepage @ http://git-scm.com
license @ GPL-2
src_url @ http://git-core.googlecode.com/files/$fullname.tar.gz 
man(http://git-core.googlecode.com/files/git-manpages-$version.tar.gz)
options @ man python perl pcre subversion threads blksha1 bash-completion
arch @ ~x86
"""

depends = """
common @ dev-lang/perl dev-perl/Error net-misc/curl dev-libs/expat 
        dev-libs/openssl dev-libs/pcre
"""

standard_procedure = False

def build():
    myopts = [
            'NO_FINK=YesPlease NO_DARWIN_PORTS=YesPlease',
            'INSTALL=install TAR=tar',
            'SHELL_PATH=/bin/sh',
            'SANE_TOOL_PATH=',
            'NO_EXTERNAL_GREP=',
            'NO_TCLTK=YesPlease',
    ]

    if not opt("python"):
        myopts.append("NO_PYTHON=YesPlease")

    if not opt("perl"):
        myopts.append("NO_PERL=YesPlease")
    else:
        myopts.append("INSTALLDIRS=vendor")

    if not opt("subversion"):
        myopts.append("NO_SVN_TESTS=YesPlease")
    
    if opt("threads"):
        myopts.append("THREADED_DELTA_SEARCH=YesPlease")

    if opt("blksha1"):
        myopts.append("BLK_SHA1=YesPlease")
    
    if opt("pcre"):
        myopts.append("USE_LIBPCRE=yes")

    sed("-i -e '/\/usr\/local/s/BASIC_/#BASIC_/' Makefile")

    make('%s prefix=/usr CFLAGS="%s" LDFLAGS="%s" gitexecdir=/usr/lib/git-core all' \
            % (" ".join(myopts), get_env('CFLAGS'), get_env('LDFLAGS')))

def install():
    raw_install('prefix=/usr CFLAGS="%s" LDFLAGS="%s" gitexecdir=/usr/lib/git-core DESTDIR=%s' \
            % (get_env('CFLAGS'), get_env('LDFLAGS'), install_dir))

    makedirs("/etc/bash_completion.d/")
    insfile("./contrib/completion/git-completion.bash", "/etc/bash_completion.d/git")

    # git daemon script for ArchLinux
    insexe("%s/git-daemon" % filesdir, "/etc/rc.d/git-daemon")
    insfile("%s/git-daemon.conf" % filesdir, "/etc/conf.d/git-daemon.conf")

    if opt("man"):
        for mansect in ('man1', 'man5', 'man7'):
            for manpage in ls("%s/%s" % (dirname(build_dir, ignore_fix_target=True), mansect), ignore_fix_target=True):
                insfile("%s/%s/%s" % (dirname(build_dir, ignore_fix_target=True), mansect, manpage), \
                        "/usr/share/man/%s/%s" % (mansect, basename(manpage, ignore_fix_target=True)))
    
    insexe("contrib/fast-import/git-p4", "/usr/bin/git-p4")
    insexe("contrib/fast-import/import-tars.perl", "/usr/bin/import-tars")
    insexe("contrib/git-resurrect.sh", "/usr/bin/git-resurrect")

    for item in ls("contrib"):
        copy("contrib/%s" % item, "/usr/share/git/contrib/%s" % item)

    # this package has not cgi option
    rmdir("/usr/share/gitweb")

    if not opt("subversion"):
        rmdir("/usr/libexec/git-core/git-svn")
        rmdir("/usr/share/man/man1/git-svn.1*")

    if opt("bash-completion"):
        insfile("contrib/completion/git-completion.bash", "/etc/bash_completion.d/git-completion.bash")

    if opt("python") and opt("gtk"):
        insexe("contrib/gitview/gitview", "/usr/bin/gitview")
        insdoc("contrib/gitview/gitview.txt")
    rmdir("/usr/lib/perl5")
