metadata = """
summary @ Standard tool to compile source trees
homepage @ http://www.gnu.org/software/make/make.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$name-$version.tar.gz
options @ nls
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gettext sys-libs/glibc
"""

def configure():
    conf("--program-prefix=g", config_enable("nls"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    makesym("gmake", "/usr/bin/make")
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
