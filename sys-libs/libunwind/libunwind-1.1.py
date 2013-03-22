metadata = """
summary @ Portable and efficient API to determine the call-chain of a program
homepage @ http://savannah.nongnu.org/projects/libunwind
license @ X11
src_url @ http://download.savannah.nongnu.org/releases/libunwind/$fullname.tar.gz
arch @ ~x86_64
options @ debug debug-frame lzma
"""

opt_common = """
lzma @ app-arch/xz
"""

def configure():
    conf("--enable-cxx-exceptions",
            config_enable("debug-frame"),
            config_enable("lzma", "minidebuginfo"),
            config_enable("debug", "conservative_checks"),
            config_enable("debug", "debug"))

def install():
    installd()
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
