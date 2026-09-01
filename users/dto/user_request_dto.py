class UserRequestDTO:
    """
    Equivalent to UserRequestDTO.java in Spring Boot.
    Holds incoming request data from the client.
    """

    def __init__(self, data: dict):
        self.username = data.get("username", "").strip()
        self.password = data.get("password", "").strip()
        self.name = data.get("name", "").strip()
        self.email = data.get("email", "").strip()
        self.phone = data.get("phone", "").strip()
        self.age = data.get("age")
        self.gender = data.get("gender", "").strip()

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "age": self.age,
            "gender": self.gender,
        }
