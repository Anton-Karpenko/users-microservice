from enum import Enum


class RoleEnum(str, Enum):
    agent = 'agent'


class StatusEnum(str, Enum):
    in_progress = 'in_progress'
    active = 'active'
