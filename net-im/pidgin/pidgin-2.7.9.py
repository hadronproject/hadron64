metadata = """
    summary @ GTK instant messenger
    license @ GPL-2
    homepage @ http://pidgin.im
    src_url @ mirror://sourceforge/$name/$name-$version.tar.bz2
    packager @ Burak Sezer, purak, purak@hadronproject.org
    options @ gstreamer meanwhile tk spell avahi python perl dbus sasl gtk ncurses zeroconf msn myspace networkmanager
"""

depends = """
    runtime = "atk cairo pango gtk gstreamer[gstreamer] tk[tk]"
    buildtime =$runtime"
"""

def configure():
    dynamic_prpls = ''; myconf = ''
    if opt("meanwhile"): dynamic_prpls += "meanwhile"
    if opt("msn"): dynamic_prpls += ",msn"
    if opt("myspace"): dynamic_prpls += ",myspace" 

    if opt("gtk"): myconf += config_enable("spell", "gtkspell")
    conf("--disable-mono",
            "--with-dynamic-prpls=%s" % dynamic_prpls,
            config_enable("gstreamer"),
            config_enable("meanwhile"),
            config_enable("tk"),
            config_enable("zeroconf", "avahi"),
            config_enable("gstreamer", "farsight"),
            config_enable("sasl", "cyrus-sasl"),
            config_enable("gstreamer", "vv"),
            config_enable("networkmanager", "nm"),
            config_enable("ncurses", "consoleui"),
            config_enable("gtk", "gtkui"),
            config_enable("perl"),
            myconf)

def install():
    export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    raw_install("DESTDIR=%s" % install_dir)
