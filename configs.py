import os
import platform
from pathlib import Path

from pydantic import BaseSettings


def whether_is_debug():
    system = platform.system()
    return True if system == 'Windows' else False


class ProjectSetting(BaseSettings):
    is_debug = whether_is_debug()

    # db
    DB_DRIVER = 'postgresql'
    DB_HOST = ''
    DB_PORT = '5432'
    DB_NAME = 'money'
    DB_USER = ''
    DB_PASSWORD = ''

    # base
    ROOT_DIR = Path(os.path.realpath(__file__)).parent
    DATA_DIR = ROOT_DIR / 'data'

    class Config:
        env_prefix = 'BILL_'


project = ProjectSetting()
