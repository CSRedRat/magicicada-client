# ubuntuone.syncdaemon.platform.notification - User Notification
#
# Author: Eric Casteleijn <eric.casteleijn@canonical.com>
#
# Copyright 2011-2012 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# In addition, as a special exception, the copyright holders give
# permission to link the code of portions of this program with the
# OpenSSL library under certain conditions as described in each
# individual source file, and distribute linked combinations
# including the two.
# You must obey the GNU General Public License in all respects
# for all of the code used other than OpenSSL.  If you modify
# file(s) with this exception, you may extend this exception to your
# version of the file(s), but you are not obligated to do so.  If you
# do not wish to do so, delete this exception statement from your
# version.  If you delete this exception statement from all source
# files in the program, then also delete it here.
"""Module that implements notification of the end user."""

from ubuntuone.status.notification import AbstractNotification

APPLICATION_NAME = 'Magicicada Client'


class Notification(AbstractNotification):
    """Notification of the end user."""

    def __init__(self, application_name=APPLICATION_NAME):
        self.application_name = application_name

    def send_notification(self, title, message, icon=None, append=False):
        """Send a notification using the underlying library."""
        # TODO: Send notifications. Dummy class is here to not break
        # on windows.
