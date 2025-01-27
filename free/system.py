class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def get_info(self):
        return f'Username: {self.username}, Email: {self.email}'


class Admin(User):
    def delete_user(self, user: User):
        print(f"{self.username} has been deleted by admin {self.username}.")

    def get_info(self):
        return f'Admin: {self.username}, Email: {self.email}'


class Moderator(User):
    def __init__(self, username: str, email: str, ):
        super().__init__(username, email)
        self.moderator_sections = []

    def add_section(self, section: str):
        if section not in self.moderator_sections:
            self.moderator_sections.append(section)

    def remove_section(self, section: str):
        if section in self.moderator_sections:
            self.moderator_sections.remove(section)

    def get_info(self):
        sections = ', '.join(self.moderator_sections) if self.moderator_sections else "None"
        return f'Moderator: {self.username}, Email: {self.email}, Moderator sections: {sections}'


class RegularUser(User):
    def post_comment(self, section: str, comment: str):
        print(f"{self.username} posted a comment in {section}: {comment}")

    def get_info(self):
        return f"Regular User: {self.username}, Email: {self.email}"


if __name__ == "__main__":
    # Создаем пользователей
    admin = Admin("AdminUser", "admin@example.com")
    moderator = Moderator("ModUser", "moderator@example.com")
    user = RegularUser("RegularUser", "user@example.com")

    # Добавляем секции модератору
    moderator.add_section("Tech")
    moderator.add_section("Gaming")

    # Пользователь публикует комментарий
    user.post_comment("Tech", "This is a great article!")

    # Администратор удаляет пользователя
    admin.delete_user(user)

    # Вывод информации о пользователях
    print(admin.get_info())  # Username: AdminUser, Email: admin@example.com (Role: Admin)
    print(
        moderator.get_info())  # Username: ModUser, Email: moderator@example.com (Role: Moderator, Sections: Tech, Gaming)
    print(user.get_info())  # Username: RegularUser, Email: user@example.com (Role: Regular User)