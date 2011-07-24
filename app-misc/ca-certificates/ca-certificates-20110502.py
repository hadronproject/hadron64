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

import glob

def install():
    # FIXME: UnicodeEncodeError
    # lpms has serious unicode problems. i am dealing with it.
    for i in "TÜBİTAK_UEKAE_Kök_Sertifika_Hizmet_Sağlayıcısı_-_Sürüm_3.crt", \
            "EBG_Elektronik_Sertifika_Hizmet_Sağlayıcısı.crt", \
            "AC_Raíz_Certicámara_S.A..crt", \
            "NetLock_Arany_=Class_Gold=_Főtanúsítvány.crt":
                system("rm -r %s/mozilla/%s" % (build_dir, i))


    for i in ("/etc/ca-certificates/update.d", "/usr/sbin", 
            "/usr/share/ca-certificates", "/etc/ssl/certs"):
        makedirs(i)
        
    raw_install("DESTDIR=%s" % install_dir)
    
    mycontent = ""
    for d in ls("%s/usr/share/ca-certificates" % install_dir):
        for crt in glob.glob("%s/usr/share/ca-certificates/%s/*.crt" % (install_dir, d)):
            mycontent += crt.split(install_dir)[1]+"\n"

    system('echo "%s" > %s/etc/ca-certificates.conf' % (mycontent, install_dir))
