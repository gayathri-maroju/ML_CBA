# importing necessary libraries
import joblib
import pandas as pd
import streamlit as st


#load the model
KMeansCls = joblib.load('cluster.pkl')

#page configuration
st.set_page_config(page_title = 'Customer Behaviour Analysis Web App', layout='centered')
st.title('Customer Behaviour Analysis')

# customer segmentation function
def segment_customers(input_data):
    
    prediction=KMeansCls.predict(pd.DataFrame(input_data, columns=['Income', 'Age', 'Month_Customer', 'TotalSpendings', 'Children']))
    print(prediction)
    pred_1 = 0
    if prediction == 0:
            pred_1 = 'Highly Active'

    elif prediction == 1:
            pred_1 = 'Moderately Active'

    elif prediction == 2:
            pred_1 = 'Least Active'

    return pred_1
def main():
    
    
    st.image("""https://cdn.w600.comps.canstockphoto.com/text-sign-showing-customer-behavior-stock-image_csp64459562.jpg""")
    Income = st.text_input("Type In The Household Income")
    Children = st.radio( "Select Number Of children In Household",('0', '1','2','3') )
    Month_Customer = st.text_input( "Type In The Month of customer's enrollment with the company")
    Age = st.slider( "Select Age",18,85)
    TotalSpendings= st.text_input( "Type In The TotalSpendings")
    

    
    
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Customer Analysis"):
        result=segment_customers([[Income,Age,Month_Customer,TotalSpendings,Children]])
    
    st.success(result)
if __name__ == '__main__':
        main ()






