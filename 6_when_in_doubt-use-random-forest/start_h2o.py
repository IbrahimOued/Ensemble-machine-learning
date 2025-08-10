# Import the required libraries:

import h2o
import seaborn as sns
import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt

from h2o.estimators.random_forest import H2ORandomForestEstimator
from sklearn import metrics
# To use H2O, we need to initialize an instance and connect to it. We can do that as follows:

h2o.init()