import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('first-innings-score-lr-model.pkl', 'rb'))

st.title('IPL First Innings Score Predictor')
st.sidebar.header('Team Data')
image = Image.open('images.jpg')
st.image(image, '')

# FUNCTION
def team_report():
    temp_array=list()
    batting_team= st.selectbox('Select Batting Team',('MI', 'KKR', 'CSK','RR','KXIP','RCB','DD','SRH'))
    if batting_team == 'CSK':
        temp_array = temp_array + [1,0,0,0,0,0,0,0]
    elif batting_team == 'DD':
        temp_array = temp_array + [0,1,0,0,0,0,0,0]
    elif batting_team == 'KXIP':
        temp_array = temp_array + [0,0,1,0,0,0,0,0]
    elif batting_team == 'KKR':
        temp_array = temp_array + [0,0,0,1,0,0,0,0]
    elif batting_team == 'MI':
        temp_array = temp_array + [0,0,0,0,1,0,0,0]
    elif batting_team == 'RR':
        temp_array = temp_array + [0,0,0,0,0,1,0,0]
    elif batting_team == 'RCB':
        temp_array = temp_array + [0,0,0,0,0,0,1,0]
    elif batting_team == 'SRH':
        temp_array = temp_array + [0,0,0,0,0,0,0,1]

        
    bowling_team = st.selectbox('Select Bowling Team',('MI', 'KKR', 'CSK','RR','KXIP','RCB','DD','SRH'))
    if bowling_team == 'CSK':
        temp_array = temp_array + [1,0,0,0,0,0,0,0]
    elif bowling_team == 'DD':
        temp_array = temp_array + [0,1,0,0,0,0,0,0]
    elif bowling_team == 'KXIP':
        temp_array = temp_array + [0,0,1,0,0,0,0,0]
    elif bowling_team == 'KKR':
        temp_array = temp_array + [0,0,0,1,0,0,0,0]
    elif bowling_team == 'MI':
        temp_array = temp_array + [0,0,0,0,1,0,0,0]
    elif bowling_team == 'RR':
        temp_array = temp_array + [0,0,0,0,0,1,0,0]
    elif bowling_team == 'RCB':
        temp_array = temp_array + [0,0,0,0,0,0,1,0]
    elif bowling_team == 'SRH':
        temp_array = temp_array + [0,0,0,0,0,0,0,1]
        
    o3= st.sidebar.slider('Overs', 5,20, 1 )
    
    o4 = st.sidebar.slider('Runs', 0,200, 1 )
    o5= st.sidebar.slider('Wickets', 0,10, 1 )
    o6 = st.sidebar.slider('Runs Scored in prev 5 overs', 0,100, 1 )
    o7= st.sidebar.slider('Wickets taken in prev 5 overs', 0,10, 1 )
    temp_array = temp_array + [int(o3),int(o4),int(o5),int(o6),int(o7)]
    data = np.array([temp_array])
    user_report_data = {
      'Battting Team':batting_team,
      'Bowling Team':bowling_team,
      'Overs':o3,
      'Runs':o4,
      'Wickets':o5,
      'Runs Scored in prev 5 overs':o6,
      'Wickets taken in prev 5 overs':o7
  }
    
    report_data = pd.DataFrame(user_report_data, index=[0])
    st.write(report_data)
    return data

team_data = team_report()
submit=st.button('PREDICT')

if(submit):
    
    score = model.predict(team_data)[0]
    st.subheader('Predicted Score -Max'+str(np.round(score, 2)))
  

