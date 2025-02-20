# Importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
# Opening the data file and studying the general information
df = pd.read_csv('/datasets/games.csv')
df.head()
