pip install matplotlib;

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

st.title("Streamlit Tutorial")
st.header("this is header")
st.subheader("this is subheader")
st.text("hello world")


st.markdown("## Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.markdown(''' :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] ''')            
    

st.latex(r"Y=\alpha + \beta X_i")

st.success("성공")
#st.info st.warning st.error st.exception


url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris_df = pd.read_csv(url)

st.table(iris_df.head())

st.dataframe(iris_df)
st.write(iris_df)
st.markdown("* * *")


#html form 형태를 출력  (위젯)
if st.checkbox("show/hide"):
  st.write("체크박스가 선택")
else:
  st.write("체크박스가 꺼짐")
  

status = st.radio("choose one",("1","2","3"))
if status == "1":
  st.success("1 됨")
else :
  st.warning("비활성화")


#드롭박스 (콤보박스)
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

#드랍다운 다중 선택
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options, len(options))


#st.slider
level = st.slider("레벨선택",1,5)


#Text
first_name = st.text_input("Enter your name","placeholder")
if st.button("submit", key='first_name'):
  result = first_name.title()
  st.success(result)
  
#textarea
message = st.text_area("메시지를 입력하세요","placeholder")
if st.button("submit", key='message'):
  result2 = message.title()
  st.success(result2)
  
  
today = st.date_input("날짜를 입력하세요", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요", datetime.time())



with st.echo():
  import pandas as pd
  df = pd.DataFrame()

st.json({
   "name" : "민수",
   "gender" : "male",
   "age" :26
})

st.sidebar.header("사이드바 메뉴")
st.sidebar.selectbox("메뉴를 선택하세요",["데이터","DOM","code"])


st.subheader("Matplotlib으로 차트 그리기")

fig, ax = plt.subplots()
ax = iris_df[iris_df['species']=="virginica"]['petal_length'].hist()
st.pyplot(fig)


#데이터 캐싱("정적인 데이터 하는 건 좋음")
# 캐싱은 어노테이션으로 표시하지만
# 반드시 함수형태로 캐싱을 지정해야함


#세션 데이터 관리
#세션은 Key-value로 이루어져 있음
#####################################새로고침 키는 완전 초기화 된다.###############################
#하지만 다른 웹 동작은  세션이 유지된다.
if 'count' not in st.session_state:  #세션 데이터 변수 하나를 초기화 하는 것
  st.session_state.count = 0
  
increment = st.button("Count 증가")

if increment :
  st.session_state.count += 1
  
st.write(st.session_state.count)



#파일 업로드 구현
#st.file_uploader
##uploaded_files = st.file_uploader("choose a csv file", accept_multiple_file=True)
###for uploaded_file in  uploaded_files:
##실습해보기


#레이아웃
first,last = st.columns(2)
first.text_input("first Name")
last.text_input("Last Name")
  

#데이터 프로파일링 실습은 나중에 해보기 
