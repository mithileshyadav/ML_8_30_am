from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# import model
model  = joblib.load("E:\\ML_Class_8_30_am\\my_trained_model\\simple_lr_regression_model_noida_authority_plot.pkl")
print(model.predict(np.array([[10]])))


# breakpoint()
class PredictRequestSimpleLrNoidaAuthorityPlot(BaseModel):
    user_input_price : float

# Create an object of FastAPI
app = FastAPI()

# Check api is working or not

@app.get("/")
def home():
    return {"message": "Api is working"}

@app.post("/noida_authority_plot_predict_simple_lr_model")
def simple_lr_model_noida_authority_plot_predict(data : PredictRequestSimpleLrNoidaAuthorityPlot):
    as_user_input = model.predict(np.array([[data.user_input_price]]))

    return {
        "Price_provided_by_you": data.user_input_price,
        "Plot_size" : as_user_input[0]
    }












