metadata = """
summary @ A mouse server for the console and xterm
homepage @ http://www.nico.schottelius.org/software/gpm/
license @ GPL
src_url @ http://www.nico.schottelius.org/software/gpm/archives/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/ncurses app-shells/bash
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("BUGS", "Changes", "README", "TODO")

    insexe("%s/gpm" % filesdir, "/etc/rc.d/gpm")
    insfile("%s/gpm.confd" % filesdir, "/etc/conf.d/gpm")
    insexe("%s/gpm.sh" % filesdir, "/etc/profile.d/gpm.sh")

    cd("%s/usr/lib" % install_dir)
    system("ln -s libgpm.so.2.* libgpm.so")
