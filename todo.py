def add_task(todo_list, task):
    todo_list.append(task)
    return f"Task added: {task}"

def show_tasks(todo_list):
    if not todo_list:
        return "Your to-do list is empty."

    return "\n".join(
        [f"{i+1}. {task}" for i, task in enumerate(todo_list)]
    )
