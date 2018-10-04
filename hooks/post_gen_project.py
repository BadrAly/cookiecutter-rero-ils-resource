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

import click

name = '{{ cookiecutter.name }}'
resource_name = '{{ cookiecutter.resource_name }}'
class_name = '{{ cookiecutter.class_name }}'
pid_type = '{{ cookiecutter.pid_type }}'
app_name = '{{ cookiecutter.app_name }}'

# imports                ------------------------------------------------------
click.secho(
    'Please add following to the config.py file of: ',
    fg='green',
    nl=False
)
click.echo(app_name)
click.echo(
    'from .modules.{resource_name}.api import {class_name}'.format(
        resource_name=resource_name,
        class_name=class_name)
)
click.echo()

# RECORDS_REST_ENDPOINTS ------------------------------------------------------
click.secho(
    'Please add following to the config.py file section: ',
    fg='green',
    nl=False
)
click.echo('RECORDS_REST_ENDPOINTS')
msg = """    {name}=dict(
        pid_type='{pid_type}',
        pid_minter='{name}_id',
        pid_fetcher='{name}_id',
        search_class=RecordsSearch,
        search_index='{resource_name}',
        search_type=None,
        record_serializers={o}
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        {c},
        search_serializers={o}
            'application/rero+json': ('rero_ils.modules.serializers'
                                      ':json_v1_search'),
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        {c},
        list_route='/{resource_name}/',
        item_route='/{resource_name}/<pid(org):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        search_factory_imp='rero_ils.query:and_search_factory'
    ),
""".format(
    name=name,
    resource_name=resource_name,
    pid_type=pid_type,
    o='{',
    c='}'
)
click.echo(msg)

# RECORDS_UI_ENDPOINTS --------------------------------------------------------
click.secho(
    'Please add following to the config.py file section: ',
    fg='green',
    nl=False
)
click.echo('RECORDS_UI_ENDPOINTS')
msg = """    '{name}': {o}
        'pid_type': '{pid_type}',
        'route': '/{resource_name}/<pid_value>',
        'template': '{app_name}/detailed_view_{resource_name}.html',
        'record_class': '{app_name}.modules.{resource_name}.api:{class_name}',
        'permission_factory_imp':
            'reroils_record_editor.permissions.cataloguer_permission_factory'
    {c}
""".format(
    name=name,
    resource_name=resource_name,
    class_name=class_name,
    pid_type=pid_type,
    app_name=app_name,
    o='{',
    c='}'
)
click.echo(msg)