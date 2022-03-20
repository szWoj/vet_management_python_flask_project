from flask import Flask, render_template, request, redirect, Blueprint
from repositories import vet_repository, animal_repository
from models.vet import Vet
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route('/animals')
def animals_menu():
    return render_template('animals/index.html')

@animals_blueprint.route('/animals/animals_all')
def animals_all():
    animals = animal_repository.select_all()
    return render_template('animals/all_animals.html', animals=animals)