# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('recaller')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('recaller')

from recaller_lib import Window
from recaller.AboutRecallerDialog import AboutRecallerDialog
from recaller.PreferencesRecallerDialog import PreferencesRecallerDialog

# See recaller_lib.Window.py for more details about how this class works
class RecallerWindow(Window):
    __gtype_name__ = "RecallerWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(RecallerWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutRecallerDialog
        self.PreferencesDialog = PreferencesRecallerDialog

        # Code for other initialization actions should be added here.

