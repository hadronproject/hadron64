metadata = """
summary @ A string search utility
homepage @ http://www.gnu.org/software/grep/grep.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ nls
arch @ ~x86
"""

def configure():
    conf("--bindir=/bin",
        "--without-included-regex",
        config_enable("nls"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
