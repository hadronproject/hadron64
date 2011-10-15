metadata = """
summary @ Midnight Commander is a text based filemanager/shell that emulates Norton Commander
homepage @ http://www.ibiblio.org/mc/
license @ GPL
src_url @ http://www.midnight-commander.org/downloads/$name-$version.tar.bz2
arch @ ~x86
options @ gpm nls X slang ncurses debug
"""

depends = """
runtime @ >=sys-libs/glib-2.8 sys-fs/e2fsprogs
build @ dev-util/pkg-config
"""
#TODO: kernel_linux needs e2fsprogs, what if not linux? :P
opt_runtime = """
X @ x11-libs/libX11 x11-libs/libICE x11-libs/libXau x11-libs/libXdmcp x11-libs/libSM
gpm @ sys-libs/gpm
ncurses @ sys-libs/ncurses
slang @ >=sys-libs/slang-2
"""

opt_build = """
nls @ sys-devel/gettext
"""


def configure():
    myscreen = ""
    if opt("slang") and opt("ncurses"):
        import lpms
        lpms.terminate("You have to choose only one option: \"slang\" or \"ncurses\". Can't open both.")
    elif opt("slang") and not opt("ncurses"):
        myscreen += " --with-screen=slang "
    elif opt("ncurses") and not opt("slang"):
        myscreen += " --with-screen=ncurses "
    elif not opt("slang") and not opt("ncurses"):
        import lpms
        lpms.terminate("You have to choose one option: \"slang\" or \"ncurses\". You didn't select any.")

    conf(
    "--disable-dependency-tracking",
    config_enable("nls"),
    "--enable-vfs",
    "--enable-vfs-undelfs",
    "--enable-charset",
    "--with-subshell",
    "--with-edit",
    config_with("X", "x"),
    config_with("debug"),
    config_with("gpm", "gpm-mouse"), myscreen)

def install():
    insdoc("AUTHORS", "README")
    raw_install("DESTDIR=%s" % install_dir)
