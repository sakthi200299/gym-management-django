class TrainerRequestDTO:
    """
    Equivalent to TrainerRequestDTO.java in Spring Boot.
    """

    def __init__(self, data: dict):
        self.name = data.get("name", "").strip()
        self.email = data.get("email", "").strip()
        self.phone = data.get("phone", "").strip()
        self.specialization = data.get("specialization", "").strip()
        self.experience_years = data.get("experience_years")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "specialization": self.specialization,
            "experience_years": self.experience_years,
        }
