from enum import Enum


class UserRole(Enum):
    GUEST = 0
    PARTICIPANT = 1
    CREATOR = 2
    ADMIN = 3
