import streamlit as st
import math

st.title('Scientific Calculator')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    return math.log(x, base)

# User Interface with Streamlit
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Sine", "Cosine", "Tangent", "Logarithm"])

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number", step=1e-6)
    num2 = st.number_input("Enter second number", step=1e-6)

if operation == "Add":
    st.write(f"{num1} + {num2} = {add(num1, num2)}")

elif operation == "Subtract":
    st.write(f"{num1} - {num2} = {subtract(num1, num2)}")

elif operation == "Multiply":
    st.write(f"{num1} * {num2} = {multiply(num1, num2)}")

elif operation == "Divide":
    st.write(f"{num1} / {num2} = {divide(num1, num2)}")

elif operation == "Power":
    st.write(f"{num1} ^ {num2} = {power(num1, num2)}")

elif operation == "Square Root":
    num = st.number_input("Enter number", step=1e-6)
    st.write(f"Square root of {num} = {sqrt(num)}")

elif operation == "Sine":
    angle = st.number_input("Enter angle in degrees", step=1e-6)
    st.write(f"Sine({angle}) = {sin(angle)}")

elif operation == "Cosine":
    angle = st.number_input("Enter angle in degrees", step=1e-6)
    st.write(f"Cosine({angle}) = {cos(angle)}")

elif operation == "Tangent":
    angle = st.number_input("Enter angle in degrees", step=1e-6)
    st.write(f"Tangent({angle}) = {tan(angle)}")

elif operation == "Logarithm":
    num = st.number_input("Enter number", step=1e-6)
    base = st.number_input("Enter base (default is 10)", step=1e-6, value=10.0)
    st.write(f"log({num}, base {base}) = {log(num, base)}")
