metadata = """
summary @ Data logging and graphing application
homepage @ http://www.rrdtool.org
license @ GPL-2
src_url @ http://oss.oetiker.ch/rrdtool/pub/$fullname.tar.gz
options @ lua perl ruby tcl python rrdcgi
arch @ ~x86_64
"""

depends = """
common @ >=media-libs/libpng-1.2.1 >=dev-libs/libxml2-2.6.31 >=x11-libs/cairo-1.4.6[svg] >=sys-libs/glib-2.12.12 >=media-libs/pango-1.17
build @ sys-apps/gawk
"""

opt_common = """
lua @ dev-lang/lua
perl @ dev-lang/perl
ruby @ dev-lang/ruby
tcl @ dev-lang/tcl
python @ dev-lang/python
"""

def prepare():
    patch(level=1)
    sed("-i '/PERLLD/s:same as PERLCC:same-as-PERLCC:' configure.ac")
    sed('-e "/^all-local:/s/ @COMP_PYTHON@//" -i bindings/Makefile.am')
    autoreconf()

def configure():
    export("RRDDOCDIR", "/usr/share/doc/rrdtool")
    conf("--disable-static",
            config_enable("rrdcgi"),
            config_enable("lua"),
            config_enable("lua", "lua-site-install"),
            config_enable("ruby"),
            config_enable("ruby", "ruby-site-install"),
            config_enable("perl"),
            config_enable("perl", "perl-site-install"),
            config_enable("--with-perl-options=INSTALLDIRS=vendor"),
            config_enable("tcl"),
            config_enable("python")
            )

install = lambda: (installd(), insdoc("COPYRIGHT"))
