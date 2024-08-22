
from graphviz import Digraph
import pandas as pd
import streamlit as st
st.set_page_config(page_title = "Study Conscious")

chapter1 = f"""
<style>
</style>
"""
def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)


def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)

# Function to create and display DFA
def create_dfa(states, alphabet, transitions, start_state, accept_states):
    dfa = Digraph()

    # Mark start state
    dfa.attr('node', shape='plaintext')
    dfa.node('start', label = "")
    dfa.edge('start', start_state, label="e")

    # Add transitions
    for transition in transitions.items():
        src = transition[0]
        for route , dst in transition[1].items():  
            if src in accept_states and (dst.strip() != '') and dst in states:
                dfa.node(src, label=src, shape='doublecircle') 
                dfa.edge(src, dst, label=route)
            elif ((not dst) or (dst.strip() == '')) and src not in accept_states:
                dfa.node(src, label=src, shape='circle')
                pass
            elif not dst or dst.strip() == '' and src in accept_states:
                dfa.node(src, label=src, shape='doublecircle')
            elif src in states and src not in accept_states and dst in states:
                dfa.node(src, label=src, shape='circle')
                dfa.edge(src, dst, label=route)
            elif dst not in states:
                st.error("Incorrect state in the table")
           
    return dfa

# Streamlit UI
def main():
    st.title("DFA Simulator")

    # User inputs for DFA
    states = st.text_input("Enter states (comma-separated):").split(',')
    alphabet = st.text_input("Enter the input symbols (comma-separated):").split(',')
    start_state = st.text_input("Enter start state:")
    accept_states = st.text_input("Enter accept states / final states (comma-separated):").split(',')

    # cleaning the inputs before processing
    states = [state.replace(" ","") for state in states]
    alphabet = [letter.replace(" ","") for letter in alphabet]
    accept_states = [state.replace(" ","") for state in accept_states]
    start_state = start_state.replace(" ","")
    
    # Transition function input
    st.subheader("Define transition function")

    # forming the table of streamlit
    # Initial scorecard dataframe
    df = pd.DataFrame(columns=alphabet, index=states, data = [[""] * (len(alphabet))])

    # Create an interactive table where users can edit cells
    st.write("### Interactive Table with Editable Cells")
    edited_df = st.data_editor(df)

    # DFA creation and visualization
    if st.button("Create DFA"):
        try:
            transitions = { 
                edited_df.index[i].strip() :{transition.strip() : edited_df.iloc[i][transition].strip() for transition in alphabet} 
                for i in range(edited_df.shape[0])
                }

            dfa = create_dfa(states, alphabet, transitions, start_state, accept_states)
            dfa.attr(rankdir="LR",kw='graph')
            st.graphviz_chart(str(dfa))

            # Rotate button
            if st.button("Rotate"):
                dfa.attr(rankdir="LR", kw='graph')
                st.graphviz_chart(str(dfa))  
        
            if st.button("Take Quiz", key="quiz1"):
                st.latex("Feature Under Construction ...")
                st.sidebar.snow()
        except Exception as e:
            print(f"{e}")
            st.error(f"{e}")
        
if __name__ == "__main__":
    main()















a = '''
video link = https://www.youtube.com/watch?v=UUGkEPkas2g&t=6s
video github = https://github.com/AbhiLegend/DFA_visualizer/blob/main/dfa.py
link -> https://pypi.org/project/visual-automata/
custom navigation = https://docs.streamlit.io/develop/tutorials/multipage/st.page_link-nav

from pythomata import SimpleDFA

# Define the alphabet, states, initial state, accepting states, and transition function
alphabet = {"a", "b"}
states = {"q0", "q1", "q2"}
initial_state = "q0"
accepting_states = {"q2"}
transition_function = {
    "q0": {"a": "q0", "b": "q1"},
    "q1": {"a": "q2", "b": "q1"},
    "q2": {"a": "q0", "b": "q1"},
}

# Create the DFA
dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)

# Test if a string is accepted by the DFA
print(dfa.accepts("aab"))  # True
print(dfa.accepts("abb"))  # True
print(dfa.accepts("aaa"))  # False
'''

