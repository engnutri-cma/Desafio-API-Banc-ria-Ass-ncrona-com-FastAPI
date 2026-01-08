from pydantic import BaseModel, PositiveFloat
from enum import Enum


class AccountIn(BaseModel):
    user_id: int
    balance: PositiveFloat



class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat

    class Config:
        use_enum_values = True