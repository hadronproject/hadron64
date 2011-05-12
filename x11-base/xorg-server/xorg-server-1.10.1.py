metadata = """
summary @ The X Server
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/xserver/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ x11-libs/pixman media-libs/mesa x11-proto/xf86vidmodeproto x11-proto/xextproto x11-proto/recordproto x11-proto/damageproto x11-proto/kbproto 
        x11-proto/inputproto x11-proto/fixesproto x11-proto/fontsproto x11-proto/xcb-proto x11-proto/compositeproto x11-proto/dri2proto x11-proto/xproto 
        x11-proto/xineramaproto x11-proto/dmxproto x11-proto/xf86dgaproto x11-proto/renderproto x11-proto/randrproto x11-proto/glproto x11-proto/videoproto 
        x11-libs/libXxf86vm x11-libs/libXi x11-libs/libXdmcp x11-libs/libXrandr x11-libs/libXau x11-libs/libXtst x11-libs/libXrender x11-libs/libXmu 
        x11-libs/libXcomposite x11-libs/libXext x11-libs/libXinerama x11-libs/libX11 x11-libs/libXfixes x11-libs/libxcb x11-libs/libXv x11-libs/libXt 
        x11-libs/libXxf86dga x11-libs/libXfont x11-libs/libXdamage x11-proto/xf86driproto x11-proto/xcmiscproto x11-proto/bigreqsproto x11-proto/scrnsaverproto 
        x11-proto/resourceproto x11-libs/libxkbfile x11-libs/libXaw x11-libs/libXres x11-libs/libpciaccess x11-libs/libdmx
"""

def prepare():
    patch("xorg-redhat-die-ugly-pattern-die-die-die.patch", level=3)
    patch("glx-pixmap-crash.patch", level=1)
    patch("bg-none-revert.patch", level=1)
    patch("xserver-1.10-pointer-barriers.patch", level=1)

def configure():
    conf("--enable-ipv6 \
            --enable-dri \
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
            --with-os-vendor=\"Hadron Project\"")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    for d in ("/etc/X11/fontpath.d", "/etc/X11/xorg.conf.d", 
            "/usr/share/X11/pci", "/usr/share/X11/xorg.conf.d"):
        makedirs(d)
    rmdir("/var/log")
    
    insdoc("COPYING")
