from app import app, db
from models import Dev, Company, Freebie

with app.app_context():

    dev = Dev.query.filter_by(name="Alice").first()
    print(dev.freebies)
    print(dev.companies)  

    company = Company.query.filter_by(name="TechCorp").first()
    company.give_freebie(dev, "Headphones", 100)
    print(dev.freebies)  


    freebie = Freebie.query.first()
    print(freebie.print_details())  
