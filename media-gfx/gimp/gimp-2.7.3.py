metadata = """
summary @ GNU Image Manipulation Program
homepage @ http://www.gimp.org/
license @ GPL LGPL
src_url @ http://mirror.csclub.uwaterloo.ca/gentoo-distfiles/distfiles/$fullname.tar.bz2
arch @ ~x86
options @ alsa aalib altivec curl dbus debug doc exif gnome jpeg lcms mmx mng pdf png python smp sse svg tiff webkit wmf udev
slot @ 2
"""

depends = """
runtime @ >=sys-libs/glib-2.18.1 dev-libs/libxml2 dev-libs/libxslt 
>=media-libs/fontconfig-2.2.0 >=media-libs/freetype-2.1.7
>=media-libs/gegl-0.0.22 >=x11-libs/gtk+-2.12.5:2
x11-libs/libXpm >=media-libs/pango-1.18.0 sys-libs/zlib x11-misc/xdg-utils
x11-themes/hicolor-icon-theme x11-libs/libXcursor
build @ >=dev-util/intltool-0.40 >=dev-util/pkg-config-0.12.0
>=sys-devel/gettext-0.17
"""

opt_runtime = """
aalib @ media-libs/aalib
alsa @ media-libs/alsa-lib 
curl @ net-misc/curl 
dbus @ dev-libs/dbus-glib 
exif @ >=media-libs/libexif-0.6.15 
gnome @ gnome-base/gvfs 
jpeg @ media-libs/jpeg
lcms @ media-libs/lcms
mng @ media-libs/libmng 
pdf @ >=app-text/poppler-0.12.3-r3[cairo]
png @ >=media-libs/libpng-1.2.2
python @ >=dev-python/pygtk-2.10.4
svg @ >=gnome-base/librsvg-2.8.0
tiff @ >=media-libs/tiff-3.5.7 
webkit @ net-libs/webkit-gtk
wmf @ >=media-libs/libwmf-0.2.8
udev @ sys-fs/udev[gudev]
"""

get("fdo_mime")
get("gnome2_utils")

def prepare():
    patch("gimp-2.7.3-glib-2.29.patch")

def configure():
    conf(
    "--disable-dependency-tracking",
    "--enable-default-binary",
    "--with-x",
    "--without-hal",
    "--without-gnomevfs",
    config_with("aalib", "aa"),
    config_with("alsa"),
    config_enable("altivec"),
    config_with("curl", "libcurl"),
    config_with("dbus"),
    config_with("gnome", "gvfs"),                
    config_with("webkit"),
    config_with("jpeg", "libjpeg"),
    config_with("exif", "libexif"),
    config_with("lcms"),
    config_enable("mmx"),
    config_with("mng", "libmng"),
    config_with("pdf", "poppler"),
    config_with("png", "libpng"),
    config_enable("python"),
    config_enable("smp", "mp"),
    config_enable("sse"),
    config_with("svg", "librsvg"),
    config_with("tiff", "libtiff"),
    config_with("wmf"),
    config_with("udev", "gudev"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    sed("-i 's|#!/usr/bin/env python|#!/usr/bin/env python2|' %s/usr/lib/gimp/2.0/plug-ins/*.py" % install_dir)
    insdoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README*")
    system("ln -s gimptool-2.0 %s/usr/bin/gimptool" % install_dir)

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()

def post_remove():
    post_install()
