#1 

class Task:
    def __init__(self, title, description, due_date, status=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    def __str__(self):
        status_text = "✅ Completed" if self.status == "Completed" else "❌ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue date: {self.due_date}\nStatus: {status_text}\n"
        

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task.title} added!")

    def mark_task_complete(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.status = "Completed"
                return f"Task '{task_title}' marked as completed."
        return f"Task '{task_title}' not found."

    def list_all_tasks(self):
        for task in self.tasks:
            print(task)

    def show_incomplete_tasks(self):
        for task in self.tasks:
            if task.status != "Completed":
                print(task)

def main_menu():
    print("1. Add task")
    print("2. Complate the task")
    print("3. Show all tasks")
    print("4. Show incomplate task")
    print("5. Exit")

def main():
    todo = ToDoList()

    while True:
        main_menu()
        select = input("Choose function (1-5):")
        if select == "1":
            title = input("Input the name of task: ")
            description = input("Input the description of the task: ")
            due_date = input("Input the deadline day (DD-MM-YYYY): ")
            task = Task(title,description,due_date)
            todo.add_task(task)

        elif select == "2":
            title = input("Input the name of task that has complated: ")
            todo.mark_task_complete(title)

        elif select == "3":
            todo.list_all_tasks()

        elif select == "4":https://github.com/ellipse1995/hw-python/tree/main
            todo.show_incomplete_tasks()
        elif select == "5":
            break
        else:
            break


main()


#2

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
class Blog:
    def __init__(self):
        self.posts = []
        
    def add_post(self, post):
        self.posts.append(post)
        print("Post added")

    def list_all_post(self):
        for post in self.posts:
            print(post)
    
    def display_by_author(self):
        author = input('Input the author name')
        for name in self.posts:
            if name.author == author:
                print(name)

def main():
    blog = Blog()

    while True:
        print("1. Add post")
        print("2. Show all posts")
        print("3. Search post by author")
        print("4. Exit")
        option = input("Choose option (1-4): ")

        if option == "1":
            title = input("Input title of post")
            content = input("Input content of post")
            author = input("Input author of post")
            post = Post(title,content,author)
            blog.add_post(post)
        
        elif option == "2":
            blog.list_all_post()

        elif option == "3":
            blog.display_by_author()
        
        elif option == "4":
            break

        else:
            break



        
main()







