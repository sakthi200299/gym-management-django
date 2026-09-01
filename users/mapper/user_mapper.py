from users.dto.user_request_dto import UserRequestDTO
from users.dto.user_response_dto import UserResponseDTO
from users.model.user import User


class UserMapper:
    """
    Equivalent to UserMapper.java (MapStruct) in Spring Boot.
    Converts between User model and DTOs.
    """

    @staticmethod
    def to_entity(dto: UserRequestDTO) -> dict:
        import hashlib
        return {
            "username": dto.username,
            "password_hash": hashlib.sha256(dto.password.encode()).hexdigest(),
            "name": dto.name,
            "email": dto.email,
            "phone": dto.phone,
            "age": dto.age,
            "gender": dto.gender,
        }

    @staticmethod
    def to_response_dto(user: User) -> UserResponseDTO:
        """User model → ResponseDTO (like toResponseDTO() in MapStruct)"""
        return UserResponseDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            age=user.age,
            gender=user.gender,
            joined_date=user.joined_date,
        )

    @staticmethod
    def to_response_dto_list(users: list) -> list:
        """List of User models → List of ResponseDTOs"""
        return [UserMapper.to_response_dto(u).to_dict() for u in users]
