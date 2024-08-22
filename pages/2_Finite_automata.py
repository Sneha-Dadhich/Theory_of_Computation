import streamlit as st
st.set_page_config(page_title = "Study Conscious")

chapter1 = f"""
<style>
</style>
"""
def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)


def chapter2_finite_automata():
    st.header("Finite Automata")
    st.write(f"""**Finite Automata (FA)** is a simple and fundamental type of automaton used in the field of 
computer science and the Theory of Computation. It is a mathematical model of computation that represents a 
system with a finite number of states, transitions between these states, and an ability to accept or reject 
input strings based on the states it reaches.

### Components of Finite Automata:
1. **States:** A finite set of states, including one start state and one or more accepting (or final) states.
2. **Alphabet (Σ):** A finite set of symbols that the automaton can read as input.
3. **Transition Function (δ):** A function that takes a state and an input symbol and returns the next state.
4. **Start State (q₀):** The state where the automaton begins its computation.
5. **Accepting States (F):** A subset of states where if the automaton ends after reading the input, the input
is accepted.

### Types of Finite Automata:
1. **Deterministic Finite Automaton (DFA):** For each state and input symbol, there is exactly one transition
to a next state. DFAs are used to recognize regular languages.""")
    
    st.image(r"C:\Users\Dell\Desktop\Sneha2.0\Programs1\Python\Definite_Automata\images\DFA_Example1.jpg")
             
    st.write(f"""
2. **Non-deterministic Finite Automaton (NFA):** For each state and input symbol, there can be multiple 
possible transitions, including transitions without input (ε-transitions). Despite its flexibility, NFAs are 
equivalent in power to DFAs in terms of the languages they can recognize.""")
    
    st.image(r"C:\Users\Dell\Desktop\Sneha2.0\Programs1\Python\Definite_Automata\images\NDFA_Example1.png", use_column_width="never")
    
    st.write(f"""
### Uses of Finite Automata:
- **Pattern Matching:** Used in text editors, search engines, and lexical analyzers to match patterns in 
strings.
- **Compiler Design:** DFAs are used in lexical analysis to tokenize source code.
- **Digital Circuit Design:** Finite automata model sequential logic circuits like counters and state machines.
- **Regular Expressions:** Finite automata provide the theoretical foundation for regular expressions used 
in text processing.

### Summary:
Finite Automata is a core concept in the Theory of Computation, providing a model for systems with a limited 
number of states and deterministic or non-deterministic behavior. It plays a crucial role in understanding how 
simple computational tasks are performed and serves as a building block for more complex computational models.
""")
    if st.button("Take Quiz", key="quiz1"):
        st.latex("Feature Under Construction ...")
        st.sidebar.snow()
chapter2_finite_automata()