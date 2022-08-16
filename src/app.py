"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

members = jackson_family.get_all_members()
response_body = {
    "hello": "world",
    "family": members
}


return jsonify(response_body),200


@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Todos
@app.route('members', method =['GET'])
def handle_hello():

    menbers = jackson_family.get_all_members()
    response_body = {
        "hello": "Hola",
        "family": members
    }    

    return jsonify(response_body), 200

    #solo uno
    @app.routes('member/<int:member_id', method = ['GET, DELETE'])
    def one_nember(nember_id):
       # member = jackson_family.query(member_id)
       #  return jsonify(menber), 200
       if request.method == "DELETE":
        jackson_family.delete_member(member_id)


    @app.route('/member', method = ['POST'])
    def add_member():
        print(request.json)
        menber={
            "id": jackson_family._generateId(),
            "age": request.json.get("age"),
            "first_name": request.json.get("first_name"),
           "last_name": request.json.get("last_name"),
            "lucky_numbers": request.json.get("lucky_numbers")     
        }    

        jackson_family.add_member(member)
        return "se agrega un miembro"