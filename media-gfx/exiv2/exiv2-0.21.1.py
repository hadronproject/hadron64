metadata = """
summary @ Exif and Iptc metadata manipulation library and tools
homepage @ http://exiv2.org/
license @ GPL2
src_url @ http://www.exiv2.org/$fullname.tar.gz
arch @ ~x86
options @ nls xmp zlib
"""

depends = """
runtime @ sys-devel/gcc
"""

opt_build = """
nls @ sys-devel/gettext
xmp @ dev-libs/boost
zlib @ sys-libs/zlib
"""

def configure():
    myconf = ""
    if not opt("zlib"):
        myconf += " --without-zlib "
    
    conf(
    config_enable("nls"),
    config_enable("xmp"), myconf)
