# waf utils for lpms

import lpms

from lpms import out

export("JOBS", get_env("JOBS")[2:])

def check_waf_binary():
    if os.access("waf", os.R_OK) and os.access("waf", os.X_OK):
        return True
    return False

def waf_configure(*args):
    if check_waf_binary():
        if not system("./waf configure --prefix=/usr %s" % " ".join(args)):
            out.error("waf configure failed.")
            lpms.terminate()
    else:
        conf()

def waf_build(*args, **kwargs):
    if "j" in kwargs:
        export("JOBS", kwargs["j"])

    if check_waf_binary():
        if not system("./waf build"):
            out.error("waf build failed.")
            lpms.terminate()
    else:
        make()

def waf_install():
    if check_waf_binary():
        if not system("./waf install --destdir=%s" %  install_dir):
            out.error("waf install failed.")
            lpms.terminate()
    else:
        raw_install("DESTDIR=%s" % install_dir)
