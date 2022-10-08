import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpeg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of every DNA
***
""")

st.header('Enter your DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines() #basically just splitting the lines
sequence = sequence[1:] #to skip the sequence name at the first line
sequence = ''.join(sequence) #concatenate list to string

st.write("""
***
""")

## prints the input dna sequence 
st.header('Input (DNA Query)')
sequence

## DNA nucleotide count 
st.header('Output (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(sequence):
    d = dict([
        ('A',sequence.count('A')),
        ('T',sequence.count('T')),
        ('G',sequence.count('G')),
        ('C',sequence.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence=sequence)

X

## 2. Print text
st.subheader('2. Print text')
st.write('There are ' +str(X['A']) + ' adenine (A)')
st.write('There are ' +str(X['T']) + ' thymine (T)')
st.write('There are ' +str(X['G']) + ' guanine (G)')
st.write('There are ' +str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
