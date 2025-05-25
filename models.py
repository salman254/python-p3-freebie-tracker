from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer, nullable=False)

   
    freebies = relationship('Freebie', backref='company')

   
    devs = relationship('Dev', secondary='freebies', backref='companies')

    @classmethod
    def oldest_company(cls):
        return cls.query.order_by(cls.founding_year).first()

    def give_freebie(self, dev, item_name, value):
       
        freebie = Freebie(dev_id=dev.id, company_id=self.id, item_name=item_name, value=value)
        db.session.add(freebie)
        db.session.commit()


class Dev(db.Model):
    __tablename__ = 'devs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    
    freebies = relationship('Freebie', backref='dev')

   
    companies = relationship('Company', secondary='freebies', backref='devs')

    def received_one(self, item_name):
       
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        
        if freebie.dev_id == self.id:
            freebie.dev_id = dev.id
            db.session.commit()


class Freebie(db.Model):
    __tablename__ = 'freebies'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    dev_id = db.Column(db.Integer, ForeignKey('devs.id'), nullable=False)
    company_id = db.Column(db.Integer, ForeignKey('companies.id'), nullable=False)


    dev = relationship('Dev', backref='freebies')
    company = relationship('Company', backref='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
