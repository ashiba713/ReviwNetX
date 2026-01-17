from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    product = Column(String)
    rating = Column(Integer)
    text = Column(String)
    timestamp = Column(String)
    risk_score = Column(Float, default=0.0)
    flag_reason = Column(String, default="")
