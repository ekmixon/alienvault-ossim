#
#  License:
#
#  Copyright (c) 2013 AlienVault
#  All rights reserved.
#
#  This package is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 dated June, 1991.
#  You may not use, modify or distribute this program under any other version
#  of the GNU General Public License.
#
#  This package is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this package; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,
#  MA  02110-1301  USA
#
#
#  On Debian GNU/Linux systems, the complete text of the GNU General
#  Public License can be found in `/usr/share/common-licenses/GPL-2'.
#
#  Otherwise you can read it here: http://www.gnu.org/licenses/gpl-2.0.txt
#

import os
import sys

from avconfig.ossimsetupconfig import AVOssimSetupConfigHandler

CONFIG_FILE = "/etc/ossim/ossim_setup.conf"
ossim_setup = AVOssimSetupConfigHandler(CONFIG_FILE)



class Config(object):
    DIR = os.path.abspath(os.path.dirname(__file__))
    # Path to our database
    SQLALCHEMY_DATABASE_URI = f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault"


    SQLALCHEMY_BINDS = {
        "status_message": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "status_message_action": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "status_action": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "current_status": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "logged_actions": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "monitor_data": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "celery_job": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_api",
        "acid_event": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_siem",
        "device": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault_siem",
        "alienvault_host": f"mysql://{ossim_setup.get_database_user()}:{ossim_setup.get_database_pass()}@{ossim_setup.get_database_db_ip()}/alienvault",
    }

    # Folder where we will store the SQLAlchemy-migrate data files
    SQLALCHEMY_MIGRATE_REPO = os.path.join(DIR, 'db_repository')
    MESSAGE_CENTER_SERVER = "messages.alienvault.com"
    MESSAGE_CENTER_PORT = 443
    MESSAGE_CENTER_PUBLIC_KEY = "/etc/alienvault/api/alienvault-message-center-public.pem"


class ProductionConfig(Config):
    pass
class DevelConfig(Config):
    pass
