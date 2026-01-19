class AIAgent:
    def __init__(self):
        self.todo_list = []

    def process_command(self, user_input):
        user_input = user_input.lower()

        if any(word in user_input for word in ["add", "todo", "task"]):
            return "todo"

        if any(word in user_input for word in ["calculate", "+", "-", "*", "/"]):
            return "calc"

        if "wiki" in user_input or "wikipedia" in user_input:
            return "wiki"

        if "joke" in user_input or "funny" in user_input:
            return "joke"

        return "unknown"
