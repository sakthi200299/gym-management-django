class ExerciseRequestDTO:
    """
    Equivalent to ExerciseRequestDTO.java in Spring Boot.
    """

    def __init__(self, data: dict):
        self.name = data.get("name", "").strip()
        self.category = data.get("category", "").strip()
        self.sets = data.get("sets")
        self.reps = data.get("reps")
        self.duration_minutes = data.get("duration_minutes")
        self.trainer_id = data.get("trainer_id")
        self.subscription_id = data.get("subscription_id")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "category": self.category,
            "sets": self.sets,
            "reps": self.reps,
            "duration_minutes": self.duration_minutes,
            "trainer_id": self.trainer_id,
            "subscription_id": self.subscription_id,
        }
