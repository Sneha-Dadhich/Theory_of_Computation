import streamlit as st
from PIL import Image
st.set_page_config(page_title = "Study Conscious")

chapter1 = f"""
<style>
[data-testid="stVerticalBlockBorderWrapper"]
{{
    color: 'red ' ; 
}}
</style>
"""
def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)


def chapter2_intro():
    st.header("Intoduction")
    st.subheader("What is Automata ?")
    

    st.write(f"""**Automata** refers to abstract machines or mathematical models that can simulate the 
behavior of computational systems. An automaton (singular of automata) operates on inputs, processes them 
according to a set of predefined rules, and produces outputs. The study of automata is a foundational topic 
in the Theory of Computation.""")
    image = Image.open("static/images/types_of_automata.png")
    st.image(image, caption='Types of Automata')

    st.write(f"""
### Types of Automata:
1. **Finite Automata (FA):** The simplest type, with a limited number of states. It's used to recognize 
regular languages.
2. **Pushdown Automata (PDA):** Equipped with a stack, allowing it to recognize context-free languages.
3. **Turing Machines:** The most powerful, capable of simulating any algorithm. It forms the basis for 
defining what is computable.

### Uses of Automata:
- **Language Recognition:** Automata are used to recognize patterns and sequences in languages, making them
crucial in the design of compilers and interpreters.
- **Modeling Computational Processes:** Automata provide a framework for understanding how machines compute 
and process data.
- **Design of Digital Circuits:** Finite Automata are used in designing sequential logic circuits.
- **Formal Verification:** Automata are used to prove the correctness of algorithms and systems in software 
engineering.

### Short Note:
Automata theory is a branch of computer science that deals with the study of abstract machines and the 
computational problems they can solve. It plays a critical role in the development of programming languages, 
artificial intelligence, and the design of hardware systems. By understanding automata, one can gain insights
into the limits of what machines can compute and how different types of problems can be approached 
algorithmically.""")
    
    if st.button("Take Quiz", key="quiz1"):
        # st.latex("hi")
        # st.sidebar.snow()
        st.switch_page("pages/quiz1.py")
        

chapter2_intro()

