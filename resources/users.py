# TODO UserList with post method to create new user

from flask import Blueprint
from flask_restful import Resource, reqparse, Api, fields, marshal

import models

user_fields = {
    'username': fields.String,
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No Password provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'verify_password',
            required=True,
            help='No Password verification provided',
            location=['form', 'json']
        )
        super().__init__()

    def post(self):
        args = self.reqparse.parse_args()
        if args.get('password') == args.get('verify_password'):
            try:
                user = models.User.create_user(**args)
            except Exception as error:
                return {'error': str(error)}, 400
            else:
                return marshal(user, user_fields), 201
        return {'error': 'Password and password verification do not match'}, 400


user_api = Blueprint('resources.user', __name__)
api = Api(user_api)
api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)
