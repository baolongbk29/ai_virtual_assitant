import configparser
import datetime

import pytz

cfg = configparser.ConfigParser()
cfg.read("./environment.ini")

# =========================================================================
#                           TIMING CONFIG
# =========================================================================
u = datetime.datetime.utcnow()
u = u.replace(tzinfo=pytz.timezone("Asia/Ho_Chi_Minh"))

# =========================================================================
#                          PROJECT INFORMATION
# =========================================================================
PROJECT = cfg["project"]
PROJECT_NAME = PROJECT["name"]
ENVIRONMENT = PROJECT["environment"]


# =========================================================================
#                          DATABASE INFORMATION
# =========================================================================

DATABASE = cfg["database"]
DATABASE_USERNAME = DATABASE["user_name"]
DATABASE_PASSWORD = DATABASE["password"]
DATABASE_NAME = DATABASE["host"]
DATABASE_PASSWORD = DATABASE["name"]
