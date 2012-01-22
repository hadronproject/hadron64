# Copyright 2009 - 2012 Burak Sezer <purak@hadronproject.org>
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

import os

import lpms

binaries = {
        "tar": "/bin/tar"
        }

def tar_extract(archive_name, partial=None):
    if not os.access(binaries["tar"], os.X_OK):
        error("%s seems problematic." % binaries["tar"])
        lpms.terminate()
    
    command = "%s xf %s/%s -C %s" % (
            binaries['tar'], 
            src_cache,
            archive_name, 
            dirname(build_dir)
            )
    
    if partial:
        command = "%s xf %s/%s %s -C %s" % (
                binaries['tar'], 
                src_cache, 
                archive_name, 
                " ".join(partial), 
                dirname(build_dir)
                )
    
    if not system(command):
        error("unpack failed.")
        lpms.terminate()
