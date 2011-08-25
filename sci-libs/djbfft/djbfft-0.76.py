metadata = """
summary @ An extremely fast library for FFT
homepage @ http://cr.yp.to/djbfft.html
license @ public-domain
src_url @ http://cr.yp.to/$name/$fullname.tar.gz
arch @ ~x86
"""

ver = "0.7.6"

def prepare():
    patch("gcc.patch", level=1)
    patch("shared.patch", level=1)
    patch("headers.patch")

def configure():
    echo ("%s/usr" % install_dir,"conf-home")
    echo("gcc -O1 -fomit-frame-pointer -fPIC -DPIC -malign-double","conf-cc")

def build():
    make('LIBDJBFFT="libdjbfft.so.%s" LIBPERMS="0755"' % ver)

def install():
    insinto("libdjbfft.so.%s" % ver, "/usr/lib")
    makesym("/usr/lib/libdjbfft.so.%s" % ver,"/usr/lib/libdjbfft.so")
    makesym("/usr/lib/libdjbfft.so.%s" % ver,"/usr/lib/libdjbfft.so.0")

    for header in ["fftc4.h", "complex4.h", "real4.h"]:
        insinto(header, "/usr/include")

    insdoc("CHANGES","README","TODO")
