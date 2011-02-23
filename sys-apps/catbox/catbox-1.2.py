get("python_utils")

standart_procedure = False

metadata = """
summary @ Python sandboxing module
homepage @ http://www.pardus.org
license @ GPL-2
src_url @ http://cekirdek.pardus.org.tr/~gurer/pisi/$name-$version.tar.gz
"""

def install():
    python_utils_install()
    insdoc("README")
