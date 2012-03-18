# Copyright 2009 - 2011 Burak Sezer <purak@hadronproject.org>
#
# This file is part of main repository
#
# main repository is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# main repository is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with main repository.  If not, see <http://www.gnu.org/licenses/>.

import lpms

def xdg_icon_resource(theme="hicolor"):
    notify("updating xdg icon resource for %s theme" % theme)
    if not system("xdg-icon-resource forceupdate --theme %s" % theme, sandbox=False):
        warn("xdg-icon-resource failed.")

def desktop_database_update(*args):
    parameters = "-q"
    if args:
        parameters = " ".join(args)

    notify("updating desktop database...")
    if not system("update-desktop-database %s" % parameters, sandbox=False):
        write(out.color("\tFAILED", "red"))

def update_mime_database(*args):
    out.notify("updating mime database...")
    if not system("update-mime-database /usr/share/mime", sandbox=False):
        warn("update-mime-database failed.")
