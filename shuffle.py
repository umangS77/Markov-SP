import random
import sys
import pandas as pd
df = pd.read_csv("PDFMalware2022.csv") # avoid header=None. 
shuffled_df = df.sample(frac=1)
shuffled_df.to_csv("PDFMalware2022-shuffled.csv", index=False)