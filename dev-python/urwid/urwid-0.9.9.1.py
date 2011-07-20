metadata = """
summary @ Urwid is a curses-based user interface library
homepage @ http://excess.org/urwid/
license @ GPL
src_url @ http://excess.org/urwid/urwid-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/python
"""

srcdir = fullname+"/src/urwid-%s" % version

standard_procedure = False

def install():
    system("python setup.py install --prefix=/usr --root=%s" % install_dir)
