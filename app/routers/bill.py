from fastapi import APIRouter

import pandas as pd
from psycopg2 import connect

from configs import project

router = APIRouter()


@router.post('/reset')
async def reset():
    """Reset saved data."""
    if not project.DATA_DIR.exists():
        project.DATA_DIR.mkdir()
    conn = connect(
        dbname=project.DB_NAME, user=project.DB_USER,
        password=project.DB_PASSWORD, host=project.DB_HOST
    )
    excel = pd.read_sql('select * from bill', conn)
    data_file = project.DATA_DIR / 'data.xlsx'

    writer = pd.ExcelWriter(str(data_file))
    excel.to_excel(writer)
    writer.save()
    return 'reset successfully'


@router.get('/all')
async def get_all():
    # todo load all data
    pass
