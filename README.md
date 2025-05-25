# Phase 3 Mock Code Challenge: Freebie Tracker

## Learning Goals

- Write SQLAlchemy migrations.
- Connect between tables using SQLAlchemy relationships.
- Use SQLAlchemy to run CRUD statements in the database.

***

## Key Vocab

- **Schema**: the blueprint of a database. Describes how data relates to other
  data in tables, columns, and relationships between them.
- **Persist**: save a schema in a database.
- **Engine**: a Python object that translates SQL to Python and vice-versa.
- **Session**: a Python object that uses an engine to allow us to
  programmatically interact with a database.
- **Transaction**: a strategy for executing database statements such that
  the group succeeds or fails as a unit.
- **Migration**: the process of moving data from one or more databases to one
  or more target databases.
  
***

## Introduction

For this assignment, we'll be working with a freebie domain.

As developers, when you attend hackathons, you'll realize they hand out a lot of
free items (informally called _freebies_, or swag)! Let's make an app for
developers that keeps track of all the freebies they obtain.

We have three models: `Company`, `Dev`, and `Freebie`

For our purposes, a `Company` has many `Freebie`s, a `Dev` has many `Freebie`s,
and a `Freebie` belongs to a `Dev` and to a `Company`.

`Company` - `Dev` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Instructions

To get started, run `pipenv install && pipenv shell` while inside of this
directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This mock code challenge does not have tests. You cannot run
`pytest` and you cannot run `learn test`. You'll need to create your own sample
instances so that you can try out your code on your own. Make sure your
relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start an `ipdb` session
with your classes defined. You can test out the methods that you write here. You
are also encouraged to use the `seed.py` file to create sample data to test your
models and associations.

Writing error-free code is more important than completing all of the
deliverables listed- prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

***

## What You Already Have

The starter code has migrations and models for the initial `Company` and `Dev`
models, and seed data for some `Company`s and `Dev`s. The schema currently looks
like this:

### companies Table

| Column        | Type    |
| ------------- | ------- |
| name          | String  |
| founding_year | Integer |

### devs Table

| Column | Type   |
| ------ | ------ |
| name   | String |

You will need to create the migration for the `freebies` table using the
attributes specified in the deliverables below.

***

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

Remember: SQLAlchemy gives your classes access to a lot of methods already!
Keep in mind what methods SQLAlchemy gives you access to on each of your
classes when you're approaching the deliverables below.

### Migrations

Before working on the rest of the deliverables, you will need to create a
migration for the `freebies` table.

- A `Freebie` belongs to a `Dev`, and a `Freebie` also belongs to a `Company`.
  In your migration, create any columns your `freebies` table will need to
  establish these relationships using the right foreign keys.
- The `freebies` table should also have:
  - An `item_name` column that stores a string.
  - A `value` column that stores an integer.

After creating the `freebies` table using a migration, use the `seed.py` file to
create instances of your `Freebie` class so you can test your code.

**After you've set up your `freebies` table**, work on building out the following
deliverables.

### Relationship Attributes and Methods

Use SQLAlchemy's `ForeignKey`, `relationship()`, and `backref()` objects to
build relationships between your three models.

**Note**: The plural of "freebie" is "freebies" and the singular of "freebies"
is "freebie".

#### Freebie

- `Freebie.dev` returns the `Dev` instance for this Freebie.
- `Freebie.company` returns the `Company` instance for this Freebie.

#### Company

- `Company.freebies` returns a collection of all the freebies for the Company.
- `Company.devs` returns a collection of all the devs who collected freebies
  from the company.

#### Dev

- `Dev.freebies` returns a collection of all the freebies that the Dev has collected.
- `Dev.companies`returns a collection of all the companies that the Dev has collected
  freebies from.

Use `python debug.py` and check that these methods work before proceeding. For
example, you should be able to retrieve a dev from the database by its
attributes and view their companies with `dev.companies` (based on your seed
data).

### Aggregate Methods

#### Freebie

- `Freebie.print_details()`should return a string formatted as follows:
  `{dev name} owns a {freebie item_name} from {company name}`.

#### Company

- `Company.give_freebie(dev, item_name, value)` takes a `dev` (an instance of
  the `Dev` class), an `item_name` (string), and a `value` as arguments, and
  creates a new `Freebie` instance associated with this company and the given
  dev.
- Class method `Company.oldest_company()`returns the `Company` instance with
  the earliest founding year.

#### Dev

- `Dev.received_one(item_name)` accepts an `item_name` (string) and returns
  `True` if any of the freebies associated with the dev has that `item_name`,
  otherwise returns `False`.
- `Dev.give_away(dev, freebie)` accepts a `Dev` instance and a `Freebie`
  instance, changes the freebie's dev to be the given dev; your code should only
  make the change if the freebie belongs to the dev who's giving it away



Freebie Tracker
This is a Python-based application built using Flask and SQLAlchemy to track freebies given by companies to developers. The application uses object-oriented principles to define models for Company, Dev (developer), and Freebie (item received by a developer).

Features
A company can give freebies to developers.

A developer can receive and give away freebies.

Each freebie links a developer and a company.

The system allows for tracking which freebies a developer has received from which company.

Table of Contents
Installation

Usage

Models

Company Model

Dev Model

Freebie Model

Methods

Company Methods

Dev Methods

Freebie Methods

Database Setup

Testing

Installation
Follow the steps below to set up the application on your local machine.

Prerequisites
Python 3.x

Flask

SQLAlchemy

Flask-Migrate

Steps to Install
Clone the repository:

bash
Copy code
git clone https://github.com/your-repository/freebie-tracker.git
Navigate into the project folder:

bash
Copy code
cd freebie-tracker
Create a virtual environment:

bash
Copy code
python3 -m venv .venv
Activate the virtual environment:

On macOS/Linux:

bash
Copy code
source .venv/bin/activate
On Windows:

bash
Copy code
.venv\Scripts\activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
To run the application:

Set the environment variable:

bash
Copy code
export FLASK_APP=app.py
export FLASK_ENV=development
Run the application:

bash
Copy code
flask run
The application should now be running on http://127.0.0.1:5000/.

Models
Company Model
This model represents a company in the system and tracks the freebies it gives out.

python
Copy code
class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer, nullable=False)

    freebies = relationship('Freebie', backref='company')  # One-to-many with Freebie
    devs = relationship('Dev', secondary='freebies', backref='companies')  # Many-to-many with Dev
Attributes:

id: Unique identifier for the company.

name: Name of the company.

founding_year: Year the company was founded.

Relationships:

One-to-many relationship with Freebie.

Many-to-many relationship with Dev through Freebie.

Dev Model
This model represents a developer who collects freebies from companies.

python
Copy code
class Dev(db.Model):
    __tablename__ = 'devs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    freebies = relationship('Freebie', backref='dev')  # One-to-many with Freebie
    companies = relationship('Company', secondary='freebies', backref='devs')  # Many-to-many with Company
Attributes:

id: Unique identifier for the developer.

name: Name of the developer.

Relationships:

One-to-many relationship with Freebie.

Many-to-many relationship with Company through Freebie.

Freebie Model
This model represents a freebie given by a company to a developer.

python
Copy code
class Freebie(db.Model):
    __tablename__ = 'freebies'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    dev_id = db.Column(db.Integer, ForeignKey('devs.id'), nullable=False)
    company_id = db.Column(db.Integer, ForeignKey('companies.id'), nullable=False)

    dev = relationship('Dev', backref='freebies')
    company = relationship('Company', backref='freebies')
Attributes:

id: Unique identifier for the freebie.

item_name: Name of the freebie.

value: Value of the freebie.

dev_id: Foreign key to the devs table.

company_id: Foreign key to the companies table.

Relationships:

One-to-one relationship with Dev and Company.

Methods
Company Methods
give_freebie(dev, item_name, value): This method creates a new Freebie and associates it with a developer and company.

oldest_company(): This class method returns the company with the earliest founding year.

Dev Methods
received_one(item_name): This method checks if a developer has received a freebie with a given item name.

give_away(dev, freebie): This method allows a developer to transfer a freebie to another developer.

Freebie Methods
print_details(): This method returns a string formatted as:

css
Copy code
"{dev name} owns a {freebie item_name} from {company name}"
Database Setup
Migrations
Initialize Migration Folder:

bash
Copy code
flask db init
Generate Migrations:

bash
Copy code
flask db migrate -m "Added Freebie table and relationships"
Apply Migrations:

bash
Copy code
flask db upgrade
Seed Data:
Run seed.py to add initial Company, Dev, and Freebie data for testing.

Testing
Testing the Relationships:
Use python debug.py to verify relationships between Dev, Company, and Freebie.

Example to test if a developer has received a freebie:

python
Copy code
dev = Dev.query.filter_by(name="Alice").first()
print(dev.freebies)  # Check the freebies the dev has received
Test Methods:

Ensure that methods like give_freebie, received_one, and give_away work as expected by calling them in debug.py or during test execution.

Contributing
Feel free to fork the repository and submit pull requests. Any issues or improvements can be reported in the issues section.

License
This project is licensed under the MIT License - see the LICENSE file for details.

