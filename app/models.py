from datetime import datetime
from typing import List

from pydantic import BaseModel


class BillDb(BaseModel):
    id: int
    category: str
    secondary: str
    remark: str
    time: datetime
    account: str
    money: str
    currency: str
    io: str
    source: str
    created: datetime
    relation: str


class BillOut(BaseModel):
    id: int
    category: str
    secondary: str
    remark: str
    time: datetime = None
    account: str
    money: str
    io: str
    source: str
    relation: str


class BillWithMeta(BaseModel):
    count: int
    money: float
    bills: List[BillOut]
