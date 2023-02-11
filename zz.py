import numpy as np
import pandas as pd
import csv

english=pd.read_csv("Books.csv")
nepali= pd.read_csv('nepali_books.csv')
ratings=pd.read_csv("Ratings.csv")

for rating in ratings:  
    print(rating)




