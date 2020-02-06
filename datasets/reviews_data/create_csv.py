from fastai.core import Path
from datetime import datetime 

def write_to_csv(df, filename=None):
    csv_path = Path('datasets/csv/')
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    if not filename:
        filename = f'reviews_{timestamp}.csv'
    else:
        filename = f'{filename}_{timestamp}.csv'

    file_path = csv_path/filename
    df.to_csv(file_path)
    return