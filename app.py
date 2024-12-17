import streamlit as st

# Dictionary of major operation budgets
operation_budgets = {
    "heart surgery": 50000,
    "knee replacement": 30000,
    "appendix removal": 15000,
    "organ transplant": 100000,
    "cancer treatment": 70000,
    "spinal surgery": 40000,
    "brain surgery": 80000,
    "eye surgery": 20000,
    "childbirth (C-section)": 12000,
    "childbirth (normal delivery)": 6000,
}

# Function to query operation budgets
def query_operation_budget(user_input):
    user_input = user_input.lower()
    for operation, budget in operation_budgets.items():
        if operation in user_input:
            return f"The estimated budget for **{operation}** is **${budget:,}**."
    return "Sorry, I couldn't find that operation. Please ask about a major operation like heart surgery, organ transplant, or cancer treatment."

# Streamlit UI
st.title("🏥 Major Operations Budget Chatbot")
st.write("Welcome! Ask me about the estimated budgets for major operations like heart surgery, organ transplants, and more.")

# User query input
user_query = st.text_input("Enter the operation you want to know about:", "")

# Button to trigger response
if st.button("Get Budget Estimate"):
    if user_query:
        response = query_operation_budget(user_query)
        st.success(response)
    else:
        st.warning("Please enter an operation to get the budget details.")
