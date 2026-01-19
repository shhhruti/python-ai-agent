def calculate(user_input):
    try:
        # Remove the word 'calculate' if present
        expression = user_input.lower().replace("calculate", "").strip()
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid calculation."
