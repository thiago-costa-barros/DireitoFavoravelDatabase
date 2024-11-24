# app/models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class ExternalWebhookHotmartReceiver(Base):
    __tablename__ = 'ExternalWebhookHotmartReceiver'
    __table_args__ = {'schema': 'df_externalsystem'}

    Id = Column(Integer, primary_key=True, index=True)
    CreationDate = Column(DateTime, default=func.now())
    UpdateDate = Column(DateTime, default=func.now(), onupdate=func.now())
    DeletionDate = Column(DateTime, nullable=True)
    RequestId = Column(String, unique=True, index=True)
    EventDate = Column(DateTime)
    EventName = Column(String)
    Version = Column(String)
    Payload = Column(JSON)

    HotmartOrderNotes = relationship('HotmartOrderNote', back_populates='ExternalWebhookHotmartReceiver')


class HotmartOrderNote(Base):
    __tablename__ = 'HotmartOrderNote'
    __table_args__ = {'schema': 'df_servicesystem'}

    Id = Column(Integer, primary_key=True, index=True)
    CreationDate = Column(DateTime, default=func.now())
    UpdateDate = Column(DateTime, default=func.now(), onupdate=func.now())
    DeletionDate = Column(DateTime, nullable=True)
    ExternalWebhookHotmartReceiverId = Column(Integer, ForeignKey('df_externalsystem.ExternalWebhookHotmartReceiver.Id'))
    HotmartProductId = Column(Integer, ForeignKey('df_servicesystem.HotmartProduct.Id'))
    HotmartBuyerId = Column(Integer, ForeignKey('df_servicesystem.HotmartBuyer.Id'))
    HotmartPurchaseId = Column(Integer, ForeignKey('df_servicesystem.HotmartPurchase.Id'))
    HotmartSubscriptionId = Column(Integer, ForeignKey('df_servicesystem.HotmartSubscription.Id'))

    ExternalWebhookHotmartReceiver = relationship('ExternalWebhookHotmartReceiver', back_populates='HotmartOrderNotes')
    HotmartProduct = relationship('HotmartProduct', back_populates='HotmartOrderNotes')
    HotmartBuyer = relationship('HotmartBuyer', back_populates='HotmartOrderNotes')
    HotmartPurchase = relationship('HotmartPurchase', back_populates='HotmartOrderNotes')
    HotmartSubscription = relationship('HotmartSubscription', back_populates='HotmartOrderNotes')
