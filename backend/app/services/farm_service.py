from datetime import datetime
from sqlalchemy.orm import Session
from ..models.farm import Farm
from ..models.user import User
from typing import List, Optional
from fastapi import Depends
from ..config.database import get_db

class FarmService:
    @staticmethod
    async def create_farm(farm_data: dict, user: User, db: Session = Depends(get_db)) -> Farm:
        farm = Farm(
            user_id=user.id,
            name=farm_data["name"],
            location=farm_data["location"],
            size_hectares=farm_data["size_hectares"],
            main_crops=farm_data["main_crops"],
            soil_type=farm_data.get("soil_type"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(farm)
        db.commit()
        db.refresh(farm)
        return farm

    @staticmethod
    async def get_farms_by_user(user_id: int, db: Session = Depends(get_db)) -> List[Farm]:
        return db.query(Farm).filter(Farm.user_id == user_id).all()

    @staticmethod
    async def get_farm(farm_id: int, db: Session = Depends(get_db)) -> Optional[Farm]:
        return db.query(Farm).filter(Farm.id == farm_id).first()

    @staticmethod
    async def update_farm(farm_id: int, farm_data: dict, db: Session = Depends(get_db)) -> Optional[Farm]:
        farm = await FarmService.get_farm(farm_id, db)
        if farm:
            for key, value in farm_data.items():
                if hasattr(farm, key):
                    setattr(farm, key, value)
            farm.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(farm)
            return farm
        return None

    @staticmethod
    async def delete_farm(farm_id: int, db: Session = Depends(get_db)) -> bool:
        farm = await FarmService.get_farm(farm_id, db)
        if farm:
            db.delete(farm)
            db.commit()
            return True
        return False 