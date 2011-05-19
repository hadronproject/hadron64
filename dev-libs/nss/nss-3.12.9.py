metadata = """
summary @ Mozilla Network Security Services
homepage @ http://www.mozilla.org/projects/security/pki/nss/
license @ MPL GPL
src_url @ http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_12_9_WITH_CKBI_1_82_RTM/src/nss-3.12.9.with.ckbi.1.82.tar.gz
arch @ ~x86
"""

import os

#def prepare():
#    patch(level=1)

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
   #export("NSPR_LIB_DIR",
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
    insfile("%s/nss.pc.in" % filesdir, "/usr/lib/pkgconfig/nss.pc")
    insexe("%s/nss-config.in" % filesdir, "/usr/bin/nss-config")
