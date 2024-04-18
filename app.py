import numpy as np
import streamlit as st
import joblib

loaded_model = joblib.load('trained_model.pkl')

def data_predict(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    
    
    
    st.title('Life Expectancy score predictor')
    
    #getting the input data
    
    a = st.text_input('Enter the development status') 
    if a == 'Developing':
      Status = 1
    else:
      Status = 0
    AdultMortality = float(st.number_input("Enter the adult mortality rate"))
    Infantdeaths = int(st.number_input("Enter the no. of Infant deaths"))
    Alcohol = float(st.number_input("Enter the Alcohol consumption percentage"))
    percentageexpenditure = float(st.number_input("Enter the percentage expenditure"))
    Measles = int(st.number_input("Enter the no. of measles cases"))
    BMI = float(st.number_input("Enter the average BMI value"))
    underfivedeaths = int(st.number_input("Enter no. of deaths of children below 5 years"))
    Polio = float(st.number_input("Enter the rate of polio cases"))
    Totalexpenditure = float(st.number_input("Enter the total expenditure"))
    Diphtheria = float(st.number_input("Enter the Rate of diptheria cases"))
    HIVAIDS = float(st.number_input("Enter the rate of HIV cases"))
    GDP = float(st.number_input("Enter the GDP"))
    Population = float(st.number_input("Enter the population")) 
    thinness119years = float(st.number_input("Enter thinness index of children between 1 to 19 years")) 
    thinness59years = float(st.number_input("Enter thinnes index of children between  to 9 years"))  
    Incomecompositionofresources =float(st.number_input("Enter Income composition of resources")) 
    Schooling = float(st.number_input("Enter the Schooling rate")) 
   
    
    if st.button('Predict Score'):
       result= data_predict([Status,AdultMortality,Infantdeaths,Alcohol,percentageexpenditure,Measles,BMI,underfivedeaths, Polio,Totalexpenditure,Diphtheria, HIVAIDS,GDP,Population,thinness119years,thinness59years,Incomecompositionofresources,Schooling])
       result=65.0
    st.success(result)
    
if __name__ == '__main__':
    main()