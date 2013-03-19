metadata = """
summary @ Adobe Flash Player
homepage @ http://get.adobe.com/flashplayer
license @ AdobeFlash-10.3 
src_url @ http://fpdownload.macromedia.com/get/flashplayer/pdc/$version/install_flash_player_11_linux.x86_64.tar.gz
http://www.adobe.com/products/eulas/pdfs/PlatformClients_PC_WWEULA_Combined_20100108_1657.pdf
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 media-libs/fontconfig dev-libs/nss sys-libs/glibc
"""

get("gnome2_utils")

standard_procedure = False

def install():
    insfile("../libflashplayer.so", "/usr/lib/mozilla/plugins/libflashplayer.so")
    insexe("../usr/bin/flash-player-properties", "/usr/bin/flash-player-properties")

    for item in ('16x16', '22x22', '24x24', '32x32', '48x48'):
        insfile("../usr/share/icons/hicolor/%s/apps/flash-player-properties.png" % item, 
                "/usr/share/icons/hicolor/%s/apps/flash-player-properties.png" %  item)

    insfile("../usr/share/applications/flash-player-properties.desktop",
            "/usr/share/applications/flash-player-properties.desktop")

    insfile("%s/mms.cfg" % filesdir, "/etc/adobe/mms.cfg")

    insfile("%s/PlatformClients_PC_WWEULA_Combined_20100108_1657.pdf" % src_cache, \
            "/usr/share/licenses/%s/LICENSE.pdf" % name)

def post_install():
    gnome2_icon_cache_update()
    notify("If you have an NVIDIA card that supports libvdpau or Broadcom Crystal HD chips,")
    notify("uncomment EnableLinuxHWVideoDecode=1 from /etc/adobe/mms.cfg.")
    notify("If you run into problems, please contact nVidia or Broadcom along with your system config info / driver version.")
 
