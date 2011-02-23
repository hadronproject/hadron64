metadata = """
summary @ Kernel headers sanitized for use in userspace
homepage @ http://www.gnu.org/software/libc
license @ GPL-2
src_url @ http://kernel.org/pub/linux/kernel/v2.6/linux-$version.tar.bz2
"""

standart_procedure = False
srcdir = "linux-2.6.37"

def build():
    make("mrproper")
    make("headers_check")

def install():
    make("INSTALL_HDR_PATH=%s/usr headers_install" % install_dir)
