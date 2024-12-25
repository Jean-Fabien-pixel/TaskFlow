import json
import os.path

from models.Task import Task


def truncate_string(s, max_len):
    """Tronquer les noms de fichiers trop long."""
    if len(s) > max_len:
        return s[:(max_len - 3)] + '...'
    return s


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

    def list_tasks(self, filter_by=None, filter_value=None, page_size=15):
        """
        Affiche les tâches sous forme paginée avec des options de filtre.
        Paramètres :
            filter_by (str) : Le critère de filtre ("statut", "priorité", "date").
            filter_value (str) : La valeur du filtre à appliquer.
            page_size (int) : Nombre de tâches à afficher par page.
        """
        header = ("No", "Description", "Priorité", "Échéance", "Statut")
        tailles = [5, 30, 10, 15, 15]

        line_format = '| ' + ''.join([f"%-{v}s| " for v in tailles])
        horz_line = "-" * (len(line_format % header) - 1)

        # Récupérer les tâches et appliquer le filtre
        tasks = self.get_tasks()
        if filter_by and filter_value:
            if filter_by == "statut":
                tasks = [task for task in tasks if task.get_status() == filter_value]
            elif filter_by == "priorité":
                tasks = [task for task in tasks if task.get_priority() == filter_value]
            elif filter_by == "date":
                tasks = sorted(tasks, key=lambda task: task.get_due_date())  # Tri par date croissante

        total_tasks = len(tasks)
        total_pages = (total_tasks + page_size - 1) // page_size  # Calculer le nombre de pages
        current_page = 1

        while True:
            start_idx = (current_page - 1) * page_size
            end_idx = start_idx + page_size
            current_tasks = tasks[start_idx:end_idx]

            # Afficher les tâches pour la page courante
            print(horz_line)
            print(line_format % header)
            print(horz_line)

            for task in current_tasks:
                idx = task.get_id()
                description = truncate_string(task.get_description(), tailles[1] - 3)
                priority = task.get_priority()
                due_date = task.get_due_date()
                status = task.get_status()
                data = (idx, description, priority, due_date, status)
                print(line_format % data)

            print(horz_line)

            # Navigation dans les pages
            print(f"\nPage {current_page}/{total_pages}")
            print("\nOptions :")
            print("n - Page suivante | p - Page précédente | q - Quitter")
            choice = input("Choisissez une option : ").lower()

            if choice == "n" and current_page < total_pages:
                current_page += 1
            elif choice == "p" and current_page > 1:
                current_page -= 1
            elif choice == "q":
                break
            else:
                print("Option invalide ou fin des pages.")
