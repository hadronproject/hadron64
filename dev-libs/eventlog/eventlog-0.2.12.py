metadata = """
summary @ API to format and send structured log messages
homepage @ http://www.balabit.com/support/community/products/
license @ BSD
src_url @ http://www.balabit.com/downloads/files?path=/$name/0.2/$name_$version.tar.gz
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s install" % install_dir)

