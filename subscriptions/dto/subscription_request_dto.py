class SubscriptionRequestDTO:

    def __init__(self, data: dict):
        self.user_id = data.get("user_id")
        self.plan_id = data.get("plan_id")
        self.start_date = data.get("start_date", "").strip()
        self.end_date = data.get("end_date", "").strip()
        self.status = data.get("status", "active").strip()

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "plan_id": self.plan_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
        }
