metadata = """
summary @ The elementary icons is an icon theme designed to be smooth, sexy, clear, and efficient.
homepage @ https://launchpad.net/elementaryicons
license @ GPL-2
src_url @ http://launchpad.net/elementaryicons/2.0/$version/+download/$fullname.tar.gz
options @ monochrome
arch @ ~x86_64
"""

depends = """
runtime @ gnome-base/librsvg
"""

standard_procedure = False

srcdir = "elementary-icon-theme"

def install():
    makedirs("/usr/share/icons")

    for i in ('elementary', 'elementary-mono-dark'):
        if i == "elementary-mono-dark" and not opt("monochrome"):
            pass
        copytree("%s/%s" % (build_dir, i), "/usr/share/icons/%s" % i)
