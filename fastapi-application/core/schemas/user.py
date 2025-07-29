from pydantic import BaseModel
from pydantic import ConfigDict

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)  # если че то это чтение с атрибутов и так используется по-умолчанию в pydantic v2+.
    id: int
