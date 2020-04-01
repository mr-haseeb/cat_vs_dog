# %%
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow import keras
from sklearn.model_selection import train_test_split
import pandas as pd
from tensorflow.keras.utils import to_categorical
# %%
dataset = pd.read_csv('data.csv',  index_col=None)

# %%
y = dataset.pop('labels').values
y = to_categorical(y)
print(y)

# %%
