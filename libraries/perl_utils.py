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

import os
import lpms

def fixlocalpod():
    if not system("find %s -type f -name perllocal.pod -delete" % install_dir):
        warn("fixlocalpod failed.")
        return False
    else:
        if not system("find %s -depth -mindepth 1 -type d -empty -delete" % install_dir):
            warn("fixlocalpod failed.")
            return False
    return True

def perl_utils_configure(*params):
    '''Configures the package using perl specific ways'''
    export("PERL_MM_USE_DEFAULT", "1")

    if os.path.isfile("Build.PL"):
        if not system("perl Build.PL installdirs=vendor destdir=%s" % install_dir):
            error("configure failed.")
            lpms.terminate()
    else:
        if not system("perl Makefile.PL %s PREFIX=/usr \
                INSTALLDIRS=vendor DESTDIR=%s" % (" ".join(params), install_dir)):
            error("configure failed.")
            lpms.terminate()

def perl_utils_build(*params):
    '''Builds the package using make or perl Build commands'''
    if os.path.isfile("Makefile"):
        if not system("make %s" % " ".join(params)):
            error("make failed.")
            lpms.terminate()
    else:
        if not system("perl Build %s" % " ".join(params)):
            error("perl Build failed.")
            lpms.terminate()

def perl_utils_install(arg = "install"):
    '''Installs the package using make or perl Build install commands'''
    if os.path.isfile("Makefile"):
        if not system("make %s" % arg):
            error("make failed.")
            lpms.terminate()
    else:
        if not system("perl Build install"):
            error("perl install failed.")
            lpms.terminate()
