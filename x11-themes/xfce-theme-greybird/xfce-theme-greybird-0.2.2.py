metadata = """
summary @ A low saturation Xfce theme, introduced in the release of Xubuntu 11.04
homepage @ http://shimmerproject.org/projects/greybird/
license @ GPL-3 CCPL
arch @ ~x86_64
"""

depends = """
runtime @ x11-themes/gtk-engines-murrine
"""

standard_procedure = False

def prepare():
    system('git clone "git://github.com/shimmerproject/Greybird.git"')

    for i in ('.gitignore', '.git'):
        rmdir("Greybird/%s" % i)

def install():
    for d in ('/usr/share/themes/',
            '/usr/share/backgrounds/',
            '/usr/share/xfce4/backdrops/'):
        makedirs(d)

    insfile("Greybird/backdrops/greybird-wall-1920x1200.png", "/usr/share/backgrounds/Greybird.png")
    system("rm -rf %s/Greybird/backdrops/" % build_dir)

    copytree("Greybird", "/usr/share/themes/Greybird")

    makesym("/usr/share/backgrounds/Greybird.png", "/usr/share/xfce4/backdrops/Greybird.png")
