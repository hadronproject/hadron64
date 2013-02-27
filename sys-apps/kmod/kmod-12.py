metadata = """
summary @ Linux kernel module handling
homepage @ http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary
license @ LGPL-2
src_url @ ftp://ftp.kernel.org/pub/linux/utils/kernel/$name/$fullname.tar.xz
options @ zlib xz static-libs debug
arch @ ~x86_64
"""

depends = """
conflict @ sys-apps/module-init-tools
"""

opt_runtime = """
xz @ >=app-arch/xz-5.0.4
zlib @ >=sys-libs/zlib-1.2.6
"""

def configure():
    raw_configure("-prefix=/usr",
            "--bindir=/bin",
            "--libdir=/usr/lib",
            "--disable-manpages",
            config_with("xz"),
            config_with("zlib"),
            config_enable("debug"),
            config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    for target in ("depmod", "insmod", "modinfo", "modprobe", "rmmod"):
        makesym("/bin/kmod", "/sbin/%s" % target)

    for target in ("lsmod", "modinfo"):
        makesym("kmod", "/bin/%s" % target)

    makedirs("/etc/depmod.d")
    makedirs("/etc/modprobe.d")
    makedirs("/usr/lib/depmod.d")
    makedirs("/usr/lib/modprobe.d")

    usb_load_ehci_first = """
softdep ohci_hcd pre: ehci_hcd
softdep uhci_hcd pre: ehci_hcd
    """
    echo(usb_load_ehci_first, "/usr/lib/modprobe.d/usb-load-ehci-first.conf")


