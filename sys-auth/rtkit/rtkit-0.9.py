metadata = """
summary @ Realtime Policy and Watchdog Daemon
homepage @ http://git.0pointer.de/?p=rtkit.git
license @ GPL + BSD
src_url @ http://0pointer.de/public/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-apps/dbus sys-auth/polkit sys-libs/libcap
"""

def prepare():
    patch(level=1)

def configure():
    autoreconf("-fi")
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    system("./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml")
    insfile("org.freedesktop.RealtimeKit1.xml", "/usr/share/dbus-1/interfaces/")

def post_install():
    system("groupadd rtkit &> /dev/null || true")
    system("useradd -d /var/run/rtkit -g rtkit -s /bin/false -m rtkit &> /dev/null || true")

    notify("To start using RealtimeKit, you need to ensure that the 'dbus' service is running. If it is already running, you need to reload it with '/etc/rc.d/dbus restart' command")
