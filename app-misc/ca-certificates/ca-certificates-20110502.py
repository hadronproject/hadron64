metadata = """
summary @ Common ca-certificates
homepage @ http://packages.qa.debian.org/c/ca-certificates.html
license @ MPL
src_url @ http://ftp.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_$version+nmu1.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash dev-libs/openssl sys-apps/debianutils
          sys-apps/findutils sys-apps/coreutils sys-apps/sed
"""

srcdir = name + "-" + version + "+nmu1"

import glob

def install():
    for i in ("/etc/ca-certificates/update.d", "/usr/sbin",
            "/usr/share/ca-certificates", "/etc/ssl/certs"):
        makedirs(i)

    raw_install("DESTDIR=%s" % install_dir)

    mycontent = ""
    for d in ls("%s/usr/share/ca-certificates" % install_dir):
        for crt in glob.glob("%s/usr/share/ca-certificates/%s/*.crt" % (install_dir, d)):
            mycontent += crt.split(install_dir)[1]+"\n"

    #system("echo \"%s\" >> %s/etc/ca-certificates.conf" % (mycontent, install_dir))
    system("ln -s /usr/share/ca-certificates/*/*.crt %s/etc/ssl/certs/" % install_dir)

def post_install():
    system("lpms -c ca-certificates | grep crt | sed 's#/usr/share/ca-certificates/##g' | grep -Ev \"\*\.crt\" > /etc/ca-certificates.conf")
    system("update-ca-certificates")
