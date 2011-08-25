metadata = """
summary @ A GTK+ based IRC client
homepage @ http://www.xchat.org/
license @ GPL
src_url @ http://www.xchat.org/files/source/2.8/$fullname.tar.bz2
arch @ ~x86
options @ gtk ssl perl python tcl dbus spell libnotify ipv6 fastscroll mmx
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_runtime = """
gtk @ x11-libs/gtk+
ssl @ dev-libs/openssl
dbus @ dev-libs/dbus-glib
spell @ app-text/gtkspell
libnotify @ x11-libs/libnotify
"""

opt_build = """
tcl @ dev-lang/tcl
python @ dev-lang/python
perl @ dev-lang/perl
"""

def configure():
    conf(
    config_enable("mmx"),
config_enable("perl"),
    config_enable("dbus"),
    config_enable("python"),
    config_enable("spell"),
    config_enable("spell", "gtkspell"),
    config_enable("tcl"),
    config_enable("gtk", "gtkfe"),
    config_enable("fastscroll", "xft"),
    config_enable("ssl", "openssl"),
    config_enable("dbus"),
    config_enable("ipv6"),
    "--enable-shm")

def install():
    raw_install("DESTDIR=%s" % install_dir)
