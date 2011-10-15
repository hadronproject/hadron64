metadata = """
summary @ The X Server
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/xserver/$fullname.tar.bz2
arch @ ~x86
options @ doc ipv6
"""

depends = """
runtime @ dev-libs/openssl media-libs/freetype >=x11-apps/iceauth-1.0.2 x11-apps/rgb
x11-apps/xauth x11-apps/xkbcomp >=x11-libs/libpciaccess-0.10.3
>=x11-libs/libXau-1.0.4 >=x11-libs/libXdmcp-1.0.2 >=x11-libs/libXfont-1.4.2
>=x11-libs/libxkbfile-1.0.4 >=x11-libs/pixman-0.21.8 >=x11-libs/xtrans-1.2.2
>=x11-misc/xbitmaps-1.0.1 >=x11-misc/xkeyboard-config-1.4
x11-libs/libXt >=x11-libs/libdmx-1.0.99.1 >=x11-libs/libX11-1.1.5 >=x11-libs/libXaw-1.0.4
>=x11-libs/libXext-1.0.99.4 >=x11-libs/libXfixes-5.0 >=x11-libs/libXi-1.2.99.1
>=x11-libs/libXmu-1.0.3 >=x11-libs/libXres-1.0.3 >=x11-libs/libXtst-1.0.99.2
x11-libs/libXv >=media-libs/mesa-7.8
build @ sys-devel/flex >=x11-proto/bigreqsproto-1.1.0 >=x11-proto/compositeproto-0.4
>=x11-proto/damageproto-1.1 >=x11-proto/fixesproto-5.0 >=x11-proto/fontsproto-2.0.2
>=x11-proto/glproto-1.4.14 >=x11-proto/inputproto-1.9.99.902 >=x11-proto/kbproto-1.0.3
>=x11-proto/randrproto-1.2.99.3 >=x11-proto/recordproto-1.13.99.1
>=x11-proto/renderproto-0.11 >=x11-proto/resourceproto-1.0.2 >=x11-proto/scrnsaverproto-1.1
x11-proto/trapproto >=x11-proto/videoproto-2.2.2 >=x11-proto/xcmiscproto-1.2.0
>=x11-proto/xextproto-7.1.99 >=x11-proto/xf86dgaproto-2.0.99.1
x11-proto/xf86rushproto >=x11-proto/xf86vidmodeproto-2.2.99.1
>=x11-proto/xineramaproto-1.1.3 >=x11-proto/xproto-7.0.22
>=x11-proto/dmxproto-2.2.99.1
>=x11-proto/xf86driproto-2.1.0 >=x11-proto/dri2proto-2.6 >=x11-libs/libdrm-2.4.20
"""

opt_build = """
doc @ app-text/xmlto www-client/links
"""

def prepare():
    patch("xorg-server-disable-acpi.patch", level=1)
    patch("xorg-server-1.9-nouveau-default.patch", level=1)
    patch("xorg-redhat-die-ugly-pattern-die-die-die.patch", level=3)
def configure():
    conf(
            config_enable("ipv6"),
            "--enable-dri \
            --enable-dmx \
            --enable-xvfb \
            --enable-xnest \
            --enable-composite \
            --enable-xcsecurity \
            --enable-xorg \
            --enable-xephyr \
            --enable-glx-tls \
            --enable-kdrive \
            --enable-install-setuid \
            --enable-config-udev \
            --disable-config-dbus \
            --enable-record \
            --disable-xfbdev \
            --disable-xfake \
            --disable-static \
            --sysconfdir=/etc/X11 \
            --localstatedir=/var \
            --with-xkb-path=/usr/share/X11/xkb \
            --with-xkb-output=/var/lib/xkb \
            --with-fontrootdir=/usr/share/fonts \
            --with-os-name=\"Hadron GNU/Linux\" \
            --with-os-vendor=\"Hadron Project\"",
            config_enable("doc", "specs"),
            config_with("doc", "xmlto"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    for d in ("/etc/X11/fontpath.d", "/etc/X11/xorg.conf.d",
            "/usr/share/X11/pci", "/usr/share/X11/xorg.conf.d"):
        makedirs(d)
    rmdir("/var/log")

    insdoc("COPYING")

def post_install():
    warn("Don't forget to re-install these packages:")
    command = """ls /var/db/lpms/filesdb/x11-drivers/xf86* | grep '\.xml' | sed 's/.xml//g' | awk -F "-" {print'$1"-"$2"-"$3'}"""
    system(command)
