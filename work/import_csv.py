import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print('start importing csv file')
employee_df = pd.read_csv('/Volumes/MacBook/projects/datascience/datascience/work/HRdata.csv', sep=';')

print('updating Gap field')
employee_df['Gap'] = employee_df['Gap'].apply(lambda x:1 if x == 'Y' else 0)


