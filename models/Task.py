class Task:
    def __init__(self, id_task, description, priority, due_date):
        self._id_task = id_task
        self._description = description
        self._priority = priority
        self._due_date = due_date
        self._status = "en cours"

    # Getters
    def get_id(self):
        return self._id_task

    def get_description(self):
        return self._description

    def get_priority(self):
        return self._priority

    def get_due_date(self):
        return self._due_date

    def get_status(self):
        return self._status

    # Setters
    def set_id(self, id_task):
        self._id_task = id_task

    def set_description(self, description):
        self._description = description

    def set_priority(self, priority):
        self._priority = priority

    def set_due_date(self, due_date):
        self._due_date = due_date

    def set_status(self, status):
        if status in ["en cours", "terminée", "supprimée"]:
            self._status = status
