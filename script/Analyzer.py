import sys
sys.path.append('C:/Users/Rauan/practice/script/Analyzer.py')
from sys import Analyzer

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyzer:
    def __init__(self, filename):
        self.data = pd.read.csv(filename)

    def info(self):
        return self.data.info()

    def describe(self):
        return self.data.describe()

    def check_missing_values(self):
        return self.data.isnull().sum()

    def check_duplicates(self):
        return self.data.duplicated().sum()

    def show_histogram(self, column):
        plt.figure(figsize=(10,6))
        sns.histplot(self.data[column], bins = 20, kde = True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def show_heatmap(self):
        plt.figure(figsize=(10,8))
        sns.heatmap(self.data.corr(), cmap='coolwarm', annot = True, fmt=".2f")
        plt.title('Corellation Matrix')
        plt.show()

    def show_corellation_matrix(self):
        return self.data.corr()
