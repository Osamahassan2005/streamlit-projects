import streamlit as st
import random
import time

# List of questions, choices, and answers
questions = [
    {
        "question": "What is the output of 2 + 2 * 3?",
        "choices": ["A. 8", "B. 10", "C. 12", "D. 6"],
        "answer": "A"
    },
    {
        "question": "Which of the following is used to define a function in Python?",
        "choices": ["A. def", "B. function", "C. define", "D. func"],
        "answer": "A"
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "choices": ["A. {1, 2, 3}", "B. [1, 2, 3]", "C. (1, 2, 3)", "D. <1, 2, 3>"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to import a module in Python?",
        "choices": ["A. include", "B. import", "C. require", "D. use"],
        "answer": "B"
    },
    {
        "question": "What is the output of 'Hello' + 'World'?",
        "choices": ["A. HelloWorld", "B. Hello World", "C. Hello+World", "D. Error"],
        "answer": "A"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "choices": ["A. int", "B. str", "C. list", "D. tuple"],
        "answer": "C"
    },
    {
        "question": "What does the len() function do?",
        "choices": ["A. Returns the type of an object", "B. Returns the length of an object", "C. Converts a value to an integer", "D. None of the above"],
        "answer": "B"
    },
    {
        "question": "Which of the following is NOT a Python keyword?",
        "choices": ["A. if", "B. else", "C. switch", "D. while"],
        "answer": "C"
    },
    {
        "question": "What is the output of bool(0)?",
        "choices": ["A. True", "B. False", "C. 0", "D. None"],
        "answer": "B"
    },
    {
        "question": "What is the correct syntax to open a file in Python?",
        "choices": ["A. open('file.txt', 'r')", "B. open.file('file.txt')", "C. file.open('file.txt')", "D. open('file.txt')"],
        "answer": "A"
    }
]

# Home page
st.title("Python Quiz")
st.write("Welcome to the Python Quiz!")
st.write("You will be asked 10 questions about Python.")
st.write("Each question has 4 options (A, B, C, D).")
st.write("Select the correct answer and click on the button to submit your answer.")
st.write("Good luck!")
st.write("Let's start the quiz!")

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.quiz_started = False
    st.session_state.next_question_time = None  # Timestamp for next question

# Function to run the quiz
def run_quiz(questions):
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
    
        if 'quiz_started' in st.session_state and st.session_state.quiz_started:
            question = st.session_state.current_question
            st.subheader(question["question"])
        selected_choice = st.radio("Select your answer:", question["choices"])

        if st.button("Submit Answer") and not st.session_state.answered:
            if selected_choice[0] == question["answer"]:  # Compare the first character (A/B/C/D)
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error("Incorrect!")
                st.error(f"The correct answer is {question['answer']}")
                
            st.session_state.answered = True
            st.session_state.next_question_time = time.time() + 3  # Set timestamp for next question

        # Check if it's time to move to the next question
        if st.session_state.answered and time.time() >= st.session_state.next_question_time:
            st.session_state.current_question = random.choice(questions)
            st.session_state.answered = False
            st.session_state.next_question_time = None
            st.rerun()

        st.write(f"Your current score is: {st.session_state.score}")

# Run the quiz
run_quiz(questions)
