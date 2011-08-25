metadata = """
summary @ A simple GTK+ Image Viewer
homepage @ http://mirageiv.berlios.de/
license @ GPL
src_url @ http://download.berlios.de/mirageiv/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-python/pygtk dev-util/desktop-file-utils
"""

def configure():
    pass

def build():
    system("python setup.py build")
    pass

def install():
    system("python setup.py install --root=%s" % install_dir)

def post_install():
    system("update-desktop-database -q")
