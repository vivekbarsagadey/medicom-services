from werkzeug.utils import secure_filename
from flask_restful import Resource, reqparse
from flask import request, render_template
import os

class UserFileuploadscontroller(Resource):
    def get(self):
        return ""

    def post(self):
        print("UserFileuploadscontroller post called")
        f = request.files["file"]
        print("file name is ",f.filename)
        #f.save(secure_filename(f.filename))
        return f.filename