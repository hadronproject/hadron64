metadata = """
summary @ GIT - the stupid content tracker, the revision control system heavily used by the Linux kernel team
homepage @ http://git-scm.com
license @ GPL-2
src_url @ http://kernel.org/pub/software/scm/git/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl dev-perl/Error
build @ dev-lang/perl dev-perl/Error
"""

def build():
    make("gitexecdir=/usr/lib/git-core")

def install():
    raw_install("gitexecdir=/usr/lib/git-core \
            NO_CROSS_DIRECTORY_HARDLINKS=1 INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

    makedirs("/etc/bash_completion.d/")
    insfile("./contrib/completion/git-completion.bash", "/etc/bash_completion.d/git")
    
    # git daemon script for ArchLinux
    insexe("%s/git-daemon" % filesdir, "/etc/rc.d/git-daemon")
    insfile("%s/git-daemon.conf" % filesdir, "/etc/conf.d/git-daemon.conf")

