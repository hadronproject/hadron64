# waf utils for lpms

import lpms

from lpms import out

export("JOBS", get_env("JOBS")[2:])

if os.access("waf", os.R_OK) and os.access("waf", os.X_OK):
    waf_exists = True
else:
    waf_exists = False

def waf_configure(*args):
    if waf_exists:
        if not system("./waf configure --prefix=/usr %s" % " ".join(args)):
            out.error("waf configure failed.")
            lpms.terminate()
    else:
        conf()

def waf_build(*args, **kwargs):
    if "j" in kwargs:
        export("JOBS", kwargs["j"])

    if waf_exists:
        if not system("./waf build"):
            out.error("waf build failed.")
            lpms.terminate()
    else:
        make()

def waf_install():
    if waf_exists:
        if not system("./waf install --destdir=%s" %  install_dir):
            out.error("waf install failed.")
            lpms.terminate()
    else:
        raw_install("DESTDIR=%s" % install_dir)
