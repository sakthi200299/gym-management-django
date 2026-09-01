class PlanRequestDTO:
    """
    Equivalent to PlanRequestDTO.java in Spring Boot.
    """

    def __init__(self, data: dict):
        self.name = data.get("name", "").strip()
        self.price = data.get("price")
        self.duration = data.get("duration", "").strip()
        self.description = data.get("description", "").strip()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "duration": self.duration,
            "description": self.description,
        }
