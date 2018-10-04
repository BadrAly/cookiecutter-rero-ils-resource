# -*- coding: utf-8 -*-
#
# This file is part of RERO ILS.
# Copyright (C) 2018 RERO.
#
# RERO ILS is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# RERO ILS is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RERO ILS; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

resource_name = '{{ cookiecutter.resource_name }}'
pid_type = '{{ cookiecutter.pid_type }}'

if not re.match(MODULE_REGEX, resource_name):
    print(
        'ERROR: {esource_name} is not a valid Python module name!'.format(
            resource_name=resource_name
        )
    )
    # exits with status 1 to indicate failure
    sys.exit(1)

if len(pid_type) > 4:
    print('ERROR: pid_type to long {pid_len}>4'.format(pid_len=len(pid_type)))
    # exits with status 1 to indicate failure
    sys.exit(1)
