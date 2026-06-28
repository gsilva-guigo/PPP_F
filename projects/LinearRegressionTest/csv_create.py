import pandas as pd
import numpy as np


def create_csv(name):
    csv_file = f'{name}.csv'
    data = pd.DataFrame({'x': np.random.randn(100), 'y': np.random.randn(100)})
    data.to_csv(csv_file, index=False)
    print(f'CSV file "{csv_file}" created successfully.')
    
create_csv('data')