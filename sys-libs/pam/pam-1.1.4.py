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
    raw_configure("--disable-prelude",
            "--disable-dependency-tracking",
            "--enable-audit",
            config_enable("debug"),
            config_enable("cracklib"),
            config_enable("berkdb", "db"),
            "--enable-nls",
            "--enable-securedir=/lib/security",
            "--enable-isadir=/lib/security")

def install():
    raw_install("INSTALL=/bin/install DESTDIR=%s" % install_dir)

    insfile("%s/other" % filesdir, "/etc/pam.d/other")
    
    insdoc("CHANGELOG", "ChangeLog", "README", "AUTHORS", "Copyright", "NEWS")

def post_install():
    system("/sbin/ldconfig -r /")
    system("chmod +s /sbin/unix_chkpwd")
    notify("Some software with pre-loaded PAM libraries might experience \
warnings or failures related to missing symbols and/or versions \
after any update. While unfortunate this is a limit of the \
implementation of PAM and the software, and it requires you to \
restart the software manually after the update. \
Alternatively, simply reboot your system.")
