metadata = """
summary @ A network utility to retrieve files from the Web
homepage @ http://www.gnu.org/software/wget/wget.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
options @ ipv6 idn debug nls ssl gnutls ntlm
"""

depends = """
runtime @ sys-libs/glibc
"""
opt_runtime = """
idn @ net-dns/libidn
nls @ sys-devel/gettext
ssl @
    gnutls @ net-libs/gnutls || dev-libs/openssl
    ntlm @ dev-libs/openssl
"""

def configure():
    myconf = ""
    if opt("ssl"):
        if opt("gnutls"):
            myconf += " --with-ssl=\"gnutls\" "
        else:
            myconf += " --with-ssl=\"openssl\" "
    else:
        notify("*** ssl option is highly recommended but you disabled it ***")
        myconf += " --without-ssl "
    
    if opt("ntlm"):
        if opt("gnutls"):
            import lpms
            lpms.terminate("*** You can not use ntlm and gnutls options together, compilation is going to fail ***")

    # fix glibc-2.16 build issue
    system("sed -i -e '/gets is a/d' lib/stdio.in.h")
    conf(
    config_enable("ssl", "opie"),
    config_enable("ssl", "digest"),
    config_enable("debug"),
    config_enable("ipv6"),
    config_enable("idn", "iri"),
    config_enable("ntlm"),
    config_enable("nls"), myconf)

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "COPYING", "ChangeLog*", "NEWS", "README", "MAILING-LIST")
