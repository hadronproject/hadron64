metadata = """
summary @ DejaVu fonts, bitstream vera with ISO-8859-2 characters
homepage @ http://dejavu.sourceforge.net/
license @ custom
src_url @ http://distfiles.gentoo.org/distfiles/dejavu-fonts-ttf-2.33.tar.bz2
arch @ ~x86
"""

srcdir = "dejavu-fonts-ttf-%s" % version

standard_procedure = False
#def build():
#    export("HOME", build_dir)
#    make()

def install():
    export("HOME", build_dir)
    insinto("ttf/*.ttf", "/usr/share/fonts/dejavu")
    for conf in ls("fontconfig"):
        insinto("fontconfig/%s" % conf, "/etc/fonts/conf.avail")
        makesym("../conf.avail/%s" % conf, "/etc/fonts/conf.d/%s" % conf)

    #makesym("/usr/share/fonts/dejavu" , "/etc/X11/fontpath.d/dejavu")
    insdoc("AUTHORS", "LICENSE", "NEWS", "README")
