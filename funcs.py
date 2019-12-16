import pandas as pd

from configs import project


async def load_data():
    """Load all bill data."""
    data_file = project.DATA_DIR / 'data.xlsx'
    data = pd.read_excel(str(data_file)).drop(columns=['Unnamed: 0'])
    data['relation'] = data['relation'].fillna('').apply(lambda x: '' if x == '' else int(float(x)))
    data['created'] = data['created'].astype('str')
    data['time'] = data['time'].astype('str')
    return data
