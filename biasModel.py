import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

class BiasModel:
    def __init__(self):
        # Get the same results each time
        np.random.seed(0)

        # Load the first dataset
        data1 = pd.read_csv("./data.csv")
        comments1 = data1["comment_text"]
        target1 = (data1["target"] > 0.7).astype(int)
        
        # Load the second dataset
        data2 = pd.read_csv("./data2.csv")
        comments2 = data2["comment_text"]
        target2 = (data2["target"] > 0.7).astype(int)
        
        # Combine the data
        comments = pd.concat([comments1, comments2], ignore_index=True)
        target = pd.concat([target1, target2], ignore_index=True)

        # Break into training and test sets
        comments_train, comments_test, y_train, y_test = train_test_split(comments, target, test_size=0.30, stratify=target)

        # Get vocabulary from training data
        self.vectorizer = CountVectorizer()
        self.vectorizer.fit(comments_train)

        # Get word counts for training and test sets
        X_train = self.vectorizer.transform(comments_train)
        X_test = self.vectorizer.transform(comments_test)

        # Train a model and evaluate performance on test dataset
        self.classifier = LogisticRegression(max_iter=2000)
        self.classifier.fit(X_train, y_train)
        self.score = self.classifier.score(X_test, y_test)
        print("Accuracy:", self.score)

        # Preview the dataset
        print("Data successfully loaded!\n")
        print("Sample toxic comment:", comments_train.iloc[22])
        print("Sample not-toxic comment:", comments_train.iloc[17])

    # Function to classify any string
    def classify_string(self, string, investigate=False):
        prediction = self.classifier.predict(self.vectorizer.transform([string]))[0]
        if prediction == 0:
            print("NOT TOXIC:", string)
        else:
            print("TOXIC:", string)
