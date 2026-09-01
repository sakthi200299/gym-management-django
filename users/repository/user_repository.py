from users.model.user import User


def save(data: dict) -> User:
    return User.objects.create(**data)


def update(user: User, data: dict) -> User:
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    return user


def find_all_objects() -> list:
    return list(User.objects.all())


def find_by_id(user_id: int) -> User | None:
    return User.objects.filter(id=user_id).first()


def find_by_username(username: str) -> User | None:
    return User.objects.filter(username=username).first()


def find_by_email(email: str) -> User | None:
    return User.objects.filter(email=email).first()


def exists_by_email(email: str) -> bool:
    return User.objects.filter(email=email).exists()


def exists_by_username(username: str) -> bool:
    return User.objects.filter(username=username).exists()
