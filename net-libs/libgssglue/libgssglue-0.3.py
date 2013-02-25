metadata = """
summary @ Exports a gssapi interface which calls other random gssapi libraries
homepage @ http://www.citi.umich.edu/projects/nfsv4/linux/
license @ BSD
src_url @ http://www.citi.umich.edu/projects/nfsv4/linux/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""


def install():
    installd()
    insfile("%s/gssapi_mech.conf" % filesdir, "/etc/gssapi_mech.conf")
    insdoc("COPYING")

