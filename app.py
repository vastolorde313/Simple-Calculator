# Save this as app.py and run using: streamlit run app.py

import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Choose operation
operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])

# Calculate when button is clicked
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "-":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "*":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Cannot divide by zero!")
