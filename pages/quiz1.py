import streamlit as st

# Function to check the answers
def check_answers(answers):
    correct_answers = {
        "Q1": "c",
        "Q2": "a",
        "Q3": "d",
        "Q4": "b",
        "Q5": "a",
    }
    
    score = 0
    for q, ans in correct_answers.items():
        if answers[q][:1] == ans:
            score += 1
            
    return score

def quiz1():
    # Quiz title

    st.title("Automata Theory Quiz")

    # Questions
    questions = {
        "Q1": "Which of the following is a regular language?",
        "Q2": "Which automaton recognizes context-free languages?",
        "Q3": "What is the language of a Turing Machine?",
        "Q4": "Which of the following is not a property of regular languages?",
        "Q5": "Which of the following statements is true?",
    }

    options = {
        "Q1": ["a) {a^n b^n | n ≥ 0}", "b) {a^n b^m | n ≠ m}", "c) {a^n | n is a multiple of 2}", "d) {a^n b^m c^n | n, m ≥ 0}"],
        "Q2": ["a) Pushdown Automaton", "b) Deterministic Finite Automaton", "c) Turing Machine", "d) Non-deterministic Finite Automaton"],
        "Q3": ["a) Regular Language", "b) Context-Free Language", "c) Context-Sensitive Language", "d) Recursively Enumerable Language"],
        "Q4": ["a) Closure under union", "b) Closure under intersection with a regular language", "c) Closure under complement", "d) Closure under reversal"],
        "Q5": ["a) Every DFA is also an NFA", "b) Every NFA is also a DFA", "c) Every PDA is also a DFA", "d) Every regular language is context-free"],
    }

    # Initialize session state to store answers
    if "answers" not in st.session_state:
        st.session_state["answers"] = {q: "" for q in questions.keys()}

    # Display questions and options
    for q, text in questions.items():
        st.write(f"**{q}: {text}**")
        st.session_state["answers"][q] = st.radio("this text is not visible", options[q], key=q , index=None, label_visibility="hidden")

    # Submit button
    if st.button("Submit"):
        score = check_answers(st.session_state["answers"])
        st.write(f"Your score is: {score} / 5")

        if score == 5:
            st.sidebar.balloons()
            # st.sidebar.snow()
            st.success("Excellent! You got all questions correct.")
        elif score >= 3:
            st.warning("Good job! But there's room for improvement.")
        else:
            st.error("You might want to review the concepts again.")

quiz1()
