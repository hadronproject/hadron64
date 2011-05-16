metadata = """
summary @ Freedesktop.org message bus system
homepage @ http://www.freedesktop.org/Software/dbus
license @ GPL-2
src_url @ http://dbus.freedesktop.org/releases/$name/$name-$version.tar.gz
arch @ ~x86
"""

depends = """
build @ x11-libs/libX11 dev-libs/expat sys-libs/libcap
runtime @ x11-libs/libX11 dev-libs/expat sys-libs/libcap
"""

def configure():
    autoreconf("-vif")
    conf("--with-xml=expat \
            --with-system-pid-file=/var/run/dbus/pid \
            --with-system-socket=/var/run/dbus/system_bus_socket \
            --with-session-socket-dir=/tmp \
            --with-dbus-user=messagebus \
            --disable-selinux \
            --disable-static \
            --disable-tests \
            --disable-asserts \
            --disable-doxygen-docs \
            --disable-xml-docs")

def install():
    raw_install('DESTDIR=%s' % install_dir)

    for dirpath in ('/var/run/dbus', '/var/lib/dbus', 
            '/usr/share/dbus-1/services'):
        makedirs(dirpath)

    makedirs("/etc/X11/xinit/xinitrc.d")

    insexe("%s/30-dbus" % filesdir, "/etc/X11/xinit/xinitrc.d/30-dbus")

    insdoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", 
            "README", "doc/TODO", "doc/*.txt")
