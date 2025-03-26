import streamlit as st
import random

# List of questions
questions = [
    {
        "question": "What is the output of 2 + 2 * 3?",
        "choices": ["A. 8", "B. 10", "C. 12", "D. 6"],
        "answer": "B"
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

# Initialize session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.selected_choice = None
    st.session_state.questions_shuffled = random.sample(questions, len(questions))  # Shuffle all questions

# Home Page
st.title("Python Quiz")
st.write("Test your Python knowledge with this quiz!")

# Start Quiz Button
if not st.session_state.quiz_started:
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.questions_shuffled = random.sample(questions, len(questions))  # Shuffle again on restart
        st.rerun()

# Quiz Logic
if st.session_state.quiz_started:
    if st.session_state.question_index < len(st.session_state.questions_shuffled):
        question = st.session_state.questions_shuffled[st.session_state.question_index]

        st.subheader(question["question"])
        selected_choice = st.radio("Select your answer:", question["choices"], key=st.session_state.question_index)

        if st.button("Submit Answer"):
            user_answer = selected_choice.split(".")[0]  # Extract 'A', 'B', etc.

            if user_answer == question["answer"]:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect! The correct answer is {question['answer']}")

            # Move to the next question
            st.session_state.question_index += 1
            st.rerun()  # Instantly update the question

        st.write(f"Your current score: {st.session_state.score}")

    else:
        st.success(f"Quiz Completed! Your final score is {st.session_state.score} / {len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.quiz_started = False
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.session_state.questions_shuffled = random.sample(questions, len(questions))  # Shuffle again
            st.rerun()
