import sqlalchemy

from app.db import metadata

bill = sqlalchemy.Table(
    "bill",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("category", sqlalchemy.String),
    sqlalchemy.Column("secondary", sqlalchemy.String),
    sqlalchemy.Column("remark", sqlalchemy.String),
    sqlalchemy.Column("time", sqlalchemy.DateTime),
    sqlalchemy.Column("account", sqlalchemy.String),
    sqlalchemy.Column("money", sqlalchemy.Numeric),
    sqlalchemy.Column("currency", sqlalchemy.String),
    sqlalchemy.Column("io", sqlalchemy.String),
    sqlalchemy.Column("source", sqlalchemy.String),
    sqlalchemy.Column("created", sqlalchemy.DateTime),
    sqlalchemy.Column("relation", sqlalchemy.Integer),
)
