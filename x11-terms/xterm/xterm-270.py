metadata = """
summary @ X Terminal Emulator
homepage @ http://invisible-island.net/xterm/
license @ custom
src_url @ ftp://invisible-island.net/xterm/$fullname.tgz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXft x11-libs/libXaw sys-libs/ncurses x11-misc/luit x11-misc/xbitmaps
"""

def configure():
    conf("--libdir=/etc \
            --mandir=/usr/share/man \
            --with-app-defaults=/usr/share/X11/app-defaults/ \
            --with-x \
            --disable-full-tgetent \
            --disable-imake \
            --enable-ansi-color \
            --enable-88-color \
            --enable-256-color \
            --enable-broken-osc \
            --enable-broken-st \
            --enable-load-vt-fonts \
            --enable-i18n \
            --enable-wide-chars \
            --enable-doublechars \
            --enable-warnings \
            --enable-tcap-query \
            --enable-logging \
            --enable-dabbrev \
            --enable-freetype \
            --enable-luit \
            --enable-mini-luit \
            --enable-narrowproto \
            --enable-exec-xterm \
            --with-tty-group=tty")

def install():
    raw_install("DESTDIR=%s" % install_dir)
