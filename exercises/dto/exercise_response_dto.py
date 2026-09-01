class ExerciseResponseDTO:
    """
    Equivalent to ExerciseResponseDTO.java in Spring Boot.
    """

    def __init__(self, id, name, category, sets, reps, duration_minutes, trainer: dict, subscription: dict):
        self.id = id
        self.name = name
        self.category = category
        self.sets = sets
        self.reps = reps
        self.duration_minutes = duration_minutes
        self.trainer = trainer
        self.subscription = subscription

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "sets": self.sets,
            "reps": self.reps,
            "duration_minutes": self.duration_minutes,
            "trainer": self.trainer,
            "subscription": self.subscription,
        }
