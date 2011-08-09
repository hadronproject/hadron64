metadata = """
summary @ Kernel headers sanitized for use in userspace.
homepage @ http://www.kernel.org
license @ GPL-2
src_url @ http://kernel.org/pub/linux/kernel/v2.6/linux-$version.tar.bz2
arch @ ~x86
"""

standard_procedure = False
<<<<<<< HEAD
srcdir = "linux-2.6.38"
=======
srcdir = "linux-2.6.39.1"
>>>>>>> 801bf3dac0c471b3b8cf78e69a1349bfe0d182e0

def build():
    make("mrproper")
    make("headers_check")

def install():
    make("INSTALL_HDR_PATH=%s/usr headers_install" % install_dir)
