metadata = """
summary @ Freedesktop.org message bus system
homepage @ http://www.freedesktop.org/Software/dbus
license @ GPL-2
src_url @ http://dbus.freedesktop.org/releases/$name/$name-$version.tar.gz
arch @ ~x86
options @ X static-libs debug
"""

depends = """
build @ dev-libs/expat sys-libs/libcap
runtime @ dev-libs/expat sys-libs/libcap
"""

opt_runtime = """
X @ x11-libs/libX11 x11-libs/libXt
"""

def configure():
    autoreconf("-vif")
    conf("--with-xml=expat \
            --with-system-pid-file=/var/run/dbus/pid \
            --with-system-socket=/var/run/dbus/system_bus_socket \
            --with-session-socket-dir=/tmp \
            --with-dbus-user=messagebus \
            --disable-selinux \
            --disable-tests \
            --disable-doxygen-docs \
            --disable-xml-docs",
            config_with("X", "x"),
            config_enable("debug", "verbose-mode"),
            config_enable("debug", "asserts"),
            config_enable("static-libs", "static"))

def install():
    raw_install('DESTDIR=%s' % install_dir)

    for dirpath in ('/var/run/dbus', '/var/lib/dbus',
            '/usr/share/dbus-1/services'):
        makedirs(dirpath)

    if opt("X"):
        makedirs("/etc/X11/xinit/xinitrc.d")
        insexe("%s/30-dbus" % filesdir, "/etc/X11/xinit/xinitrc.d/30-dbus")

    insexe("%s/dbus" % filesdir, "/etc/rc.d/dbus")

    insdoc("AUTHORS", "ChangeLog", "HACKING", "NEWS",
            "README", "doc/TODO", "doc/*.txt")

def post_install():
    system("groupadd messagebus &> /dev/null || true")
    system("useradd -d /var/run/dbus -g messagebus -s /bin/false messagebus &> /dev/null || true")

    notify("If somehow you're installing DBus first time, don't forget to add in DAEMONS section of rc.conf")
