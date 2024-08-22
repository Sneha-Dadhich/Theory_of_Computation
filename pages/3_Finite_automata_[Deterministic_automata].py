import streamlit as st
st.set_page_config(page_title = "Study Conscious")

chapter1 = f"""
<style>
</style>
"""
def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)


def chapter2_deterministic_automata():
    st.header("Finite Automata")
    st.subheader("Determininstic Automata :")
    st.write("""**Deterministic Finite Automaton (DFA)** is a type of finite automaton where the behavior is 
entirely predictable and unambiguous. In a DFA, for each state and input symbol, there is exactly one possible 
next state. This determinism makes DFAs straightforward to understand and implement, especially in contexts
where precise pattern recognition is required.

### Key Characteristics of DFA:
1. **Deterministic Transitions:** At any given state, for each input symbol, the DFA has one and only one
transition to another state. There are no ambiguities or multiple choices.
   
2. **No ε-transitions:** A DFA does not have transitions that occur without consuming an input symbol 
(i.e., no ε-transitions, where ε represents the empty string).

3. **Uniqueness:** For every state and input symbol, the next state is uniquely determined.

### Components of a DFA:
- **States (Q):** A finite set of states.
- **Alphabet (Σ):** A finite set of input symbols.
- **Transition Function (δ):** A function δ: Q × Σ → Q that determines the next state based on the current 
state and input symbol.
- **Start State (q₀):** The initial state where the computation begins.
- **Accepting States (F):** A subset of Q. If the DFA ends in one of these states after processing all input 
symbols, the input is accepted.

### How DFA Works:
1. **Start:** The DFA starts in the start state \( q_0 \).
2. **Read Input:** It reads the input string one symbol at a time.
3. **State Transition:** Based on the current state and the input symbol, the DFA transitions to the next 
state as defined by the transition function.
4. **Accept or Reject:** If, after reading the entire input string, the DFA is in an accepting state, the 
input is accepted; otherwise, it is rejected.

### Example of DFA:
Consider a DFA that recognizes the string "ab" over the alphabet {a, b}.

- **States:** Q = {q₀, q₁, q₂}
- **Alphabet:** Σ = {a, b}
- **Transition Function:**
  - δ(q₀, a) = q₁
  - δ(q₁, b) = q₂
- **Start State:** q₀
- **Accepting State:** F = {q₂}

In this DFA:
- Starting in state q₀, if the input "a" is read, it moves to q₁.
- From q₁, if the input "b" is read, it moves to q₂.
- If the input string ends in q₂, it is accepted.

### Applications of DFA:
- **Lexical Analysis:** DFAs are used in compilers to recognize tokens in the source code.
- **Text Processing:** Pattern matching algorithms, like those used in grep, are often based on DFA.
- **Protocol Design:** DFAs model protocols in computer networks, ensuring that systems follow the correct 
sequence of operations.

### Summary:
A Deterministic Finite Automaton is a fundamental computational model characterized by its unambiguous 
behavior, where each input leads to exactly one possible state transition. This determinism makes DFAs 
efficient and reliable for various applications, especially in pattern recognition and formal language 
processing.
""")
    if st.button("Take Quiz", key="quiz1"):
      st.latex("Feature Under Construction ...")
      st.sidebar.snow()
chapter2_deterministic_automata()
