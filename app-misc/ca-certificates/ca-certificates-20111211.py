metadata = """
summary @ Common ca-certificates
homepage @ http://packages.qa.debian.org/c/ca-certificates.html
license @ MPL
src_url @ http://ftp.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash dev-libs/openssl sys-apps/debianutils
          sys-apps/findutils sys-apps/coreutils sys-apps/sed
"""

def install():
    import glob
    
    for i in ("/etc/ca-certificates/update.d", "/usr/sbin",
            "/usr/share/ca-certificates", "/etc/ssl/certs"):
        makedirs(i)

    raw_install("DESTDIR=%s" % install_dir)

    mycontent = ""
    for d in ls("%s/usr/share/ca-certificates" % install_dir):
        for crt in glob.glob("%s/usr/share/ca-certificates/%s/*.crt" % (install_dir, d)):
            mycontent += crt.split(install_dir+"/usr/share/ca-certificates/")[1]+"\n"


    echo("%s" % mycontent, "/etc/ca-certificates.conf")

def post_install():
    # FIXME: lpms must do something about external command fails
    if not system("update-ca-certificates"):
        error("update-ca-certificates failed.")
