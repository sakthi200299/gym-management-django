import hashlib

from users.repository import user_repository
from users.dto.user_request_dto import UserRequestDTO
from users.mapper.user_mapper import UserMapper


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _check_password(raw: str, hashed: str) -> bool:
    return _hash_password(raw) == hashed


def register_user(dto: UserRequestDTO) -> dict:
    if not dto.username:
        raise ValueError("Username is required")
    if not dto.password:
        raise ValueError("Password is required")
    if not dto.name:
        raise ValueError("Name is required")
    if not dto.email:
        raise ValueError("Email is required")
    if not dto.phone:
        raise ValueError("Phone is required")
    if not dto.age:
        raise ValueError("Age is required")
    if not dto.gender:
        raise ValueError("Gender is required")
    if user_repository.exists_by_username(dto.username):
        raise ValueError("Username already exists")
    if user_repository.exists_by_email(dto.email):
        raise ValueError(f"Email '{dto.email}' already exists")
    user = user_repository.save(UserMapper.to_entity(dto))
    return UserMapper.to_response_dto(user).to_dict()


def update_user(user_id: int, dto: UserRequestDTO) -> dict:
    user = user_repository.find_by_id(user_id)
    if not user:
        raise ValueError(f"User with id {user_id} not found")
    data = UserMapper.to_entity(dto)
    user = user_repository.update(user, data)
    return UserMapper.to_response_dto(user).to_dict()


def load_user(username: str, password: str) -> dict:
    user = user_repository.find_by_username(username)
    if not user or not _check_password(password, user.password_hash):
        raise ValueError("Invalid username or password")
    return {"username": user.username, "email": user.email}


def get_user_by_username(username: str) -> dict | None:
    user = user_repository.find_by_username(username)
    if not user:
        return None
    return {"username": user.username, "email": user.email}


def get_all_users() -> list:
    users = user_repository.find_all_objects()
    if not users:
        raise ValueError("No users found")
    return UserMapper.to_response_dto_list(users)


def get_user_by_id(user_id: int) -> dict:
    user = user_repository.find_by_id(user_id)
    if not user:
        raise ValueError(f"User with id {user_id} not found")
    return UserMapper.to_response_dto(user).to_dict()
