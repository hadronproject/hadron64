metadata = """
summary @ Freedesktop.org message bus system
homepage @ http://www.freedesktop.org/Software/dbus
license @ GPL-2
src_url @ http://dbus.freedesktop.org/releases/$name/$name-$version.tar.gz
options @ debug doc selinux static-libs test X
"""

def configure():
    conf(config_with("X", "x"),
        config_enable("debug", "verbose-mode"),
        config_enable("selinux"),
        config_enable("selinux", "libaudit"),
        config_enable("static-libs", "static"),
        "--enable-shared",
        "--with-xml=expat",
        "--with-system-pid-file=/var/run/dbus.pid",
        "--with-system-socket=/var/run/dbus/system_bus_socket",
        "--with-session-socket-dir=/tmp",
        "--with-dbus-user=messagebus",
        "--localstatedir=/var")

def install():
    raw_install('DESTDIR=%s' % install_dir)

    for dirpath in ('/var/run/dbus', '/var/lib/dbus', 
            '/usr/share/dbus-1/services'):
        makedirs(dirpath)

    insdoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", 
            "README", "doc/TODO", "doc/*.txt")
