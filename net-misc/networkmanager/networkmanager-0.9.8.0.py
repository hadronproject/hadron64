metadata = """
summary @ Network Management daemon
homepage @ http://www.gnome.org/projects/NetworkManager/
license @ GPL
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/NetworkManager/0.9/NetworkManager-$version.tar.xz
arch @ ~x86_64
options @ gnutls dhcpcd introspection
"""

depends = """
common @ >=sys-apps/dbus-1.2 dev-libs/dbus-glib net-wireless/wireless_tools sys-apps/systemd
    sys-auth/polkit dev-libs/libnl:1.1 net-wireless/wpa_supplicant[dbus] net-libs/libsoup
    >=sys-libs/glib-2.30

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
    raw_configure("--prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --libexecdir=/usr/lib/networkmanager \
    --with-crypto=nss \
    --with-dhclient=/usr/sbin/dhclient \
    --with-dhcpcd=/usr/sbin/dhcpcd \
    --with-iptables=/usr/sbin/iptables \
    --with-systemdsystemunitdir=/usr/lib/systemd/system \
    --with-udev-dir=/usr/lib/udev \
    --with-resolvconf=/usr/sbin/resolvconf \
    --with-session-tracking=systemd \
    --disable-static \
    --disable-ppp \
    --enable-more-warnings=no \
    --disable-wimax \
    --enable-modify-system \
    --enable-doc")

def install():
    installd()
    insfile("%s/NetworkManager.conf" % filesdir, "/etc/NetworkManager/")
    makedirs("/etc/NetworkManager/dnsmasq.d")

