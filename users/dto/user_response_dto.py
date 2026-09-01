class UserResponseDTO:
    """
    Equivalent to UserResponseDTO.java in Spring Boot.
    Holds outgoing response data sent to the client.
    """

    def __init__(self, id, name, email, phone, age, gender, joined_date):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.gender = gender
        self.joined_date = str(joined_date)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "age": self.age,
            "gender": self.gender,
            "joined_date": self.joined_date,
        }
