import json
import os.path

from models.Task import Task


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []

    # Getters
    def get_tasks(self):
        return self.tasks

    def find_task_by_id(self, id_task):
        for task in self.tasks:
            if task.get_id() == id_task:
                return task
        return None

    # Setters
    def set_tasks(self, tasks):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tâche ajoutée : {task.get_description()}")

    def remove_task(self, id_task):
        for task in self.tasks:
            if task.get_id() == id_task:
                task.set_status("supprimée")
                print(f"Tâche '{id_task}' supprimée avec succès.")
                return
        print(f"Aucune tâche trouvée avec l'identifiant '{id_task}'.")

    def save_data(self):
        """Sauvegarder les données dans le fichier JSON."""
        task_json = os.path.abspath("tasks.json")
        with open(task_json, "w", encoding="utf-8") as file:
            data = {
                "tasks": [
                    {
                        "id": task.get_id(),
                        "description": task.get_description(),
                        "priority": task.get_priority(),
                        "due_date": task.get_due_date(),
                        "status": task.get_status()
                    } for task in self.tasks
                ]
            }
            json.dump(data, file, indent=4)

    def init_tasks(self):
        task_json = os.path.abspath("tasks.json")
        if not os.path.exists(task_json):
            self.save_data()

        try:
            with open(task_json, "r", encoding="utf-8") as file:
                data = json.load(file)
                if data:
                    tasks = data["tasks"]
                    for task_data in tasks:
                        task = Task(
                            task_data["id"],
                            task_data["description"],
                            task_data["priority"],
                            task_data["due_date"]
                        )
                        task.set_status(task_data["status"])
                        self.add_task(task)
        except Exception as e:
            print(e)

    def list_tasks(self):
        """Affiche les archives sous forme tabulaire."""
        header = ("No", "Description", "Priorité", "Echéance", "Statut")
        tailles = [5, 30, 10, 15, 15]

        line_format = '| ' + ''.join([f"%-{v}s| " for v in tailles])
        horz_line = "-" * (len(line_format % header) - 1)

        print(horz_line)
        print(line_format % header)
        print(horz_line)

        for task in self.get_tasks():
            idx = task.get_id()
            description = task.get_description()
            priority = task.get_priority()
            due_date = task.get_due_date()
            status = task.get_status()
            data = (idx, description, priority, due_date, status)
            print(line_format % data)
        print(horz_line)
