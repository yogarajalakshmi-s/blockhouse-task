from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field, constr

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    order_type = Column(String(10), nullable=False)

class OrderCreate(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=10, description="Stock symbol")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    quantity: int = Field(..., gt=0, description="Quantity must be a positive integer")
    order_type: constr(pattern="^(buy|sell)$") = Field(..., description="Order type must be 'buy' or 'sell'")
