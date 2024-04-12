import streamlit as st

st.title("Feedback para la comunidá")

st.write("Patricia no estuvo aquí")

# Display your writing
writing_text = """
Manuel es el mejor...
"""
st.write(writing_text)

# Create a text input for users to enter their feedback
feedback = st.text_area("Diganos que quiere:")

# Create a submit button
if st.button("Enviar Feedback"):
    # Save the feedback to a file or database
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")
    st.success("Muchas gracias!")
