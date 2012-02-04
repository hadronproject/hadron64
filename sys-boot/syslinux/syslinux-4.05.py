metadata = """
summary @ Collection of boot loaders that boot from FAT, ext2/3/4 and btrfs filesystems, from CDs and via PXE
homepage @ http://syslinux.zytor.com/
license @ GPL2
src_url @ http://www.kernel.org/pub/linux/utils/boot/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl
build @ dev-lang/yasm
"""

def prepare():
    patch(level=1)
    sed(""" -i 's|/usr/man|/usr/share/man|g' mk/syslinux.mk""")

def configure():
    pass

def install():
    raw_install("INSTALLROOT=%s AUXDIR=/usr/lib/syslinux" % install_dir)

    insfile("%s/syslinux.cfg" % filesdir, "/boot/syslinux/syslinux.cfg")
    insexe("%s/syslinux-install_update" % filesdir, "/usr/sbin/syslinux-install_update")

def post_install():
    notify("If you want to use syslinux as your bootloader")
    notify("==> edit /boot/syslinux/syslinux.cfg and run")
    notify("==> # /usr/sbin/syslinux-install_update -i -a -m")
    notify("==> to install it.")
    notify("")
    notify("Also if you are upgrading syslinux,")
    notify("run ==> # /usr/sbin/syslinux-install_update -s")
