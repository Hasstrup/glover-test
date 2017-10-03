from app import app
from app import db
# user_event = db.Table('user_event',
#                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#                       db.Column('event_id', db.Integer, db.ForeignKey('event.id')))
event_vendors = db.Table('event_vendor',
                           db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
                           db.Column('vendor_id', db.Integer, db.ForeignKey('vendor.id')),
                           db.PrimaryKeyConstraint('event_id', 'vendor_id'))
# component_vendor = db.table('event_component',
#                             db.Column('component_id', db.Integer, db.ForeignKey('component.id')),
#                             db.Column('vendor_id', db.Integer, db.ForeignKey('vendor.id ')))
class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    events = db.relationship('Event', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' %(self.username)

class Event(db.Model):
    __tablename__ = 'Event'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vendors = db.relationship('Vendor', secondary=event_vendors,
                                 primaryjoin=(event_vendors.c.event_id == id),
                                 secondaryjoin=(event_vendors.c.vendor_id == 'vendor.id'),
                                 backref='events')

    def __repr__(self):
        return '<Event %r>' %(self.name)

class Component(db.Model):
    __tablename__ = 'Component'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    vendors = db.relationship('Vendor', backref='component', lazy='dynamic' )
    Max_price = db.Column(db.Integer)
    Min_price = db.Column(db.Integer)

    def __repr__(self):
        return '<Component %s>' %(self.name)

class Vendor(db.Model):
    __tablename__ = 'Vendor'

    id = db.Column(db.Integer, primary_key=True)
    vendorname = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120))
    component_id = db.Column(db.Integer, db.ForeignKey('component.id'))
    events = db.relationship('Event', secondary=event_vendors,
                             primaryjoin=(event_vendors.c.event_id == 'event.id'),
                             secondaryjoin=(event_vendors.c.vendor_id == id),
                             backref='vendors')

    def __repr__(self):
        return (self.vendorname)
