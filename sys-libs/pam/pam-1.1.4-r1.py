metadata = """
summary @ Pluggable Authentication Modules
homepage @ http://www.kernel.org/pub/linux/libs/pam/
license @ PAM
src_url @ http://mirror.nexcess.net/kernel.org/linux/libs/pam/library/Linux-PAM-$version.tar.bz2
arch @ ~x86
options @ berkdb cracklib debug
"""

depends = """
runtime @ sys-libs/glibc sys-devel/flex
"""

opt_runtime = """
cracklib @ sys-libs/cracklib
berkdb @ sys-libs/db
"""

srcdir = "Linux-PAM-%s" % version

def configure():
    raw_configure(
            "--sysconfdir=/etc",
            "--libdir=/lib",
            "--disable-prelude",
            "--disable-dependency-tracking",
            "--enable-audit",
            config_enable("debug"),
            config_enable("cracklib"),
            config_enable("berkdb", "db"),
            "--enable-nls",
            "--enable-securedir=/lib/security",
            "--enable-isadir=/lib/security",
            "DESTDIR=%s" % install_dir)

def install():
    raw_install("INSTALL=/bin/install DESTDIR=%s" % install_dir)

    insfile("%s/other" % filesdir, "/etc/pam.d/other")
    
    insdoc("CHANGELOG", "ChangeLog", "README", "AUTHORS", "Copyright", "NEWS")

    cd("%s/lib/security" % install_dir)
    system("ln -s pam_unix.so pam_unix_acct.so")
    system("ln -s pam_unix.so pam_unix_auth.so")
    system("ln -s pam_unix.so pam_unix_passwd.so")
    system("ln -s pam_unix.so pam_unix_session.so")

    setmod("+x", "%s/sbin/unix_chkpwd" % install_dir)

def post_install():
    system("/sbin/ldconfig -r /")
    notify("Some software with pre-loaded PAM libraries might experience \
warnings or failures related to missing symbols and/or versions \
after any update. While unfortunate this is a limit of the \
implementation of PAM and the software, and it requires you to \
restart the software manually after the update. \
Alternatively, simply reboot your system.")
