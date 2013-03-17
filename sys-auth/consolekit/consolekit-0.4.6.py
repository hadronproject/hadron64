metadata = """
summary @ Framework for defining and tracking users, login sessions and seats.
homepage @ http://www.freedesktop.org/wiki/Software/ConsoleKit
license @ GPL
src_url @ http://anduin.linuxfromscratch.org/sources/BLFS/svn/c/ConsoleKit-$version.tar.xz
options @ pam
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/pam sys-auth/polkit sys-libs/zlib x11-libs/libX11 sys-apps/dbus
"""

srcdir = "ConsoleKit-%s" % version

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--localstatedir=/var",
            "--libexecdir=/usr/lib/ConsoleKit",
            config_enable("pam", "pam-module"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insexe("%s/pam-foreground-compat.ck" % filesdir,
            "/usr/lib/ConsoleKit/run-session.d/pam-foreground-compat.ck")

    insfile("%s/consolekit.logrotate" % filesdir,
            "/etc/logrotate.d/consolekit/consolekit.logrotate")
    if opt("pam"):
        insfile("%s/system-session" % filesdir, "/etc/pam.d/system-session")
