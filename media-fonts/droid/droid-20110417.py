metadata = """
summary @ A font created by Ascender Corporation for use by the Open Handset Alliance platform, Android.
homepage @ http://code.google.com/android/
license @ Apache
src_url @ ftp://ftp.archlinux.org/other/community/ttf-droid/ttf-droid.tar.xz
arch @ ~x86
"""

depends = """
runtime @ media-fonts/encodings x11-apps/mkfontdir media-libs/fontconfig x11-apps/mkfontscale
"""

standard_procedure = False
srcdir = "ttf-droid"

def install():
    makedirs("/usr/share/fonts/%s" % name)
    insinto("*.ttf", "/usr/share/fonts/%s" % name)

def post_install():
    # TODO: we need a helper that manages font related post_install jobs
    notify("updating font cache...")
    system("fc-cache -f ")
    system("mkfontscale /usr/share/fonts/droid")
    system("mkfontdir /usr/share/fonts/droid")
