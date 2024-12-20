from pydantic import BaseModel

class Config(BaseModel):
    group_blacklist: list = []
    group_whitelist: list = []