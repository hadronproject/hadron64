metadata = """
summary @ Libraries/utilities to handle ELF objects (drop in replacement for libelf)
homepage @ https://fedorahosted.org/elfutils
license @ GPL-2-with-exceptions
src_url @ https://fedorahosted.org/releases/e/l/elfutils/$version/$fullname.tar.bz2
options @ zlib bzip2 lzma nls
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ >=sys-devel/flex-2.5.4a sys-devel/m4 
>=sys-devel/binutils-2.15.90.0.1 >=sys-devel/gcc-4.1.2
"""

opt_common = """
zlib @ >=sys-libs/zlib-1.2.2.3
bzip2 @ app-arch/bzip2
lzma @ app-arch/xz
"""

def configure():
    conf(config_enable("nls"), config_enable("bzip2", "bzlib"),
            config_enable("lzma"), '--program-prefix="eu-"')

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", 
            "NOTES", "README", "THANKS", "TODO")
