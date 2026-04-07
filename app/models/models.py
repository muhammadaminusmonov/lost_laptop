from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
import uuid
from app.core.database import Base
from app.models.user import User


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at =Column(DateTime(timezone=True), onupdate=func.now())
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True)

    def __repr__(self):
        return f'<Category(id={self.id}, name={self.name})>'

class UniqueNumberCategory(Base):
    __tablename__ = 'unique_number_category'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True)


class UniqueNumber(Base):
    __tablename__ = 'unique_number'
    id = Column(Integer, primary_key=True, index=True)
    unique_number_category = Column(Integer, ForeignKey('unique_number_category.id'), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True)




class LostDevice(Base):
    __tablename__ = 'lost_device'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey('device.id'), nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True)



class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(Integer, ForeignKey('category.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String, nullable=True)
    status = Column(Boolean)
    uid = Column(Integer, ForeignKey('unique_number_category.id'), nullable=False)

