from enum import Enum

import uuid
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class SubTypes(str, Enum):
    BASIC = "Basic"
    PRO = "Pro"
    ULTRA = "Ultra"


class Subscription(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    type: SubTypes
    price: float


class Customer(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr
    full_name: str| None = None
    nick_name: str | None = None
    phone: str | None = None
    subscription: uuid.UUID | None = Field(default=None, foreign_key="subscription.id")

