from fastapi import APIRouter, Depends, status
from schemas import AccountIn
from security import login_required
from services import AccountService
from services import TransactionService
from views import AccountOut, TransactionOut

from src.schemas.transaction import TransactionIn
from src.services.transaction import TransactionService



router = APIRouter(prefix="/accounts", dependencies=[Depends(login_required)])

account_service = AccountService()
tx_service = TransactionService()


@router.get("/", response_model=list[AccountOut])
async def read_accounts(limit: int, skip: int = 0):
    return await account_service.read_all(limit=limit, skip=skip)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(account: AccountIn):
    return await account_service.create(account)


@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0):
    return await tx_service.read_all(account_id=id, limit=limit, skip=skip)


router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    return await service.create(transaction)