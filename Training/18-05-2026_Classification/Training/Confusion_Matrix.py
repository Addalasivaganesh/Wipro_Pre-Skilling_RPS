import pandas as pd
from seaborn import regression
from sklearn.ensemble._hist_gradient_boosting import predictor
from sklearn.metrics._plot import confusion_matrix

data ={
    "Study hours":[1,2,3,4,5,6,7,8],
    "Attendence":[55,60,65,70,75,80,85,90],
    "Result":[
        "Fail",
        "Fail",
        "Fail",
        "Pass",
        "Pass",
        "Pass",
        "Pass",
        "Pass",
    ]
}

df = pd.DataFrame(data)
print(df)

X = df[["Study hours", "Attendence"]]
y = df["Result"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, Y_test = train_test_split(X, y, test_size = 0.2,random_state =42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
Y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix

#confusion matrix
cm =confusion_matrix (
    Y_test,Y_pred)
print(cm)


