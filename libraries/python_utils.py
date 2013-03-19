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

import glob
import lpms
from lpms.utils import executable_path
from lpms.exceptions import BuiltinError


def set_python_binary(kwargs):
    # Use default python executable if python_version keyword is not given
    python_binary = executable_path("python")
    if "python_version" in kwargs:
        python_binary += kwargs["python_version"]
        if executable_path(python_binary) is None:
            raise BuiltinError("%s could not found." % python_binary)
    return python_binary


def python_utils_configure(*params, **kwargs):
    '''Configures the package using setup.py configure command'''
    python_binary = set_python_binary(kwargs)
    if not system("%s -B setup.py configure %s" % (python_binary, " ".join(params))):
        error("configuration failed.")
        lpms.terminate()


def python_utils_build(*params, **kwargs):
    '''Builds the package by running setup.py build with given parameters'''
    python_binary = set_python_binary(kwargs)
    if not system("%s -B setup.py build %s" % (python_binary, " ".join(params))):
        error("building failed.")
        lpms.terminate()

def python_utils_install(*params, **kwargs):
    '''Installs the package with given parameters'''
    python_binary = set_python_binary(kwargs)
    if not system("%s -B setup.py install --root=%s \
            --no-compile -O0 %s" % (python_binary, install_dir, " ".join(params))):
        error("installation failed.")
        lpms.terminate()

    # This part is borrowed from PiSi
    # BEGIN
    doc_files = ('AUTHORS', 'CHANGELOG', 'CONTRIBUTORS', 'COPYING*', 'COPYRIGHT',
            'Change*', 'KNOWN_BUGS', 'LICENSE', 'MAINTAINERS', 'NEWS',
            'README*', 'PKG-INFO')

    for doc_file in doc_files:
        for doc in glob.glob(doc_file):
            if not isempty(doc):
                insdoc(doc)
    # END
