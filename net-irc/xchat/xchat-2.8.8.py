metadata = """
	summary @ Graphical IRC client
	license @ GPL-2
	homepage @ http://www.xchat.org
    src_url @ http://xchat.org/files/source/2.8/$name-$version.tar.bz2
	options @ dbus gtk ipv6 libnotify nls perl python ssl debug fastscroll mmx ntlm spell tcl xchatdccserver
"""

def configure():
	conf("--enable-shm",
	config_enable("dbus"),
	config_enable("ipv6"),
	config_enable("mmx"),
	config_enable("nls"),
	config_enable("ntlm"),
	config_enable("perl"),
	config_enable("python"),
	config_enable("spell", "spell"),
	config_enable("ssl", "openssl"),
	config_enable("tcl"),
	config_enable("gtk", "gtkfe"),
	config_enable("fastscroll", "xft"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "COPYING", "ChangeLog", "HACKING", "README")
