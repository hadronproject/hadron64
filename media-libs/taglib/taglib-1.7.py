metadata = """
summary @ A Library for reading and editing the meta-data of several popular audio formats
homepage @ http://developer.kde.org/~wheeler/taglib.html
license @ GPL2
src_url @ http://developer.kde.org/~wheeler/files/src/$fullname.tar.gz
arch @ ~x86
options @ asf debug examples mp4
"""

depends = """
runtime @ sys-libs/zlib
build @ dev-util/cmake dev-util/pkg-config
"""

def configure():
	pass

def build():
    system("mkdir build")
    cd("./build")
    myconf = ""
    if opt("mp4"):
        myconf += " -DWITH_MP4=ON "
    else:
        myconf += " -DWITH_MP4=OFF "

    if opt("asf"):
        myconf += " -DWITH_ASF=ON "
    else:
        myconf += " -DWITH_ASF=OFF "
    
    if opt("examples"):
        myconf += " -DBUILD_EXAMPLES=ON "
    else:
        myconf += " -DBUILD_EXAMPLES=OFF "

    system("cmake ../ \
        -DCMAKE_INSTALL_PREFIX=/usr \
	    -DCMAKE_BUILD_TYPE=Release %s " % myconf)
    make()

def install():
	cd("./build")
	raw_install("DESTDIR=%s" % install_dir)

def post_install():
    if not opt("asf"):
        notify("WARNING: You've chosen to disable the asf option, thus taglib won't include support for Microsoft's 'advanced systems format' media container")

    if not opt("mp4"):
        notify("WARNING: You've chosen to disable the mp4 option, thus taglib won't include support for the MPEG-4 part 14 / MP4 media container")

