metadata = """
summary @ A utility providing key negotiation for WPA wireless networks
homepage @ http://hostap.epitest.fi/wpa_supplicant
license @ GPL
src_url @ http://hostap.epitest.fi/releases/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/openssl sys-apps/dbus sys-libs/readline dev-libs/libnl:1.1
"""

def prepare():
    cd(name)
    patch("dbus.patch", level=2)
    copy("%s/config" % filesdir, "./.config")
    system("sed -i 's@/usr/local@$(PREFIX)@g' Makefile")
    #   seems deprecated
    #    echo("CONFIG_LIBNL20=y", ".config")

def build():
    cd(name)
    make()

def install():
    cd(name)
    raw_install("DESTDIR=%s" % install_dir)
