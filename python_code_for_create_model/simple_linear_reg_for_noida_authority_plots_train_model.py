import pandas as pd
import numpy as np

# Read the csv file  --> Data/Noida_authority_plots_Simple_linear_regression.csv
df = pd.read_csv(r"E:\ML_Class_8_30_am\Data\Noida_authority_plots_Simple_linear_regression.csv")

X = df[["Amount_in_Crore"]]   # --> 2D is required
y = df["Land_in_Bigha"]

# Now i am going to start train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  =  train_test_split(X, y, test_size = 0.2, random_state = 42)

# Now i am going to train the model using LinearRegression
from sklearn.linear_model import LinearRegression
# Create an object
model = LinearRegression()
# Now train the model
model.fit(X_train, y_train)

# Now i am going to test the model 
print(model.predict([[50]]))
print(model.predict([[10000]]))


# Now Create a y_pred variable using X_test
y_pred = model.predict(X_test)
y_pred


# Now i am going to check the accuracy of the model using r2
# =============================================================
# r2 == 1  --> Perfect fit
# r2 > 0.9 --> Excellent
# r2 < 0.5 --> Bad Model
# =============================================================
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(r2)


# Now i am going to convert model in .pkl
# for .pkl you need to insall joblib
import joblib
joblib.dump(model, "E:\ML_Class_8_30_am\my_trained_model\simple_lr_regression_model_noida_authority_plot.pkl")

print("Model dumped succssfully......")




