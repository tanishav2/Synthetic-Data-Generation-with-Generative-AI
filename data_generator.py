import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

# Load the data
data = pd.read_csv("C:/Users/Rajesh Varshney/Downloads/screentime_analysis.csv")
print(data.head()) 