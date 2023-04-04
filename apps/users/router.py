from fastapi import APIRouter

from config.constants import TAG_USERS

router = APIRouter(tags=[TAG_USERS])
