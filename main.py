from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import models
import database
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/orders/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    try:
        db_order = models.Order(**order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    except IntegrityError:
        db.rollback()  # Rollback the transaction if duplicate or constraint violation
        raise HTTPException(status_code=400, detail="Duplicate order detected.")
