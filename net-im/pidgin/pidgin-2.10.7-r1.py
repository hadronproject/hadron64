metadata = """
summary @ GTK instant messenger
license @ GPL-2
homepage @ http://pidgin.im
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.bz2
options @ gstreamer meanwhile tcl spell python perl dbus sasl gtk ncurses zeroconf networkmanager gnutls debug zephyr idn
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/startup-notification x11-misc/libxss
        x11-themes/hicolor-icon-theme app-misc/ca-certificates dev-util/intltool
"""

opt_runtime = """
dbus @ sys-apps/dbus
        dev-python/dbus-python
        dev-libs/dbus-glib
spell @ app-text/gtkspell
ncurses @ sys-libs/ncurses
        dbus @ x11-libs/gtk+:2 
                x11-libs/libSM
gnutls @ net-libs/gnutls || dev-libs/nss
gtk @ x11-libs/gtk+:2 
sasl @ dev-libs/cyrus-sasl
meanwhile @ net-libs/meanwhile
gstreamer @ media-libs/gstreamer
networkmanager @ net-misc/networkmanager
tcl @ dev-lang/tcl
idn @ net-dns/libidn
"""

# FIXME: the options and configure function will be improved. Take a look at msn for example: http://goo.gl/ps05p

get("main/gnome2_utils")

# patches from gentoo
prepare = lambda: patch(level=1)

def configure():
    dynamic_prpls="irc,jabber"
    myconf = ""
    if opt("gnutls"):
        myconf += " --enable-nss=no --enable-gnutls=yes --with-gnutls-includes=/usr/include/gnutls "
    else:
        myconf += " --enable-gnutls=no --enable-nss=yes "

    _dynamic_prpls = ["oscar","yahoo","simple","msn","myspace","silc","zephyr"]
    for prpl in _dynamic_prpls:
        if opt("%s" % prpl):
            dynamic_prpls += ",%s" % prpl
    if opt("meanwhile"):
        dynamic_prpls += ",sametime"
    if opt("groupwise"):
        dynamic_prpls += ",novell"
    if opt("zeroconf") or opt("avahi"):
        notify("we still don't have a avahi package, so disabling zeroconf/bonjour support for now")
        #dynamic_prpls += ",bonjour"
    
    conf("--disable-mono",
    "--disable-schemas-install",
    "--disable-avahi",
    "--disable-doxygen",
    "--with-dynamic-prpls=%s" % dynamic_prpls,
    config_enable("networkmanager", "nm"),
    "--with-system-ssl-certs=/etc/ssl/certs",
    "--disable-vv",
    config_enable("debug"),
    config_enable("gstreamer"),
    config_enable("gtk", "gtkui"),
    config_enable("dbus"),
    config_enable("spell", "gtkspell"),
    config_enable("ncurses", "consoleui"),
    config_enable("meanwhile"),
    config_enable("sasl", "cyrus-sasl"),
    config_enable("tcl"),
    config_enable("idn"), myconf)


def install():
    export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    gnome2_icon_cache_update()
