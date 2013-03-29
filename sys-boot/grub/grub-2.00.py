metadata = """
summary @ A GNU multiboot boot loader
homepage @ http://www.gnu.org/software/grub/
license @ GPL
src_url @ http://ftp.gnu.org/gnu/grub/grub-$version.tar.xz
arch @ ~x86_64
slot @ 2
"""

# TODO: 
# * options: debug mount truetype libzfs static
# * perhaps, efi support?

depends = """
runtime @ sys-libs/ncurses sys-apps/sed sys-apps/diffutils app-arch/xz >=sys-libs/ncurses-5.2-r5
build @ >=dev-lang/python-2.5.2 sys-devel/flex sys-devel/bison sys-apps/texinfo
"""

def prepare():
    sed("-i -e '/gets is a/d' grub-core/gnulib/stdio.in.h")

def configure():
    conf("--program-prefix=",
            "--program-transform-name='s,grub,grub2,'",
            "--with-grubdir=grub2",
            "--disable-grub-emu-usb",
            "--disable-efiemu",
            "--disable-werror")

def install():
    raw_install("DESTDIR=%s" % install_dir)
