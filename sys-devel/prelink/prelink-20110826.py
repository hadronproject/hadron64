metadata = """
summary @ ELF prelinking utility to speed up dynamic linking.
homepage @ http://people.redhat.com/jakub/prelink/
license @ GPL-2
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/prelink/prelink-20110826.tar.bz2/d9ecbd8193d9aa3b8cbc3bf76db7aeff/prelink-20110826.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ dev-libs/elfutils
"""

srcdir = "prelink"

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/doc/prelink.conf" % build_dir, "/etc/prelink.conf")
    insdoc("TODO", "ChangeLog")
