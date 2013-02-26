metadata = """
summary @ Common ca-certificates
homepage @ http://packages.qa.debian.org/c/ca-certificates.html
license @ MPL
src_url @ http://ftp.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash dev-libs/openssl sys-apps/debianutils
          sys-apps/findutils sys-apps/coreutils sys-apps/sed
"""

def install():
    import glob
    for item in ("/etc/ca-certificates/update.d", "/usr/sbin",
            "/usr/share/ca-certificates", "/etc/ssl/certs"):
        makedirs(item)
    raw_install("DESTDIR=%s" % install_dir)
    mycontent = ""
    for item in ls("/usr/share/ca-certificates"):
        for crt in glob.glob("%s/usr/share/ca-certificates/%s/*.crt" % (install_dir, item)):
            mycontent += crt.split(install_dir+"/usr/share/ca-certificates/")[1]+"\n"
    echo(mycontent, "/etc/ca-certificates.conf")

def post_install():
    # FIXME: lpms must do something about external command fails
    notify("Updating certificates. This might take a while...")
    #if not system("update-ca-certificates --fresh"):
    #    error("update-ca-certificates failed.")
