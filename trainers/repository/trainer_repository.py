from trainers.model.trainer import Trainer


def save(data: dict) -> Trainer:
    return Trainer.objects.create(**data)


def update(trainer: Trainer, data: dict) -> Trainer:
    for key, value in data.items():
        setattr(trainer, key, value)
    trainer.save()
    return trainer


def find_all_objects() -> list:
    return list(Trainer.objects.all())


def find_by_id(trainer_id: int) -> Trainer | None:
    return Trainer.objects.filter(id=trainer_id).first()


def exists_by_email(email: str) -> bool:
    return Trainer.objects.filter(email=email).exists()
