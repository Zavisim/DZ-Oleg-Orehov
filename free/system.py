class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def get_info(self):
        return f'Username: {self.username}, Email: {self.email}'


class Admin(User):
    def delete_user(self):
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
    # Create users
    admin = Admin("admin1", "admin1@example.com")
    moderator = Moderator("mod1", "mod1@example.com")
    user = RegularUser("user1", "user1@example.com")

    # Display user info
    print(admin.get_info())
    print(moderator.get_info())
    print(user.get_info())

    # Admin deletes a user
    admin.delete_user(user)

    # Moderator manages sections
    moderator.add_section("Sports")
    moderator.add_section("Technology")
    print(moderator.get_info())
    moderator.remove_section("Sports")
    print(moderator.get_info())

    # Regular user posts a comment
    user.post_comment("Technology", "Great article!")
