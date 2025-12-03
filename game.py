import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize the secret number in session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.game_over = False

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Input from user
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if st.session_state.game_over:
        st.warning("Click 'Restart Game' to play again.")
    else:
        if guess < st.session_state.secret_number:
            st.info("Too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.info("Too high! Try again.")
        else:
            st.success("🎉 Correct! You guessed the number!")
            st.session_state.game_over = True

# Restart button
if st.button("Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.game_over = False
    st.experimental_rerun()
