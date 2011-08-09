metadata = """
summary @ An MP3 encoder and graphical frame analyzer
homepage @ http://lame.sourceforge.net/
license @ LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86
options @ mmx sndfile static-libs debug mp3rtp
"""

depends = """
runtime @ sys-libs/glibc sys-libs/ncurses
"""

def configure():
    myconf = ""
    if opt("sndfile"):
        myconf += " --with-fileio=sndfile "

    conf(
    "--disable-dependency-tracking",
    config_enable("static-libs", "static"),
    config_enable("debug"),
    config_enable("debug", "norm"),
    config_enable("mmx", "nasm"),
    config_enable("mp3rtp"),
    "--disable-mp3x", myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("API", "ChangeLog", "HACKING", "STYLEGUIDE", "TODO", "USAGE")
