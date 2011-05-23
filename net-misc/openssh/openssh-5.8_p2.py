metadata = """
summary @ Free version of the SSH connectivity tools
homepage @ http://www.openssh.org/portable.html
license @ BSD
src_url @ ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/$name-5.8p2.tar.gz
arch @ ~x86
"""

srcdir = name+"-5.8p2"

depends = """
runtime @ sys-libs/glibc sys-apps/tcp-wrappers dev-libs/openssl dev-libs/libedit
"""

def configure():
    raw_configure("--prefix=/usr", 
    "--libexecdir=/usr/lib/ssh",
	"--sysconfdir=/etc/ssh --with-tcp-wrappers --with-privsep-user=nobody",
	"--with-md5-passwords --with-pam --with-mantype=man --mandir=/usr/share/man",
	"--with-xauth=/usr/bin/xauth --with-ssl-engine",
	"--with-libedit --disable-strip")


def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insexe("%s/sshd" % filesdir, "/etc/rc.d/sshd")
    insfile("%s/sshd.confd" % filesdir, "/etc/conf.d/sshd")
    insfile("%s/sshd.pam" % filesdir, "/etc/pam.d/sshd")
    insexe("%s/contrib/findssl.sh" % build_dir, "/usr/bin/findssl.sh")
    insexe("%s/contrib/ssh-copy-id" % build_dir, "/usr/bin/ssh-copy-id")
    insfile("%s/contrib/ssh-copy-id.1" % build_dir, "/usr/share/man/man1/ssh-copy-id.1")

    makedirs("/var/empty/sshd")

    insdoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
