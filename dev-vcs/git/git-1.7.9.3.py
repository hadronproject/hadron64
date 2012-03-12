metadata = """
summary @ GIT - the stupid content tracker, the revision control system heavily used by the Linux kernel team
homepage @ http://git-scm.com
license @ GPL-2
src_url @ http://git-core.googlecode.com/files/$fullname.tar.gz 
man(http://git-core.googlecode.com/files/git-manpages-$version.tar.gz)
options @ man
arch @ ~x86
"""

depends = """
common @ dev-lang/perl dev-perl/Error net-misc/curl dev-libs/expat 
        dev-libs/openssl dev-libs/pcre
"""

standard_procedure = False

def build():
    make('prefix=/usr CFLAGS="%s" LDFLAGS="%s" USE_LIBPCRE=1 NO_CROSS_DIRECTORY_HARDLINKS=1 \
            gitexecdir=/usr/lib/git-core' % (get_env('CFLAGS'), get_env('LDFLAGS')))

def install():
    raw_install('prefix=/usr CFLAGS="%s" LDFLAGS="%s" USE_LIBPCRE=1 \
            gitexecdir=/usr/lib/git-core NO_CROSS_DIRECTORY_HARDLINKS=1 \
            INSTALLDIRS=vendor DESTDIR=%s' % (get_env('CFLAGS'), get_env('LDFLAGS'), install_dir))

    makedirs("/etc/bash_completion.d/")
    insfile("./contrib/completion/git-completion.bash", "/etc/bash_completion.d/git")

    # git daemon script for ArchLinux
    insexe("%s/git-daemon" % filesdir, "/etc/rc.d/git-daemon")
    insfile("%s/git-daemon.conf" % filesdir, "/etc/conf.d/git-daemon.conf")

    if opt("man"):
        for mansect in ('man1', 'man5', 'man7'):
            for manpage in ls("%s/%s" % (dirname(build_dir), mansect)):
                insfile("%s/%s/%s" % (dirname(build_dir), mansect, manpage), \
                        "/usr/share/man/%s/%s" % (mansect, basename(manpage)))
    
    rmdir("/usr/lib/perl5")
