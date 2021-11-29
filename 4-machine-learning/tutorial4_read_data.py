# -*- coding: UTF-8 -*-
import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import matplotlib.pyplot as plt # Visualization
import seaborn as sns
#set plotting 
plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
plt.style.use('seaborn-whitegrid')

#import data
path = './' 
df = pd.read_csv(path + 'insurance.csv')
if __name__ == '__main__':
    print('Number of rows and columns in the data set: ', df.shape)