metadata = """
summary @ run scripts or programs in a directory
homepage @ http://packages.qa.debian.org/d/debianutils.html
license @ GPL
src_url @ http://ftp.de.debian.org/debian/pool/main/d/debianutils/debianutils_$version.tar.gz
arch @ ~x86_64
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
