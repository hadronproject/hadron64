get("python_utils")

standart_procedure = False

metadata = """
summary @ Python sandboxing module
homepage @ http://www.pardus.org
license @ GPL-2
src_url @ http://cekirdek.pardus.org.tr/~gurer/pisi/$name-$version.tar.gz
"""

depends = """
runtime @ dev-lang/python
build @ dev-lang/python
"""

def install():
    python_utils_install()
    insdoc("README")
    makedirs("lib/hede/hodo")

