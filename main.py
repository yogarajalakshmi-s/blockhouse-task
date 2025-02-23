from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import models, database, schemas, crud
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/orders/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    try:
        db_order = crud.create_order(db=db, order=order)
        return db_order
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")

@app.get("/orders/", response_model=List[schemas.OrderResponse])
def get_orders(db: Session = Depends(database.get_db)):
    orders = db.query(models.Order).all()
    return orders