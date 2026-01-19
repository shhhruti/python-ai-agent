from flask import Flask, render_template, request
from agent import AIAgent
from calculator import calculate
from wikipedia_tool import wiki_search
from todo import add_task, show_tasks
from jokes import tell_joke
from llm_helper import ask_llm


app = Flask(__name__)
agent = AIAgent()

# Chat history stored per session (simple in-memory)
chat_history = []

def get_agent_response(user_input):
    intent = agent.process_command(user_input)

    if intent == "calc":
        return calculate(user_input)

    elif intent == "wiki":
        topic = user_input.replace("wiki", "").replace("wikipedia", "").strip()
        return wiki_search(topic)

    elif intent == "todo":
        if "show" in user_input:
            return show_tasks(agent.todo_list)
        else:
            task = user_input.replace("add", "").replace("todo", "").strip()
            return add_task(agent.todo_list, task)

    elif intent == "joke":
        return tell_joke()

    else:
        return ask_llm(user_input, chat_history)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]

        agent_response = get_agent_response(user_input)

        chat_history.append({
            "user": user_input,
            "agent": agent_response
        })

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
