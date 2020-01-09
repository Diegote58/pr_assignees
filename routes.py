from flask import render_template, flash, redirect, url_for
import json
from flask_restful import Resource
from service import userService

class Quotes(Resource):
    def get(self):
        return render_template('index.html', title='Q')
