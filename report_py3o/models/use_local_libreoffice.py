# -*- coding: utf-8 -*-
#
# Copyright 2017 Taŭga Tecnologia
#    Ari Caldeira <ari.caldeira@tauga.com.br>
# License AGPL-3 or later (http://www.gnu.org/licenses/agpl)
#

from __future__ import division, print_function, unicode_literals

import os

libreoffice_present = os.path.expanduser('~/.py3o_libreoffice_present')

if os.path.exists(libreoffice_present):
    USE_LOCAL_LIBREOFFICE = open(libreoffice_present).read() == 'True'
else:
    USE_LOCAL_LIBREOFFICE = False
    try:
        import sh
        import tempfile

        sh.libreoffice('--headless', '--version')

        USE_LOCAL_LIBREOFFICE = True

    except:
        pass

    open(libreoffice_present, 'w').write(str(USE_LOCAL_LIBREOFFICE))
