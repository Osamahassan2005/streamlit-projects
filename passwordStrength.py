import streamlit as st
import random
import string

def pass_strength(password):
	feedback = []
	score = 0
	if len(password) >= 8 :
		score += 1
	else:
		feedback.append('❌ Password is too short it should be at least 8 characters')
		
	if any(char in password for char in '@#$&!^%*,'):
		score += 1
	else:
		feedback.append('❌ Passwors must contain at least on special character(e.g:@#$&!)')
	if any(char.isdigit() for char in password):
		score += 1
	else:
		feedback.append('❌ Password should contain at least one digit')
			
	if any(char.islower() for char in password ):
		score += 1
	else:
		feedback.append('❌ Password must include at least one Lowercase letter')
			
	if any(char.isupper() for char in password):
		score += 1
	else:
		feedback.append('❌ Passwors must include at least one upper case letter ')
	return score, feedback
	
#streamlit app
st.title('Password Strength Checker')
st.markdown('Check your password strength.')
#password input
password = st.text_input('Enter your password')

#check password button
if st.button('Check Password'):
	score, feedback = pass_strength(password)
	st.subheader(f'Password Score: {score} out of 5')

	for item in feedback:
		st.write(item)
		
	#password strength indicator (moved inside button check)
	if score == 5:
		st.success('Your password is strong')
	elif score >= 3:
		st.warning('Your password is medium')
	else:
		st.error('Your password is weak')

#password generator
st.sidebar.subheader('Random Password Generator')
length = st.sidebar.slider('Select the length of the password', min_value=8, max_value=32, value=16)
if st.sidebar.button('Generate Password'):
	password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
	st.sidebar.write(f'For **{length}** characters the password is : **{password}**')
#created by
st.sidebar.markdown('Created by [Osama](https://github.com/Osamahassan2005)')
