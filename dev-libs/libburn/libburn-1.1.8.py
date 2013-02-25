metadata = """
summary @ Library for reading, mastering and writing optical discs
homepage @ http://libburnia.pykix.org/
license @ GPL-2
src_url @ http://files.libburnia-project.org/releases/$fullname.tar.gz
options @ static-libs track-src-odirect debug
arch @ ~x86_64
"""

def configure():
    conf(config_enable("static-libs", "static"),
            config_enable("track-src-odirect"),
            "--disable-libcdio",
            "--disable-ldconfig-at-install",
            config_enable("debug")
    )

install = lambda: installd()
