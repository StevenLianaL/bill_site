from datetime import date

import pandas as pd


class BillFilter:
    @staticmethod
    def filter_year_month_day(df: pd.DataFrame, year: int = 0, month: int = 0, day: int = 0):
        stamp = pd.to_datetime(df['time'])
        condition = stamp.dt.year == year
        if month:
            condition = (stamp.dt.month == month) & condition
            if day:
                condition = (stamp.dt.day == day) & condition
        return df.loc[condition, :]

    @staticmethod
    def filter_start_end(df: pd.DataFrame, start: date = '', end: date = ''):
        stamp = pd.to_datetime(df['time'])
        condition = (stamp >= start) & (stamp <= end)
        return df.loc[condition, :]

    @staticmethod
    def filter_io(df: pd.DataFrame, io: str):
        """if not io,return df self"""
        if io:
            return df.loc[df.io == io, :]
        else:
            return df

    @staticmethod
    def filter_kind(df: pd.DataFrame, category: str, secondary: str = ''):
        if category:
            condition = df.category == category
            if secondary:
                condition = (df.secondary == secondary) & condition
            return df.loc[condition, :]
