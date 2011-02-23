metadata = """
summary @ Msn messenger
license @ GPL-2
homepage @ www.emesene.org
src_url @ http://garr.dl.sourceforge.net/project/$name/$name-$version/$name-$version.tar.gz
"""

standart_procedure = False

def build():
    system("python setup.py build_ext -i")

def install():
    install_path = "/usr/share/%s" % pkgname
    insinto("*", install_path)
    rmdir(install_path+"/build")
    makesym(joinpath(install_path, pkgname), "/usr/bin/%s" % pkgname)
