metadata = """
summary @ A simple keystroke-driven window manager
homepage @ http://www.nongnu.org/ratpoison/
license @ GPL
src_url @ http://savannah.nongnu.org/download/$name/$fullname.tar.gz
arch @ ~x86
options @ debug history xft
"""

depends = """
runtime @ x11-libs/libXinerama x11-libs/libXtst dev-perl/Pod-Parser
"""

opt_build = """
history @ sys-libs/readline
xft @ x11-libs/libXft
"""

def configure():
    if not opt("history"):
        myconf = " --disable-history "


    conf(
    config_with("xft"),
    config_enable("debug"), myconf)

def build():
    make("CFLAGS=\"$CFLAGS -DHAVE_GETLINE\"")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("INSTALL", "TODO", "README", "NEWS", "AUTHORS", "ChangeLog")

    cd("contrib")
    system("./genrpbindings")
    for bind in ("Ratpoison.pm", "ratpoison-cmd.el", "ratpoison.rb", "ratpoison.lisp", "ratpoison.py"):
        insfile(bind, "/usr/share/ratpoison/bindings/")
    
    insfile("%s/ratpoison.desktop" % filesdir, "/etc/X11/sessions/")

