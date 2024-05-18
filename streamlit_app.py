# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Калькулятор индекса массы тела')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Введите ваш вес (в кг)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Выберите единицы измерения роста: ',
				('см', 'метры', 'футы'))

# compare status value
if(status == 'см'):
	# take height input in centimeters
	height = st.number_input('Сантиметры')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Введите свой рост")

elif(status == 'метры'):
	# take height input in meters
	height = st.number_input('Метры')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Введите свой рост")

else:
	# take height input in feet
	height = st.number_input('Футы')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Введите свой рост")

# check if the button is pressed or not
if(st.button('Рассчитать ИМТ')):

	# print the BMI INDEX
	st.text("Ваш ИМТ {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("У вас очень низкий вес")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("У вас низкий вес")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Вес в норме")
	elif(bmi >= 25 and bmi < 30):
		st.warning("У вас избыточный вес")
	elif(bmi >= 30):
		st.error("Чрезвычайно избыточный вес")