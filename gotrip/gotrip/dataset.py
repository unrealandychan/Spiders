import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("japan.csv")
for tag in df.tags:
    taglist = tag.split(',')
    print(taglist[7:-6])