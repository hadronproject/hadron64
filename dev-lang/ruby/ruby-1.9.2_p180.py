metadata = """
summary @ An object oriented language for quick and easy programming
homepage @ http://www.ruby-lang.org/en
src_url @ ftp://ftp.ruby-lang.org/pub/$name/1.9/$name-$version.tar.bz2
license @ GPL-2
options @ doc
"""

version = "-".join(version.split("_"))
srcdir = name+"-"+version

def configure():
    conf("--enable-shared",
        "--enable-pthread",
        "--enable-shared",
        "--with-sitedir=/usr/lib/ruby/site_ruby",
        "--disable-rpath")

def install():
    raw_install("DESTDIR=%s install-nodoc" % install_dir)
    if opt("doc"):
        raw_install("DESTDIR=%s install-doc install-capi" % install_dir)
