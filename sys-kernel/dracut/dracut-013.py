metadata = """
summary @ Generic initramfs generation tool
homepage @ http://dracut.wiki.kernel.org/
license @ GPL2
src_url @ http://her.gr.distfiles.macports.org/mirrors/ftp.kernel.org/pub/linux/boot/dracut/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ app-text/docbook-xsl-stylesheets app-shells/bash sys-apps/util-linux sys-fs/udev dev-libs/libxslt
"""

standard_procedure = False

def build():
    make("sysconfdir=/etc")

def install():
    raw_install("DESTDIR=%s sysconfdir=/etc" % install_dir)
