import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'Planeta' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Personaje(Base):
    __tablename__ = 'Personaje'
    uid = Column(Integer, primary_key=True)
    name = Column(String(30), nullable = False)
    homeworld = Column(String(50), ForeignKey('Planeta.nombre'))
   
    relacionpersonaje = relationship("Personaje")

class Vehicle(Base):
    __tablename__ = 'Vehicle' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    manufactura = Column(String(50), ForeignKey('Planeta.nombre'))
   
    relacionvehicle = relationship("Vehicle")

class ListaFavoritos(Base):
    __tablename__ = 'ListaFavoritos' 
    id = Column(Integer, primary_key=True)
    favoritoPersonaje = Column(String(50), nullable=False)
    mail= Column(String(50),  ForeignKey('Usuario.mail'))
    favoritoPlaneta = Column(String(50),  ForeignKey('Planeta.nombre'))
    favoritoVehicle = Column(String(50),  ForeignKey('Vehicle.nombre'))
   
    relacionvehicle = relationship("Vehicle")
    
class Usuario(Base):
    __tablename__ = 'Usuario' 
    mail = Column(String(50), primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(250), nullable=False)
   
    relacionusuario = relationship("Usuario")



   
  



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')