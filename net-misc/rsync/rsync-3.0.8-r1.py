metadata = """
summary @ File transfer program to keep remote files into sync
homepage @ http://rsync.samba.org/
license @ GPL-3
src_url @ http://rsync.samba.org/ftp/rsync/src/rsync-3.0.8.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-apps/acl
"""

def configure():
    conf("--with-included-popt",
            "--enable-acl-support",
            "--enable-xattr-support")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insexe("%s/rsyncd"  % filesdir, "/etc/rc.d/rsyncd")
    insfile("%s/rsyncd.conf" % filesdir, "/etc/rsyncd.conf")
    insfile("%s/rsync.xinetd" % filesdir, "/etc/xinetd.d/rsync")
