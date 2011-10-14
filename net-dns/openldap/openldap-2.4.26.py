metadata = """
summary @ Lightweight Directory Access Protocol (LDAP) client libraries
homepage @ http://www.openldap.org/
license @ custom
src_url @ ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-$version.tgz
arch @ ~x86
options @ icu berkdb perl ssl gnutls tcpd sasl odbc iodbc debug ipv6 syslog 
"""

depends = """
runtime @ sys-libs/glibc
build @ sys-apps/groff
"""

opt_runtime = """
sasl @ dev-libs/cyrus-sasl
tcpd @ sys-apps/tcp-wrappers
icu @ dev-libs/icu
ssl @
    gnutls @ net-libs/gnutls || dev-libs/openssl
perl @ dev-lang/perl
berkdb @ sys-libs/db
odbc @ 
    iodbc @ dev-db/libiodbc || dev-db/unixODBC
"""

def prepare():
    sed("""-i 's|-m 644 $(LIBRARY)|-m 755 $(LIBRARY)|' libraries/{liblber,libldap,libldap_r}/Makefile.in""")
    sed("""-i 's|#define LDAPI_SOCK LDAP_RUNDIR LDAP_DIRSEP "run" LDAP_DIRSEP "ldapi"|#define LDAPI_SOCK LDAP_DIRSEP "run" LDAP_DIRSEP "openldap" LDAP_DIRSEP "ldapi"|' include/ldap_defaults.h""")
    sed("""-i 's|%LOCALSTATEDIR%/run|/run/openldap|' servers/slapd/slapd.conf""")
    sed("""-i 's|-$(MKDIR) $(DESTDIR)$(localstatedir)/run|-$(MKDIR) $(DESTDIR)/run/openldap|' servers/slapd/Makefile.in""")

def configure():
    if opt("icu"):
        export("ac_cv_header_unicode_utypes_h", "yes")
    else:
        export("ac_cv_header_unicode_utypes_h", "no")

    myconf = ""
    if opt("berkdb"):
        myconf += " --enable-bdb --enable-hdb "
    else:
        warn("You have disabled berkdb, that means you can only use remote-backends!")
        myconf += " --disable-bdb --disable-hdb "

    if opt("perl"):
        myconf += " --enable-perl=mod "
    
    if opt("ssl"):
        ssl_lib = "openssl"
        if opt("gnutls"):
            ssl_lib = "gnutls"
    else:
        ssl_lib = "no"
    myconf += " --with-tls=%s " % ssl_lib

    if opt("odbc"):
        odbc_lib = "unixodbc"
        myconf += " --enable-sql=mod "
        if opt("iodbc"):
            odbc_lib = "iodbc"
        myconf += " --with-odbc=%s " % odbc_lib

    conf("--enable-crypt",
        "--enable-dynamic",
        "--with-threads",
        config_enable("ipv6"),
        config_enable("syslog"),
        config_enable("debug"),
        config_enable("tcpd", "wrappers"),
        config_enable("sasl", "cyrus-sasl"),
        config_enable("sasl", "spasswd"),
        myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makesym("liblber.so", "/usr/lib/liblber.so.2")
    makesym("libldap.so", "/usr/lib/libldap.so.2")
    insdoc("ANNOUNCEMENT", "CHANGES", "COPYRIGHT", "README", "LICENSE")
    insexe("%s/slapd" % filesdir, "/etc/rc.d/slapd")
    insfile("%s/slapd.default" % filesdir, "/etc/conf.d/slapd")
    makedirs("/var/lib/openldap")
    makedirs("/etc/openldap/slapd.d")

def post_install():
    setmod("640", "/etc/openldap/{slapd.conf,DB_CONFIG.example}")
    setowner("root:439", "/etc/openldap/{slapd.conf,DB_CONFIG.example}")
    system("groupadd -g 439 ldap &>/dev/null")
    system("useradd -u 439 -g ldap -d /var/lib/openldap -s /bin/false ldap &>/dev/null")
    system("chown -R ldap:ldap /var/lib/openldap &>/dev/null")

#def post_remove():
#    system("userdel ldap >/dev/null 2>&1")
#    system("groupdel ldap >/dev/null 2>&1")
