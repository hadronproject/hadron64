metadata = """
summary @ Vi IMproved, an advanced text editor
homepage @ http://www.vim.org
license @ GPL-2
src_url @ ftp://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/ncurses dev-lang/python
build @ sys-libs/ncurses dev-lang/python
"""

srcdir = "vim73"

def prepare():
    echo('#define SYS_VIMRC_FILE "/etc/vimrc"', "src/feature.h")

def configure():
    conf("--with-modified-by=Hadron",
            "--with-compiledby=Hadron",
            "--enable-multibyte",
            "--enable-pythoninterp",
            "--enable-perlinterp",
            "--with-features=huge",
            "--with-tlib=ncurses",
            "--enable-gui=no")

def install():
    raw_install("VIMRCLOC=/etc DESTDIR=%s install" % install_dir)
    copy("%s/vimrc" % filesdir, "/etc/vimrc")
