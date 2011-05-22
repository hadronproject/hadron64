metadata = """
summary @ Generic SCSI utilities
homepage @ http://sg.danny.cz/sg/sg3_utils.html
license @ GPL BSD
src_url @ http://sg.danny.cz/sg/p/$fullname.tgz
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")

