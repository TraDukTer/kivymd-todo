# python -m venv env
# env\scripts\activate
# pip install kivymd

from kivymd.app import MDApp
from task_classes import CreateTaskDialog, TodoItem

class Main(MDApp):
    
    def on_start(self):
        self.populate_tasks_from_file()

    def populate_tasks_from_file(self, file_name = "task_cache"):
        tasks_list = []
        with open(file_name, "r", encoding="utf8") as file:
            tasks_list = file.read().split("#endtask#\n\n")
        for task in tasks_list:
            task_as_list = task.split("\n")
            task_text = task_as_list[0]
            if len(task_as_list) > 1:
                task_date = task_as_list[1]
            if task_text != "":
                self.add_task_widget(task_text)

        
    def save_task_to_file(self, task_textfield, date):
        with open("task_cache", "a", encoding="utf8") as file:
            file.write(f"{task_textfield.text}\n{date.text} #endtask#\n\n")


    def show_create_task_dialog(self):
        self.task_dialog = CreateTaskDialog(title="CREATE TASK")
        self.task_dialog.open() 

    def close_dialog(self):
        self.task_dialog.dismiss()
        
    def add_task_widget(self, task_text):
        self.root.ids['container'].add_widget(TodoItem(text=task_text))

    def add_task(self, task_textfield):
        #print(task_textfield.text)
        self.add_task_widget(task_textfield.text)

if __name__ == '__main__':
    Main().run()