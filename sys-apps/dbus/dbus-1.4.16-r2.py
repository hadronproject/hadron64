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
    #autoreconf("-vif")
    conf("--with-xml=expat",
        "--with-system-pid-file=/var/run/dbus.pid",
        "--with-system-socket=/var/run/dbus/system_bus_socket",
        "--with-session-socket-dir=/tmp",
        "--with-dbus-user=81",
        "--libexecdir=/usr/lib/dbus-1.0",
        "--disable-selinux",
        "--disable-tests",
        "--disable-doxygen-docs",
        "--disable-xml-docs",
        "--enable-shared",
        config_with("X", "x"),
        config_enable("debug", "verbose-mode"),
        config_enable("debug", "asserts"),
        config_enable("static-libs", "static"))

def build():
    make()
    make("-C tools dbus-launch")

def install():
    raw_install('DESTDIR=%s' % install_dir)


    for dirpath in ('/var/run/dbus', '/var/lib/dbus',
            '/usr/share/dbus-1/services',
            '/usr/share/dbus-1/system-services',
            '/etc/dbus-1/session.d',
            '/etc/dbus-1/system.d'):
        makedirs(dirpath)
    setowner("81:81", "%s/var/run/dbus" % install_dir)

    if opt("X"):
        makedirs("/etc/X11/xinit/xinitrc.d")
        insexe("%s/30-dbus" % filesdir, "/etc/X11/xinit/xinitrc.d/30-dbus")

    insexe("%s/dbus" % filesdir, "/etc/rc.d/dbus")

    sed("-i -e 's|<user>81</user>|<user>dbus</user>|' %s/etc/dbus-1/system.conf" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "HACKING", "NEWS",
            "README", "doc/TODO", "doc/*.txt")

def post_install():
    #FIXME: Python Python Python
    system("getent group 81 >/dev/null && userdel messagebus >/dev/null || true")
    system("getent group dbus >/dev/null || groupadd -g 81 dbus")
    system("getent passwd dbus >/dev/null || useradd -c 'System message bus' -u 81 -g dbus -d '/' -s /bin/false dbus")
    system("passwd -l dbus &>/dev/null")
    system("dbus-uuidgen --ensure")

    notify("If somehow you're installing DBus first time, don't forget to add in DAEMONS section of rc.conf")
