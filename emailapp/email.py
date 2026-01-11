class Email:
    def __init__(self, id, title, description, time, status):
        self.id = id
        self.title = title
        self.description = description
        self.time = time
        self.status = status

EMAIL_STORE = {
    Email(0,"Thong bao lich phong van 1", "Phong van luc 11:00" ,"05/05/2025", False),
    Email(1,"Thong bao lich phong van 2", "Phong van luc 12:00" ,"05/05/2025", True),
    Email(2,"Thong bao lich phong van 3", "Phong van luc 13:00" ,"05/05/2025", False)
}

def get_Email_list():
    return EMAIL_STORE

def get_Email_by_id(id):
     emails = get_Email_list()
     return emails[id]

def delete_email_by_id(id):
    global EMAIL_STORE
    EMAIL_STORE = [email for email in EMAIL_STORE if email.id != id ]