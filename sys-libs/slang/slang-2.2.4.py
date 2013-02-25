metadata = """
summary @ S-Lang is a powerful interpreted language
homepage @ http://www.jedsoft.org/slang/
license @ GPL
src_url @ ftp://ftp.fu-berlin.de/pub/unix/misc/slang/v2.2/$name-$version.tar.bz2
arch @ ~x86_64
options @ pcre png readline zlib
"""

opt_runtime = """
pcre @ dev-libs/pcre
png @ >=media-libs/libpng-1.4
readline @ sys-libs/readline
zlib @ sys-libs/zlib
"""

def configure():
    rdln = "slang"
    if opt("readline"):
        rdln = "gnu"
    conf(
    "--with-readline=%s" % rdln,
    config_with("pcre"),
    config_with("png"),
    config_with("zlib", "z"))

def build():
    make(j=1)

def install():
    raw_install("DESTDIR=%s install-all" % install_dir)
    insdoc("NEWS", "README", "*.txt")
