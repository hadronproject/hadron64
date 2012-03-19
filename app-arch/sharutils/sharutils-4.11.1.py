metadata = """
summary @ Tools to deal with shar archives
homepage @ http://www.gnu.org/software/sharutils/
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86
options @ nls
"""

depends = """
build @ sys-apps/texinfo
"""

opt_build = """
nls @ sys-devel/gettext
"""

def configure():
    conf(config_enable("nls"))

def install():
    installd()
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
