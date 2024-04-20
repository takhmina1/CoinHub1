class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.email_confirmed = False

# Функция для регистрации нового пользователя
def register_user(users_list, username, email, password):
    for user in users_list:
        if user.username == username:
            return "Пользователь с таким именем уже существует"
        if user.email == email:
            return "Пользователь с такой почтой уже существует"
    new_user = User(username, email, password)  # Создаем новый экземпляр класса User
    users_list.append(new_user)  # Добавляем пользователя в список пользователей
    return "Пользователь успешно зарегистрирован"

# Функция для аутентификации пользователя
def authenticate_user(users_list, username, password):
    for user in users_list:
        if user.username == username and user.password == password:
            return user
    return None

# Функция для подтверждения электронной почты
def confirm_email(users_list, email):
    for user in users_list:
        if user.email == email:
            user.email_confirmed = True
            return "Email успешно подтвержден"
    return "Пользователь с такой почтой не найден"

# Функция для сброса пароля
def reset_password(users_list, email, new_password):
    for user in users_list:
        if user.email == email:
            user.password = new_password
            return "Пароль успешно изменен"
    return "Пользователь с такой почтой не найден"

# Функция для изменения пароля
def change_password(users_list, username, old_password, new_password):
    for user in users_list:
        if user.username == username and user.password == old_password:
            user.password = new_password
            return "Пароль успешно изменен"
    return "Пользователь с таким именем и паролем не найден"
