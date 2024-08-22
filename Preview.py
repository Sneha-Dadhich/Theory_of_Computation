import streamlit as st

st.set_page_config(page_title = "Automata")
# st.sidebar.success("Chapters") 


chapter1 = f"""
<style>
</style>
"""

def apply_css(css):
    st.markdown(css,unsafe_allow_html=True)

def chapter2_preview():
    st.header("Automata")
    st.subheader("Preview")
    st.sidebar.title("Chapters")
    st.write(f"""The chapter "Automata" in the Theory of Computing delves into one of the core concepts of 
theoretical computer science: the study of abstract machines and the computational problems they can solve.
Automata theory is essential for understanding how computers and other systems process information and 
recognize patterns.

Key topics covered in this chapter include:

1. **Introduction to Automata**: The chapter begins by defining automata and their significance in 
computational theory. It explains how automata serve as mathematical models of computation that can simulate 
real-world processes and systems.

2. **Finite Automata**: A detailed exploration of finite automata, including both deterministic (DFA) and 
non-deterministic (NFA) finite automata. The chapter discusses how these machines recognize regular languages 
and how they are used in applications like lexical analysis and text processing.

3. **Regular Expressions and Languages**: The chapter explains the relationship between finite automata and 
regular expressions, showing how regular expressions can be used to describe patterns in strings. It also 
covers the concept of regular languages, which are languages that can be recognized by finite automata.

4. **Closure Properties**: The chapter examines the closure properties of regular languages, explaining how 
operations like union, intersection, concatenation, and Kleene star affect these languages and how they can be
used to build more complex languages from simpler ones.

5. **Minimization of Automata**: Techniques for minimizing finite automata are presented, showing how to 
reduce the number of states in a DFA without changing the language it recognizes. This section highlights the 
importance of efficient computation.

6. **Context-Free Grammars and Pushdown Automata**: The chapter introduces context-free grammars (CFGs) and 
pushdown automata (PDA), expanding on the limitations of finite automata and explaining how PDAs can recognize
context-free languages, which are more complex than regular languages.

7. **Applications of Automata**: Practical applications of automata theory are discussed, including their role 
in designing compilers, parsing programming languages, and modeling systems in software engineering and 
network protocols.

8. **Limitations of Automata**: The chapter concludes with a discussion of the limitations of different types 
of automata, leading to the exploration of more powerful computational models like Turing machines.

By the end of this chapter, readers will have a comprehensive understanding of automata, their types, and 
their applications in computing. This knowledge is fundamental for further studies in areas such as compiler
design, formal verification, and complexity theory.
""")
    
chapter2_preview()
