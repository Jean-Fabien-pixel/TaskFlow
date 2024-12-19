

def list_tasks():
    """Affiche les archives sous forme tabulaire."""
    header = ("Description", "Priorité", "Echéance", "Statut")
    tailles = [30, 10, 15, 15]

    line_format = '| ' + ''.join([f"%-{v}s| " for v in tailles])
    horz_line = "-" * (len(line_format % header) - 1)

    print(horz_line)
    print(line_format % header)
    print(horz_line)

    for row in rows:
        last_modified = format_mtime(row[2])
        name = truncate_string(str(row[0]), tailles[0] - 1)
        data = (name, str(row[1]), last_modified)
        print(line_format % data)
    print(horz_line)

tasks = []


def __main__():
    menu = "1. Ajouter une tâche\n2. Modifier une tâche\n3. Supprimer une tâche\n4. Lister les tâches (avec filtre)\n5. Quitter"
    print(menu)
    choice = int(input("Entrez votre choix : "))
    while choice != 5:
        match choice:
            case 1:
                description = input("Entrez la description de votre tâche :")
                priority = input("Entrez la priorité de votre tâche (basse, moyenne, haute) :")
                due_date = input("Ajouter une date limite à la tâche (format DD/MM/YYYY) :")
                status = "en cours"
                task = {
                    "description": description,
                    "priority": priority,
                    "due_date": due_date,
                    "status": status
                }
                tasks.append(task)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                pass

        menu = "1. Ajouter une tâche\n2. Modifier une tâche\n3. Supprimer une tâche\n4. Lister les tâches (avec filtre)\n5. Quitter"
        print(menu)


if __name__ == "__main__":
    __main__()
