from datetime import datetime

from models import Task
from controllers import TaskManager


def is_valid(date):
    """Valide une date au format DD/MM/YYYY et vérifie qu'elle est dans le futur."""
    try:
        date_fin = datetime.strptime(date, "%d/%m/%Y")
        date_fin = date_fin.replace(hour=23, minute=59, second=59, microsecond=999999)
        if date_fin >= datetime.now():
            return True
        else:
            print("L'échéance doit être supérieure à la date actuelle.")
    except ValueError:
        print("Format de date invalide. Veuillez entrer une date au format DD/MM/YYYY.")
    return False


def display_menu():
    """Affiche le menu principal."""
    menu = (
        "1. Ajouter une tâche\n"
        "2. Modifier une tâche\n"
        "3. Supprimer une tâche\n"
        "4. Lister les tâches (avec filtre)\n"
        "5. Quitter"
    )
    print(menu)


def __main__():
    task_manager = TaskManager.TaskManager()
    task_manager.init_tasks()

    while True:
        display_menu()
        try:
            choice = int(input("Entrez votre choix : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        data = task_manager.get_tasks()
        last_id = data[-1].get_id() if data else 0
        match choice:
            case 1:
                description = input("Entrez la description de votre tâche : ").strip()
                while description == "":
                    description = input("Entrez la description de votre tâche : ").strip()

                priority = input("Entrez la priorité de votre tâche (basse, moyenne, haute) : ").strip().lower()
                while priority not in ["basse", "moyenne", "haute"]:
                    priority = input("Entrez la priorité de votre tâche (basse, moyenne, haute) : ").strip()

                while True:
                    due_date = 0
                    try:
                        # Demander à l'utilisateur d'entrer une date
                        due_date = input("Ajouter une date limite à la tâche (format DD/MM/YYYY) : ").strip()
                        # Essayer de convertir la chaîne en objet datetime
                        due_date_obj = datetime.strptime(due_date, "%d/%m/%Y")
                        if is_valid(due_date):
                            break  # Sort de la boucle si la date est valide
                    except ValueError or not is_valid(due_date):
                        # Si une erreur survient, afficher un message et redemander
                        print("Format de date invalide. Veuillez entrer une date au format DD/MM/YYYY.")

                task = Task.Task(last_id + 1, description, priority, due_date)
                task_manager.add_task(task)
                print(f"Tâche ajoutée : {task.get_description()}")
                task_manager.save_data()
            case 2:
                # Modification d'une tâche
                if not task_manager.get_tasks():
                    print("Aucune tâche disponible à modifier.")
                    continue
                try:
                    id_task = int(input("Entrez le numéro de la tâche à modifier : "))
                except ValueError:
                    print("Identifiant invalide.")
                    continue
                task = task_manager.find_task_by_id(id_task)
                if task:
                    description = input(
                        f"Entrez la description de votre tâche [{task.get_description()}] : ").strip() or task.get_description()
                    priority = input(
                        f"Entrez la priorité (basse, moyenne, haute) [{task.get_priority()}]: ").strip().lower() or task.get_priority()
                    while priority not in ["basse", "moyenne", "haute"]:
                        priority = input("Priorité invalide. Réessayez (basse, moyenne, haute) : ").strip().lower()
                    while True:
                        due_date = input(
                            f"Entrez l'échéance (format DD/MM/YYYY) [{task.get_due_date()}]: ").strip() or task.get_due_date()
                        if is_valid(due_date):
                            break
                    status = input(
                        f"Entrez le statut (en cours, terminée, supprimée) [{task.get_status()}]: ").strip().lower() or task.get_status()
                    while status not in ["en cours", "terminée", "supprimée"]:
                        status = input(
                            "Statut invalide. Réessayez (en cours, terminée, supprimée) : ").strip().lower()

                    task.set_description(description)
                    task.set_priority(priority)
                    task.set_due_date(due_date)
                    task.set_status(status)
                    task_manager.save_data()
                    print(f"La tâche {task.get_id()} a été modifiée avec succès.")
                else:
                    print("Aucune tâche ne correspond au numéro entrée.")
            case 3:
                id_task = int(input("Entrez le numéro de la tâche à supprimer : "))
                task_manager.remove_task(id_task)
                task_manager.save_data()
            case 4:
                while choice not in ["s", "p", "d", ""]:
                    choice = input(
                        "Filtrer par (s)tatut/(p)riorité/(d)ate ou appuyez sur Entrée pour tout afficher : ").strip().lower()
                while True:
                    try:
                        page_size = input(
                            "Entrez le nombre d'éléments par page (laissez vide pour la liste complète) : ") or len(
                            task_manager.get_tasks())
                        page_size = int(page_size)
                        if page_size <= 0:
                            print("Le nombre d'éléments par page doit être positif.")
                            continue
                        break
                    except ValueError:
                        print("Entrez un nombre valide.")
                if choice == "s":
                    status = input("Entrez le statut (en cours/terminée/supprimée) : ")
                    task_manager.list_tasks(filter_by="statut", filter_value=status, page_size=page_size)
                elif choice == "p":
                    priority = input("Entrez la priorité (basse/normale/haute) : ")
                    task_manager.list_tasks(filter_by="priorité", filter_value=priority, page_size=page_size)
                elif choice == "d":
                    task_manager.list_tasks(filter_by="date", page_size=page_size)
                else:
                    task_manager.list_tasks(page_size=page_size)
            case 5:
                print("Au revoir !")
                break
            case _:
                print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    __main__()
