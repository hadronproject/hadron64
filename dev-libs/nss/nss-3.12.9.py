metadata = """
summary @ Mozilla Network Security Services
homepage @ http://www.mozilla.org/projects/security/pki/nss/
license @ MPL GPL
src_url @ http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_12_9_WITH_CKBI_1_82_RTM/src/nss-3.12.9.with.ckbi.1.82.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/nspr dev-db/sqlite sys-libs/zlib
build @ dev-lang/perl
"""

def prepare():
    makedirs("mozilla/dist/pkgconfig")
    copy("%s/nss.pc.in" % filesdir, "mozilla/dist/pkgconfig/nss.pc.in")
    copy("%s/nss-config.in" % filesdir, "mozilla/dist/pkgconfig/nss-config.in")
    if not system("%s/generate-pc-config.sh" % filesdir):
        notify("patladi")

def build():
    cd("mozilla/security/nss/lib/ckfw/builtins")
    make("generate")
    
    cd(build_dir)

    system("unset CFLAGS")
    system("unset CXXFLAGS")
    export("BUILD_OPT", "1")
    export("NSS_ENABLE_ECC", "1")
    export("NSS_USE_SYSTEM_SQLITE", "1")
    export("OPT_FLAGS","%s -g -fno-strict-aliasing" % get_env("CFLAGS"))
    
    export("PKG_CONFIG_ALLOW_SYSTEM_LIBS", "1")
    export("PKG_CONFIG_ALLOW_SYSTEM_CFLAGS", "1")
    export("NSPR_INCLUDE_DIR", "/usr/include/nspr")

    make("-C mozilla/security/coreconf")
    make("-C mozilla/security/dbm")
    make("-C mozilla/security/nss")

def install():
    cd("mozilla")

    for binary in ["certutil", "modutil", "pk12util", "signtool", "ssltap"]:
        insinto("dist/Linux*/bin/%s" % binary, "/usr/bin", sym=False)

    for lib in ["*.a","*.chk","*.so"]:
        insinto("dist/Linux*/lib/%s" % lib, "/usr/lib/nss", sym=False)

    # Headers
    for header in ["dist/private/nss/*.h","dist/public/nss/*.h"]:
        insinto(header, "/usr/include/nss", sym=False)

    # Drop executable bits from headers
    setmod("0644", "%s/usr/include/nss/*.h" % install_dir)

    # Install nss-config and nss.pc
    insfile("dist/pkgconfig/nss.pc", "/usr/lib/pkgconfig/nss.pc")
    insexe("dist/pkgconfig/nss-config", "/usr/bin/nss-config")

    for lib in ('libssl3.so', 'libsmime3.so', 'libnssutil3.so', 'libnss3.so', 
            'libsoftokn3.so', 'libfreebl3.so', 'libnssckbi.so', 'libnssdbm3.so'):
        makesym("nss/%s" % lib, "/usr/lib/%s" % lib)
