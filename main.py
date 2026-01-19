from agent import AIAgent
from calculator import calculate
from wikipedia_tool import wiki_search
from todo import add_task, show_tasks
from jokes import tell_joke

agent = AIAgent()

print("🤖 AI Agent Started. Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    intent = agent.process_command(user_input)

    if intent == "calc":
        print("Agent:", calculate(user_input))

    elif intent == "wiki":
        topic = user_input.replace("wiki", "").replace("wikipedia", "").strip()
        print("Agent:", wiki_search(topic))

    elif intent == "todo":
        if "show" in user_input:
            print("Agent:", show_tasks(agent.todo_list))
        else:
            task = user_input.replace("add", "").replace("todo", "").strip()
            print("Agent:", add_task(agent.todo_list, task))

    elif intent == "joke":
        print("Agent:", tell_joke())

    else:
        print("Agent: Sorry, I didn’t understand that. Try asking for help!")
