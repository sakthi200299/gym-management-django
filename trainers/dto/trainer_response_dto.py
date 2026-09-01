class TrainerResponseDTO:
    """
    Equivalent to TrainerResponseDTO.java in Spring Boot.
    """

    def __init__(self, id, name, email, phone, specialization, experience_years):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.specialization = specialization
        self.experience_years = experience_years

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "specialization": self.specialization,
            "experience_years": self.experience_years,
        }
