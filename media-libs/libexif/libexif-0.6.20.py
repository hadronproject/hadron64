metadata = """
summary @ A library to parse an EXIF file and read the data from those tags
homepage @ http://sourceforge.net/projects/libexif
license @ LGPL
src_url @ http://downloads.sf.net/sourceforge/$name/$fullname.tar.bz2
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
