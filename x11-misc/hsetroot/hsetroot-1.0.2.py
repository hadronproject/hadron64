metadata = """
summary @ A tool which allows you to compose wallpapers for X.
homepage @ http://www.thegraveyard.org/hsetroot.php
license @ GPL
src_url @ http://www.thegraveyard.org/files/$name-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc media-libs/imlib2[X]
build @ x11-proto/xproto
"""
