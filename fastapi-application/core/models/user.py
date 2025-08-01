from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

class User(IntIdPkMixin, Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(unique=True)
