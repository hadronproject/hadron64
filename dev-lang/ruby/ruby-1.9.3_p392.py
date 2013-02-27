metadata = """
summary @ An object oriented language for quick and easy programming
homepage @ http://www.ruby-lang.org/en
src_url @ ftp://ftp.ruby-lang.org/pub/ruby/ruby-1.9.3-p392.tar.gz
license @ GPL-2
options @ berkdb gdbm ssl ncurses readline doc yaml
arch @ ~x86_64
"""

depends = """
common @ sys-libs/zlib dev-libs/libffi
"""

opt_common = """
berkdb @ sys-libs/db
gdbm @ sys-libs/gdbm
ssl @ dev-libs/openssl
ncurses @ sys-libs/ncurses
readline @ sys-libs/readline
yaml @ dev-libs/libyaml
"""

srcdir = "ruby-1.9.3-p392"

# the patches from gentoo, thanks...

#def prepare():
#    for item in ("004_gfbsd7.patch", "005_no-undefined-ext.patch", "009_no-gems.patch"):
#        patch(item, location="%s/patches" % dirname(build_dir), level=1)
#    autoreconf()

def configure():
    conf("--enable-shared",
        "--enable-pthread",
        "--with-sitedir=/usr/lib/ruby/site_ruby",
        "--disable-rpath",
        config_enable("doc", "install-doc"),
        "--enable-ipv6",
        config_enable("debug"),
        config_with("berkdb", "dbm"),
        config_with("yaml", "psych"),
        config_with("gdbm"),
        config_with("ssl", "openssl"),
        config_with("ncurses", "curses"),
        "--enable-option-checking=no"
    )

def install():
    raw_install("DESTDIR=%s" % install_dir)
    if opt("doc"):
        raw_install("DESTDIR=%s install-doc install-capi" % install_dir)
