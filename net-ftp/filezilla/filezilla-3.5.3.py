metadata = """
summary @ Fast and reliable FTP, FTPS and SFTP client
homepage @ http://filezilla-project.org/
license @ GPL
src_url @ http://downloads.sourceforge.net/project/filezilla/FileZilla_Client/$version/FileZilla_$version_src.tar.bz2
arch @ ~x86
options @ dbus nls
"""

depends = """
runtime @ >=dev-db/sqlite-3.7 net-dns/libidn >=net-libs/gnutls-2.8.3
>=x11-libs/wxgtk-2.8.9[X] x11-misc/xdg-utils
build @ dev-util/pkg-config >=sys-devel/libtool-1.4
"""

opt_runtime = """
dbus @ sys-apps/dbus
"""

opt_build = """
nls @ >=sys-devel/gettext-0.11
"""

def configure():
    conf(
    config_with("dbus"),
    config_enable("nls", "locales"),
    "--disable-autoupdatecheck",
    "--disable-manualupdatecheck",
    "--with-tinyxml=builtin")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS")
    insfile("src/interface/resources/48x48/filezilla.png", "/usr/share/pixmaps/filezilla.png")
