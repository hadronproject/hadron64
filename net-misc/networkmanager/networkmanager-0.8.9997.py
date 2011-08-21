metadata = """
summary @ Network Management daemon
homepage @ http://www.gnome.org/projects/NetworkManager/
license @ GPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/NetworkManager/0.8/NetworkManager-$version.tar.bz2
arch @ ~x86
options @ gnutls dhcpcd introspection
"""

depends = """
runtime @ sys-apps/dbus dev-libs/dbus-glib net-wireless/wireless_tools sys-fs/udev sys-libs/glib
    sys-auth/polkit dev-libs/libnl:1.1 net-wireless/wpa_supplicant[dbus] sys-auth/consolekit net-dialup/ppp
build @ dev-util/pkg-config dev-util/intltool sys-devel/gettext
"""

opt_runtime = """
gnutls @ dev-libs/libgcrypt net-libs/gnutls
dhcpcd @ net-misc/dhcpcd
introspection @ dev-libs/gobject-introspection
"""

srcdir = "NetworkManager-" + version

def prepare():
    patch(level=1)

def configure():

    myconf = ""
#    if opt("gnutls"):
    myconf += " --with-crypto=gnutls"
#    else:
#        myconf += " --with-crypto=nss "
            
    conf(
    "--disable-more-warnings",
    "--disable-static",
    "--localstatedir=/var",
    "--with-distro=arch",
    "--with-dbus-sys-dir=/etc/dbus-1/system.d",
    "--with-udev-dir=/lib/udev",
    "--with-dhclient=/usr/sbin/dhclient",
    "--with-dhcpcd=/sbin/dhcpcd",
    "--with-iptables=/usr/sbin/iptables",
    "--with-systemdsystemunitdir=/lib/systemd/system",
    config_with("dhcpcd"),
    config_enable("introspection"), myconf)

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/NetworkManager.conf" % filesdir, "/etc/NetworkManager/NetworkManager.conf")
