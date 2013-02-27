blame = """
alias @ purak
packager @ Burak Sezer <purak{et}hadronproject.org>
bugs_to @ toolchain{et}hadronproject.org
"""

metadata = """
summary @ Hardware (PCI, USB, OUI, IAB) IDs databases
homepage @ https://github.com/gentoo/hwids
license @ GPL-2 BSD
src_url @ ftp://download.tuxfamily.org/hadron/distfiles/$fullname.tar.bz2
arch @ ~x86_64
"""

standard_procedure = False
srcdir = name

def install():
    for ids in ('pci.ids', 'usb.ids'):
        insfile("%s/%s" % (build_dir, ids), \
                "/usr/share/hwdata/%s" % ids)
