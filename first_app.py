# import streamlit as st
# import numpy as np
# import pandas as pd

# st.title('My First App')

# # st.write("Here's our first attempt at using data to create a table:")
# # st.write(pd.DataFrame({
# #     'first column': [1, 2, 3, 4],
# #     'second column' : [10, 20, 30, 40]
# # }))

# df = pd.DataFrame({
#     'first column' : [1, 2, 3, 4],
#     'second column' : [10, 20, 30, 40]
# })

# df

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(chart_data)


# sapa_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon']
# )

# st.map(sapa_data)

# if st.checkbox('Show Dataframe'):
#     chart_data = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns=['a', 'b', 'c'])

#     chart_data


import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('dtreemodel.pkl','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: Black;background-color:#f32445'>Diabetes Predictor</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest :)</h3>", unsafe_allow_html=True)
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("It a Web app that would help the user in determining whether they have diabetes or not.")
  st.sidebar.header("What tools where used to make this?")
  st.sidebar.text("The Model was made using a dataset from Machine Learning class along with using Machine learning notebooks to train the model. We made use of Sci-Kit learn in order to make our Decision Tree Model.")



  preg = st.slider("Input Your number of Pregnancies",0,17)
  glucose = st.slider("Input your glucose intake",0.0,250.0)
  Insulin = st.slider("Input your Insulin level",0.0,900.0)
  BMI= st.slider("Input your BMI (Body Mass Index)",0.0,70.0)
  DiabetesPedigreeFunction = st.slider("DiabetesPedigreeFunction" ,1.0,5.0)
  age = st.slider("Input your Age",0,100)
  log_age = np.log(age)

  inputs = [[preg,glucose,Insulin,BMI,DiabetesPedigreeFunction,age,log_age]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    st.text('1 represents Positive while 0 represents negative')
    st.success(f'Your Predicted Diabetes State is {updated_res}')
    if updated_res == 0:
      st.write("Congratulations!!! You DO NOT have diabetes")
    else:
      st.write("I'm sorry but You have diabetes.....Please see your Doctor as soon as possible :(")
  # genre = st.radio(
  #  "What's your favorite movie genre",  
  #  ('Comedy', 'Drama', 'Documentary'))

  # if genre == 'Comedy':
  #   st.write('You selected comedy.')
  # else:
  #   st.write("You didn't select comedy.")

if __name__ =='__main__':
  main() 