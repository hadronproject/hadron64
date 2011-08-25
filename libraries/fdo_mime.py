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

from lpms import out
from lpms import shelltools

def desktop_database_update(*args):
    parameters = "-q"
    if args:
        parameters = " ".join(args)

    out.notify("updating desktop database...")
    if not shelltools.system("update-desktop-database %s" % parameters):
        out.write(out.color("\tFAILED", "red"))
