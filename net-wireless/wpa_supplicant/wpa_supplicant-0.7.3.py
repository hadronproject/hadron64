metadata = """
summary @ A utility providing key negotiation for WPA wireless networks
homepage @ http://hostap.epitest.fi/wpa_supplicant
license @ GPL
src_url @ http://hostap.epitest.fi/releases/$fullname.tar.gz
arch @ ~x86_64
options @ dbus debug eap-sim readline gnutls 
"""

depends = """
runtime @ dev-libs/openssl sys-apps/dbus sys-libs/readline dev-libs/libnl:1.1
"""

opt_runtime = """
readline @ sys-libs/ncurses sys-libs/readline
gnutls @ net-libs/gnutls
"""

def prepare():
    cd(name)
    patch("dbus.patch", level=2)
    copy("%s/config" % filesdir, "./.config")
    system("sed -i 's@/usr/local@$(PREFIX)@g' Makefile")
    #   seems deprecated
    #    echo("CONFIG_LIBNL20=y", ".config")

def configure():

    echo("CONFIG_CTRL_IFACE=y", ".config")
    echo("CONFIG_BACKEND=file", ".config")

    echo("CONFIG_EAP_GTC=y", ".config")
    echo("CONFIG_EAP_MD5=y", ".config")
    echo("CONFIG_EAP_OTP=y", ".config")
    echo("CONFIG_EAP_PAX=y", ".config")
    echo("CONFIG_EAP_PSK=y", ".config")
    echo("CONFIG_EAP_TLV=y", ".config")
    echo("CONFIG_IEEE8021X_EAPOL=y", ".config")
    echo("CONFIG_PKCS12=y", ".config")
    echo("CONFIG_PEERKEY=y", ".config")
    echo("CONFIG_EAP_LEAP=y", ".config")
    echo("CONFIG_EAP_MSCHAPV2=y", ".config")
    echo("CONFIG_EAP_PEAP=y", ".config")
    echo("CONFIG_EAP_TLS=y", ".config")
    echo("CONFIG_EAP_TTLS=y", ".config")

    #if opt("dbus"): dbus is default
    echo("CONFIG_CTRL_IFACE_DBUS=y", ".config")
    echo("CONFIG_CTRL_IFACE_DBUS_NEW=y", ".config")
    echo("CONFIG_CTRL_IFACE_DBUS_INTRO=y", ".config")

    if opt("debug"):
        echo("CONFIG_DEBUG_FILE=y", ".config")

    if opt("eap-sim"):
        echo("CONFIG_EAP_SIM=y", ".config")
        echo("CONFIG_EAP_AKA=y", ".config")
        echo("CONFIG_EAP_AKA_PRIME=y", ".config")
        echo("CONFIG_PCSC=y", ".config")

    if opt("readline"):
        echo("CONFIG_READLINE=y", ".config")

    if opt("gnutls"):
        echo("CONFIG_GNUTLS=y", ".config")
        echo("CONFIG_GNUTLS_EXTRA", ".config")
    else:
        echo("CONFIG_TLS=internal", ".config")

    #if opt("linux"): ?

    echo("CONFIG_DRIVER_ATMEL=y", ".config")
    echo("CONFIG_DRIVER_HOSTAP=y", ".config")
    echo("CONFIG_DRIVER_IPW=y", ".config")
    echo("CONFIG_DRIVER_NDISWRAPPER=y", ".config")
    echo("CONFIG_DRIVER_NL80211=y", ".config")
    echo("CONFIG_DRIVER_RALINK=y", ".config")
    echo("CONFIG_DRIVER_WEXT=y", ".config")
    echo("CONFIG_DRIVER_WIRED=y", ".config")
        

def build():
    cd(name)
    make()

def install():
    cd(name)
    raw_install("DESTDIR=%s" % install_dir)
