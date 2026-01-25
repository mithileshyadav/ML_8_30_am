from django.shortcuts import render
import numpy as np
import joblib
# Create your views here.

def home(request):
    if request.method == "POST":
        # Take all input data from html page
        data = request.POST
        amount_in_cor_input = float(data.get("amount_in_cror"))
        corner_loc_input = int(data.get("corner_loc"))
        distan_from_main_rd_input = float(data.get("distan_from_main_rd"))
        parking_input = int(data.get("parking"))
        loaction_rating_input = float(data.get("loaction_rating"))
        
        # import model and predict
        model  = joblib.load("E:\\ML_Class_8_30_am\\my_trained_model\\muliple_lr_regression_model_noida_authority_plot.pkl")
        print(model.predict(np.array([[amount_in_cor_input,corner_loc_input,distan_from_main_rd_input, parking_input, loaction_rating_input ]])))
        predicted_data = model.predict(np.array([[amount_in_cor_input,corner_loc_input,distan_from_main_rd_input, parking_input, loaction_rating_input ]]))

        # stote predicted data inside context dict.
        context = {
            "html_response_data": predicted_data[0]
            }
        
        # retun contect dict as response
        return render(request, "index.html", context)


    else:
        return render(request, "index.html")
