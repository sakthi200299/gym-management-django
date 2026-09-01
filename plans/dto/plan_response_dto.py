class PlanResponseDTO:
    """
    Equivalent to PlanResponseDTO.java in Spring Boot.
    """

    def __init__(self, id, name, price, duration, description):
        self.id = id
        self.name = name
        self.price = str(price)
        self.duration = duration
        self.description = description

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "duration": self.duration,
            "description": self.description,
        }
