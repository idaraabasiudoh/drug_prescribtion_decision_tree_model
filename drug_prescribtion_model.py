import warnings
warnings.filterwarnings("ignore")

import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from IPython.display import Image

# Load the dataset
my_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv', delimiter=",")
print("Data Shape:", my_data.shape)

# Define feature matrix X and target vector y
X = my_data[["Age", "Sex", "BP", "Cholesterol", "Na_to_K"]].values
y = my_data["Drug"]

# Convert categorical variables to numerical values
sex_col = preprocessing.LabelEncoder()
sex_col.fit(["F", "M"])
X[:,1] = sex_col.transform(X[:,1])

BP_col = preprocessing.LabelEncoder()
BP_col.fit(["LOW", "NORMAL", "HIGH"])
X[:,2] = BP_col.transform(X[:,2])

cho_col = preprocessing.LabelEncoder()
cho_col.fit(["NORMAL", "HIGH"])
X[:,3] = cho_col.transform(X[:,3])

# Split the dataset into training and testing sets
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

# Create and train the decision tree model
drugTree = DecisionTreeClassifier(criterion="entropy", max_depth=4)
drugTree.fit(X_trainset, y_trainset)

# Make predictions
predTree = drugTree.predict(X_testset)

# Evaluate the model
print("Decision Tree's Accuracy:", metrics.accuracy_score(y_testset, predTree))

# Visualize the decision tree
export_graphviz(drugTree, out_file='tree.dot', filled=True, feature_names=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])
