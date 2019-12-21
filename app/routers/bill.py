from datetime import date

from fastapi import APIRouter

import pandas as pd
from psycopg2 import connect

from app.models import BillWithMeta
from configs import project
from funcs import load_data
from tools.bill_helper import BillFilter

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


@router.get('/all', response_model=BillWithMeta)
async def get_all():
    """Get all bills"""
    data = await load_data()
    return {
        'bills': data.to_dict(orient='record'),
        'count': len(data),
        'money': data['money'].sum()
    }


@router.get('/specify', response_model=BillWithMeta)
async def get_specify_bill(io: str = '',
                           started: date = None, finished: date = None,
                           year: int = 0, month: int = 0, day: int = 0,
                           category: str = '', secondary: str = ''
                           ):
    """Get specify bill.started/finished or year/month/day only can use one."""
    data = await load_data()
    bill_filter = BillFilter()
    if io:
        data = bill_filter.filter_io(data, io)
    if started:
        data = bill_filter.filter_start_end(data, started, finished)
    elif year:
        data = bill_filter.filter_year_month_day(data, year, month, day)
    if category:
        data = bill_filter.filter_kind(data, category, secondary)
    return {
        'bills': data.to_dict(orient='record'),
        'count': len(data),
        'money': data['money'].sum()
    }
