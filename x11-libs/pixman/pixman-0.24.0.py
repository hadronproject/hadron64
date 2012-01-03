metadata = """
summary @ Pixman library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/$fullname.tar.bz2
arch @ ~x86
options @ mmx sse2 neon
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_depends = """
neon @ net-libs/neon
"""

def configure():
    myconf = ""
    if opt("sse2"):
        if opt("mmx"):
            myconf += " --enable-mmx --enable-sse2 "
        else:
            warn("You enabled SSE2 but have MMX disabled. This is invalid.")
            warn("pixman will be built *without* MMX/SSE2 support.")
            myconf += " --disable-mmx --disable-sse2 "
    else:
        if opt("mmx"):
            myconf += " --disable-sse2 --enabled-mmx "
        else:
            myconf += " --disable-sse2 --disable-mmx "

    conf(
    "--disable-static",
    "--disable-gtk",
    config_enable("neon", "arm-neon"), myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
