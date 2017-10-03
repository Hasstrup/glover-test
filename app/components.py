from app import app
from app import db
from .models import Component

Venue = Component(
        name= 'Venue',
        vendors= [],
        Max_price= [],
        Min_Price= []
        )

Sound = Component(
        name= 'Sound',
        vendors= [],
        Max_price= [],
        Min_Price= []
        )

Food = Component(
        name= 'Food',
        vendors= [],
        Max_price= [],
        Min_Price= []
        )

db.session.add(Food, Sound, Venue)
db.session.commit()
