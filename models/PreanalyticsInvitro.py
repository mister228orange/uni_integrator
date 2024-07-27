import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, JSON, Enum, Index, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()


class StatusEnum(enum.Enum):
    COMPLETE = "complete"
    AWAIT = "await"
    SENDED = "sended"


class PreanalyticsInvitro(Base):
    __tablename__ = "preanalytics_invitro"

    order_id = Column(String, index=True, nullable=False)
    preanalytic_id = Column(String, primary_key=True, index=True, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.AWAIT, nullable=False, index=True)
    result = Column(Text)
    attach = Column(JSONB)
    created_at = Column(TIMESTAMP, default=datetime.UTC, nullable=False, index=True, )

    __table_args__ = (
        Index("fast search incomplete", "status"),
        Index("fast search by daterange", "created_at", postgresql_using="brin")
    )
    expire_on_commit = False
