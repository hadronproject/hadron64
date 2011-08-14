metadata = """
summary @ An object oriented language for quick and easy programming
homepage @ http://www.ruby-lang.org/en
src_url @ ftp://ftp.ruby-lang.org/pub/$name/1.9/$name-1.9.2-p290.tar.bz2
license @ GPL-2
options @ doc
"""

srcdir = name+"-"+".".join(version.split(".")[:-1])+"-"+"p"+version.split(".")[-1]

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
