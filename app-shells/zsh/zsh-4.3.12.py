metadata = """
summary @ A POSIX compliant shell
homepage @ http://www.zsh.org/
license @ ZSH
src_url @ ftp://ftp.zsh.org/pub/$fullname.tar.bz2
arch @ ~x86
options @ gdbm pcre maildir caps debug lpms-completion
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_runtime = """
gdbm @ sys-libs/gdbm
"""

def configure():
    myconf = ""
    if opt("debug"):
        myconf += " --enable-zsh-debug --enable-zsh-mem-debug \
                --enable-zsh-mem-warning --enable-zsh-secure-free --enable-zsh-hash-debug "

    conf(
    "--enable-multibyte",
    "--enable-maildir-support",
    "--enable-function-subdirs",
        config_enable("pcre"),
        config_enable("caps", "cap"),
        config_enable("gdbm"),
        config_enable("maildir", "maildir-support"),
    "--enable-zsh-secure-free",
    "--enable-etcdir=/etc/zsh",
    "--bindir=/bin",
    "--enable-zshenv=/etc/zsh/zshenv",
    "--enable-zlogin=/etc/zsh/zlogin",
    "--enable-zlogout=/etc/zsh/zlogout",
    "--enable-zprofile=/etc/profile",
    "--enable-zshrc=/etc/zsh/zshrc", myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENCE", "META-FAQ", "NEWS", "README", "config.modules")

    if opt("lpms-completion"):
        insfile("%s/_lpms" % filesdir, "/usr/share/zsh/%s/functions/Completion/Linux/_lpms" % version)
