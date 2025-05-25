from app import db
from models import Company, Dev

def seed_data():
 
    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")

    company1 = Company(name="TechCorp", founding_year=2000)
    company2 = Company(name="DevWorks", founding_year=2010)

    db.session.add(dev1)
    db.session.add(dev2)
    db.session.add(company1)
    db.session.add(company2)
    db.session.commit()


    company1.give_freebie(dev1, "Laptop", 1500)
    company2.give_freebie(dev2, "Tablet", 800)
    company2.give_freebie(dev1, "Smartwatch", 300)

    db.session.commit()

if __name__ == "__main__":
    seed_data()
