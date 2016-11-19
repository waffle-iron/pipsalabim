# -*- coding: utf-8 -*-
#
#   This file is part of Pip Sala Bim.
#   Copyright (C) 2016, Pip Sala Bim Developers.
#
#   Please refer to AUTHORS.rst for a complete list of Copyright holders.
#
#   Pip Sala Bim is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Pip Sala Bim is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see http://www.gnu.org/licenses.
"""
``pipsalabim.api.update`` is a module implementing the update command.

"""
from __future__ import absolute_import, print_function

from ..core.cache import (download_json_database, stdlibjson, pypijson,
                          stdlibjsonfile, pypijsonfile)


def main(*args, **kwargs):
    """
    Update databases from PyPIContents.

    :return: an exit status.

    .. versionadded:: 0.1.0
    """

    print('Updating the standard library database ...')
    if download_json_database(stdlibjsonfile, stdlibjson):
        print('Success!\n')
    else:
        print('There was an error!\n')

    print('Updating the PyPIContents database ...')
    if download_json_database(pypijsonfile, pypijson):
        print('Success!\n')
    else:
        print('There was an error!\n')

    return 0