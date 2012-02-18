metadata = """
summary @ A dark, smooth Xfce theme, introduced in the release of Xubuntu 9.10
homepage @ http://shimmerproject.org/projects/albatross/
license @ GPL-3 CCPL
arch @ ~x86
"""

depends = """
runtime @ x11-themes/gtk-engines-murrine
"""

standard_procedure = False

def prepare():
    system('git clone "git://github.com/shimmerproject/Albatross.git"')

    for i in ('.gitignore', '.git', 'shearwater', 'xsplash', 'usplash'):
        rmdir("Albatross/%s" % i)

def install():
    for d in ('/usr/share/themes/',
            '/usr/share/backgrounds/',
            '/usr/share/xfce4/backdrops/'):
        makedirs(d)

    insfile("Albatross/backdrops/albatross-2009-10.png", "/usr/share/backgrounds/Albatross.png")
    system("rm -rf %s/Albatross/backdrops/" % build_dir)

    copytree("Albatross", "/usr/share/themes/Albatross")

    makesym("/usr/share/backgrounds/Albatross.png", "/usr/share/xfce4/backdrops/Albatross.png")
