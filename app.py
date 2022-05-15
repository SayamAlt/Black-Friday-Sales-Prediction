#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib


# In[2]:


model = joblib.load('model.pkl')
model


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/")
def home():
    return render_template('home.html')


# In[5]:


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        user_id = int(request.form['uid'])
        product_id = int(request.form['pid'])
        sel_gender = request.form['gender']
        gender = 0 #Assuming that gender is female by default
        if sel_gender == 'Male':
            gender = 1
        elif sel_gender == 'Female':
            gender = 0
        age_inp = request.form['age']
        age = 0
        if age_inp == '0-17':
            age = 0
        elif age_inp == '18-25':
            age = 1
        elif age_inp == '26-35':
            age = 2
        elif age_inp == '36-45':
            age = 3
        elif age_inp == '46-50':
            age = 4
        elif age_inp == '51-55':
            age = 5
        elif age_inp == '55+':
            age = 6
        occupation = int(request.form['occ'])
        city_category = request.form['city_categ']
        cc = 0
        if city_category == 'A':
            cc = 1
        elif city_category == 'B':
            cc = 2
        elif city_category == 'C':
            cc = 3
        city_stay = request.form['years_stay']
        stay_duration = 0
        if city_stay == '0':
            stay_duration = 0
        elif city_stay == '1':
            stay_duration = 1
        elif city_stay == '2':
            stay_duration = 2
        elif city_stay == '3':
            stay_duration = 3
        elif city_stay == '4+':
            stay_duration = 4
        wed_status = request.form['marital_status']
        marital_status = 0 #Assuming that person is unmarried by default
        if wed_status == 'Married':
            marital_status = 1
        prod_cat_1 = float(request.form['product_categ_1'])
        prod_cat_2 = float(request.form['product_categ_2']) #Between 2.0 and 18.0
        prod_cat_3 = float(request.form['product_categ_3']) #Between 3.0 and 18.0
#         print([user_id,
#             product_id,
#             gender,
#             age, 
#             occupation,
#             cc,
#             stay_duration,
#             marital_status,
#             prod_cat_1,
#             prod_cat_2,
#             prod_cat_3])
        predictions = model.predict([[
            user_id,
            product_id,
            gender,
            age, 
            occupation,
            cc,
            stay_duration,
            marital_status,
            prod_cat_1,
            prod_cat_2,
            prod_cat_3
        ]]) 
        output = predictions[0]
        output = "%.2f" % output
        return render_template('home.html',prediction_text="The customer purchase amount in the Black Friday sales across various distinct high-volume products is ${}.".format(output))


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)

