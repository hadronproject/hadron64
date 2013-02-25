metadata = """
summary @ Generic initramfs generation tool
homepage @ http://dracut.wiki.kernel.org/
license @ GPL2
src_url @ http://www.kernel.org/pub/linux/utils/boot/dracut/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ app-text/docbook-xsl-stylesheets app-shells/bash sys-apps/util-linux sys-fs/udev dev-libs/libxslt
"""

standard_procedure = False

def build():
    make("sysconfdir=/etc")

def install():
    raw_install("DESTDIR=%s sysconfdir=/etc" % install_dir)
