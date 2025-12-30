class UserProfile:
    def __init__(self):
        self.name = None
        self.email = None
        self.phone = None


class UserProfileBuilder:
    def __init__(self):
        self.profile = UserProfile()

    def set_name(self, name):
        self.profile.name = name
        return self

    def set_email(self, email):
        self.profile.email = email
        return self

    def set_phone(self, phone):
        self.profile.phone = phone
        return self

    def build(self):
        return self.profile


profile = (
    UserProfileBuilder()
    .set_name("Manas")
    .set_email("manas@mail.com")
    .build()
)

print(profile.name, profile.email)
