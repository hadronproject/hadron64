metadata = """
summary @ A powerful light-weight programming language designed for extending applications.
homepage @ http://www.lua.org
license @ MIT
src_url @ http://www.lua.org/ftp/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/readline
"""

def prepare():
    patch("liblua.so.patch", level=1)

def build():
    flags = "%s -fPIC" % get_env("CFLAGS")
    make("MYCFLAGS=\"%s\" linux" % flags)

def install():
    raw_install("INSTALL_DATA='cp -d' TO_LIB='liblua.a liblua.so liblua.so.5.2' LUA_SO=liblua.so  INSTALL_TOP='%s/usr' INSTALL_MAN='%s/usr/share/man/man1' linux install" % (install_dir, install_dir))
    #raw_install('INSTALL_TOP="%s/usr"' % install_dir)
    #makesym("/usr/lib/liblua.so.5.1", "/usr/lib/liblua.so")
    #insinto("/usr/share/lua/5.1", "etc/strict.lua")
