metadata = """
summary @ Pluggable Authentication Modules
homepage @ http://www.kernel.org/pub/linux/libs/pam/
license @ GPL-2
src_url @ https://fedorahosted.org/releases/l/i/linux-pam/Linux-PAM-$version.tar.bz2
arch @ ~x86_64
options @ berkdb cracklib debug nls nis
"""

depends = """
runtime @ sys-libs/glibc sys-devel/flex
"""

opt_runtime = """
cracklib @ sys-libs/cracklib
berkdb @ sys-libs/db
"""

def configure():
    cd("../Linux-PAM-%s" % raw_version)
    conf("--enable-dependency-tracking",
            "--enable-shared",
            config_enable("nls"),
            config_enable("nis"),
            config_enable("debug"),
            config_enable("berkdb", "db"),
            config_enable("cracklib"),
            "--disable-prelude")
    patch()

build = lambda: (cd("../Linux-PAM-%s" % raw_version), make())

def install():
    cd("../Linux-PAM-%s" % raw_version)
    raw_install("DESTDIR=%s SCONFIGDIR=/etc/security" % install_dir)
    insfile("%s/other" % filesdir, "/etc/pam.d/other")

    insdoc("CHANGELOG", "ChangeLog", "README", "AUTHORS", "Copyright", "NEWS")

    setmod("4755", "%s/sbin/unix_chkpwd" % install_dir)

def post_install():
    notify("Some software with pre-loaded PAM libraries might experience")
    notify("warnings or failures related to missing symbols and/or versions")
    notify("after any update. While unfortunate this is a limit of the")
    notify("implementation of PAM and the software, and it requires you to")
    notify("restart the software manually after the update.")
    notify("Alternatively, simply reboot your system.")
