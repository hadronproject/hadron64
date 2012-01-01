metadata = """
summary @ Library to pack up hard disk files and directories into a ISO 9660 disk image
homepage @ http://libburnia.pykix.org/
license @ GPL-2
src_url @ http://files.libburnia-project.org/releases/$fullname.tar.gz
options @ debug verbose-debug acl xattr 
arch @ ~x86
"""

opt_common = """
acl @ sys-apps/acl
xattr @ sys-apps/attr
zlib @ sys-libs/zlib
"""

def configure():
    conf(config_enable("static-libs", "static"),
            config_enable("debug"),
            config_enable("verbose-debug"),
            config_enable("acl", "libacl"),
            config_enable("xattr"),
            config_enable("zlib"),
            "--disable-libjte",
            "--disable-ldconfig-at-install")

install = lambda: installd()


