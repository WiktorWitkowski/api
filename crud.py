from typing import Annotated

from fastapi import APIRouter, status, Query
from sqlmodel import select

from deps import SessionDep
from models import Subscription

router = APIRouter()


@router.post("/subscription", status_code=status.HTTP_201_CREATED)
def create_subscription(sub: Subscription, session: SessionDep) -> Subscription:
    session.add(sub)
    session.commit()
    session.refresh(sub)
    return sub


@router.get("/subscriptions")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Subscription]:
    query = select(Subscription).offset(offset).limit(limit)
    subs = session.exec(query).all()
    return subs
