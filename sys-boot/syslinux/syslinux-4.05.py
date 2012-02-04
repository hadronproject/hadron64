metadata = """
summary @ Collection of boot loaders that boot from FAT, ext2/3/4 and btrfs filesystems, from CDs and via PXE
homepage @ http://syslinux.zytor.com/
license @ GPL2
src_url @ http://www.kernel.org/pub/linux/utils/boot/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl sys-libs/glibc
build @ dev-lang/nasm
"""

def prepare():
    patch(level=1)
    sed("-i 's|/usr/man|/usr/share/man|g' mk/syslinux.mk")

def build():
    # gnized option '-Wl,--hash-style=gnu'
    # ld: use the --help option for usage information
    # make[1]: *** [pxelinux.elf] Error 1
    # make[1]: *** Waiting for unfinished jobs....
    # ld: unrecognized option '-Wl,--hash-style=gnu'
    # ld: use the --help option for usage information
    # make[1]: *** [isolinux.elf] Error 1

    # unset env variables to fix top error
    unset_env_variables()
    make()
    
def install():
    raw_install("INSTALLROOT=%s AUXDIR=/usr/lib/syslinux" % install_dir)

    insfile("%s/syslinux.cfg" % filesdir, "/boot/syslinux/syslinux.cfg")
    insexe("%s/syslinux-install_update" % filesdir, "/usr/sbin/syslinux-install_update")

def post_install():
    # post install messages were borrowed by seqizz from arch linux
    notify("If you want to use syslinux as your bootloader")
    notify("edit /boot/syslinux/syslinux.cfg and run")
    notify("# syslinux-install_update -i -a -m")
    notify("to install it.")
    notify("")
    notify("Also if you are upgrading syslinux,")
    notify("run # syslinux-install_update -s")
