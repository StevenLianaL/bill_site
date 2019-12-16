from datetime import datetime

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
    category: str
    secondary: str
    remark: str
    time: datetime = None
    account: str
    money: str
    io: str
    source: str
    relation: str
