import pandas as pd
import streamlit as st
st.set_page_config(page_title = "Study Conscious")

chapter1 = f"""
<style>
</style>
"""
def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)

def practice_finite_automata():
    st.header("Tutorial")
    st.subheader("Steps to design the Finite Automata ")
    st.write("""Creating an automaton step-by-step, starting from the language definition, is a systematic approach. Here’s how you can go about it:

### 1. **Define the Language (L):**
   - **Language Definition:** Begin by clearly defining the language you want your automaton to recognize. 
The language is a set of strings over a given alphabet (Σ).
   - **Example:** Lets design a deterministic finite automaton (DFA) that accepts strings over the alphabet 
{a,b} such that the strings contain the subsequence 'ab'.
             
here L = {["ab",] ,["aab", "bab","aba", "abb"], ... }

### 2. **Identify the Basic Components:**
   - **Smallest Unit:** Identify the smallest unit or pattern that needs to be recognized. This could be a 
single symbol or a short sequence of symbols that are critical to the language.
   - **Example:** For the language \( L \), the smallest critical sequence is "ab".
   
### 3. **Create Automata for the Smallest Unit:**
   - **Single State Automata:** Start by creating simple automata that can recognize the smallest units or 
basic patterns.
   - **Example:** 
     - Create an automaton that recognizes "a".
     - Create another automaton that recognizes "b".
   - These can be combined or extended to build the full automaton.""")
    ans_df = pd.DataFrame(columns = ['a', 'b'] , index = ['q0', 'q1','q2'], data = [['q1', ''], ['', 'q2'], ['', '']])
    df = pd.DataFrame(columns = ['a', 'b'] , index = ['q0', 'q1','q2'], data = "")
    st.write("##### Enter the data in the table to make the automa")    
    edited_df = st.data_editor(df, key="2")
    if st.button("Check"):
        if chk_answer(ans_df, edited_df):
            st.image(r"images\DFA_practice1.1.png")
        else :
            st.error("Wrong Data")
    

    st.write("""

### 6. **Test and Refine the Automaton:**
   - **Test Cases:** Use a variety of test strings (both valid and invalid) to ensure the automaton works as 
expected.
   - **Refinement:** Refine the automaton by adding or modifying states and transitions as necessary.""")
    ans_df = pd.DataFrame(columns = ['a', 'b'] , index = ['q0', 'q1','q2'], data = [['q1', 'q0'], ['q1', 'q2'], ['q2', 'q2']])
    df = pd.DataFrame(columns = ['a', 'b'] , index = ['q0', 'q1','q2'])
    st.write("##### Enter the data in the table to make the automa")
    edited_df = st.data_editor(df)
    if st.button("Check", key = "button_2"):
        if chk_answer(ans_df, edited_df):
            st.image(r"images\DFA_practice1.2.png")
        else :
            st.error("Wrong Data")
#     st.write("""
# ### **Example: Automaton to Recognize "ab"**

# 1. **Language:** L ={ w ∈ {a,b} | w contains the substring "ab"}

#                 L={w∈{a,b} 


# 2. **Smallest Unit:** The substring "ab".

# 3. **State Diagram:**
#    - **Start State (q0):** Starting state.
#    - **q1:** After reading "a".
#    - **Accept State (q2):** After reading "b" following an "a".

# 4. **Transition Function:**
#    - From `q0`, on input "a", go to `q1`.
#    - From `q1`, on input "b", go to `q2` (accepting state).
#    - From `q1`, on input "a", stay in `q1`.
#    - From `q0` and `q2`, on input "b", stay in `q0` and `q2`, respectively.

# 5. **Final Automaton:**
#    - **States:** `Q = {q0, q1, q2}`
#    - **Alphabet:** `Σ = {a, b}`
#    - **Start State:** `q0`
#    - **Accept State:** `q2`
#    - **Transition Function (δ):**
#      - δ(`q0`, `a`) = `q1`
#      - δ(`q1`, `b`) = `q2`
#      - δ(`q1`, `a`) = `q1`
#      - δ(`q0`, `b`) = `q0`
#      - δ(`q2`, `a`) = `q2`
#      - δ(`q2`, `b`) = `q2`

# This systematic approach—from defining the language to constructing the smallest unit of automata, then 
# combining them into a complete automaton—helps in building complex automata that effectively recognize the 
# language in question.
    
   #  """)
   #  st.image("images/DFA_practice1.2.png")

def chk_answer(ans_df,df):
    ans_df['a'] = ans_df['a'].str.replace(" ", "")
    ans_df['b'] = ans_df['b'].str.replace(" ", "")
    return df.equals(ans_df)
   #  edited_df = st.data_editor(df)


    
practice_finite_automata()