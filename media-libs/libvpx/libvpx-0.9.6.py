metadata = """
summary @ The VP8 Codec SDK 
homepage @ http://www.webmproject.org/ 
license @ BSD 
src_url @ http://webm.googlecode.com/files/$name-v$version.tar.bz2 
arch @ ~x86
options @ altivec debug mmx postproc sse sse2 sse3 ssse3 sse4_1 threads cpudetection
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/yasm
"""

srcdir = name+"-v"+version

def configure():
    flaglarim = ("altivec", "debug", "mmx", "postproc", "sse", "sse2", "sse3", "ssse3", "sse4_1")
    raw_configure(
    "--enable-vp8",
    config_enable("cpudetection", "runtime-cpu-detect"),
    " ".join([config_enable(aha) for aha in (flaglarim)]),
    "--disable-install-docs",
    "--disable-install-srcs")
    pass

def install():
	raw_install("DIST_DIR=%s/usr" % install_dir)

	insdoc("LICENSE")

