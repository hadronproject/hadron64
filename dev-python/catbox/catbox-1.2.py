get("python_utils")

metadata = """
summary @ Python sandboxing module
homepage @ http://www.pardus.org
license @ GPL-2
src_url @ http://cekirdek.pardus.org.tr/~gurer/pisi/$name-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/python
build @ dev-lang/python
"""

standart_procedure = False

def install():
    python_utils_install()
    insdoc("README")
