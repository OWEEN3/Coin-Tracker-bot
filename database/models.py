from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, BigInteger

from database.database import Base

IntPK = Annotated[int, mapped_column(Integer, primary_key=True, nullable=False)]

class Users(Base):
    __tablename__ = "users"

    id: Mapped[IntPK]
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    notification_status: Mapped[str] = mapped_column(String)
    notification_type: Mapped[str] = mapped_column(String)
    notification_interval: Mapped[int] = mapped_column(Integer)

class Tracking(Base):
    __tablename__ = "tracking"

    id: Mapped[IntPK]
    user_chat_id: Mapped[int] = mapped_column(ForeignKey("users.chat_id", ondelete="CASCADE"), nullable=False)
    symbol: Mapped[str] = mapped_column(String, nullable=False)