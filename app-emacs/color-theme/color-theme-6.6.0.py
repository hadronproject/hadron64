metadata = """
summary @ Emacs color theme
homepage @ http://www.nongnu.org/color-theme/
license @ GPL-2
src_url @ http://download.savannah.gnu.org/releases/$name/$name-$version.tar.gz
arch @ ~x86
"""

depends = """
common @ app-editors/emacs
"""

standard_procedure = False
srcdir             = "color-theme-6.6.0"

def install():
    insinto("*.el", "/usr/share/emacs/site-lisp/color-theme")
    insinto("themes", "/usr/share/emacs/site-lisp/color-theme")

