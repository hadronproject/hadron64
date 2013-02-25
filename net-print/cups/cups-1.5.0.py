metadata = """
summary @ The CUPS Printing System
homepage @ http://www.cups.org/
license @ GPL
src_url @ ftp://ftp.easysw.com/pub/cups/$version/$fullname-source.tar.bz2
arch @ ~x86_64
options @ ssl gnutls dbus jpeg pam perl png acl tiff usb X threads debug static-libs
"""

depends = """
build @ app-arch/gzip sys-libs/zlib sys-devel/autoconf
"""

opt_runtime = """
png @ media-libs/libpng
acl @ sys-apps/acl sys-apps/attr
pam @ sys-libs/pam
X @ x11-misc/xdg-utils
ssl @ 
    gnutls @ net-libs/gnutls || dev-libs/openssl
tiff @ media-libs/tiff
dbus @ sys-apps/dbus
jpeg @ media-libs/jpeg
perl @ dev-lang/perl
usb @ dev-libs/libusb:0
"""

#TODO: krb5 ldap perl

def configure():
    myconf = ""
    if opt("ssl"):
        if opt("gnutls"):
            myconf +=  " --enable-gnutls "
        else:
            myconf += " --enable-openssl "
    else:
        myconf += " --disable-gnutls --disable-openssl "

    if opt("gnutls"):
        if not opt("threads"):
            notify('*** "gnutls" option also needs "threads" option, enabling "threads" ***')
            myconf += " --enable-threads "
    
    aclocal("-I config-scripts")
    autoconf("-I config-scripts")
    conf(
    "--with-python",
    "--with-cups-user=daemon",
    "--with-cups-group=lp",
    "--enable-pam=yes",
    "--enable-raw-printing",
    config_enable("dbus"),
    config_enable("acl"),
    config_enable("debug"),
    config_enable("debug", "debug-guards"),
    config_enable("jpeg"),
    config_enable("pam"),
    config_enable("png"),
    config_enable("static-libs", "static"),
    config_enable("tiff"),
    config_enable("usb", "libusb"),
    "--with-dbusdir=/etc/dbus-1",
    "--disable-dnssd",
    "--with-php=/usr/bin/php-cgi", myconf)

def install():
    raw_install("BUILDROOT=%s install-headers install-libs" % install_dir)

    insexe("%s/cups" % filesdir, "/etc/rc.d/cups")
    insfile("%s/cups.logrotate" % filesdir, "/etc/logrotate.d/cups")
    insfile("%s/cups.pam" % filesdir, "/etc/pam.d/cups")
	
    system("touch %s/etc/cups/printers.conf" % install_dir)
    system("touch %s/etc/cups/classes.conf" % install_dir)
    system("touch %s/etc/cups/client.conf" % install_dir)
    system('echo "# see man client.conf" >> %s/etc/cups/client.conf' % install_dir)
    system("touch %s/etc/cups/subscriptions.conf" % install_dir)

    if not opt("X"):
        system("rm -fr %s/usr/share/applications" % install_dir)
