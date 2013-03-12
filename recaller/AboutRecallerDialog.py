# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('recaller')

import logging
logger = logging.getLogger('recaller')

from recaller_lib.AboutDialog import AboutDialog

# See recaller_lib.AboutDialog.py for more details about how this class works.
class AboutRecallerDialog(AboutDialog):
    __gtype_name__ = "AboutRecallerDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutRecallerDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

