from flask import Flask
from flask_restful import Api, Resource, reqparse
from S3Module.ApiReceiver import ApiReceiver
from S3Module.Command import *


import os
import logging
from os.path import dirname, realpath, join
current_path = realpath(dirname(__file__))
logfile_name = "{}\\apiLog.log".format(current_path)


app = Flask(__name__)
api = Api(app)

class Invoker(Resource):
    def __init__(self):
        pass

    def get(self, s3object):
        """
        Get method o f rest api
        :param s3object:
        :return:
        """
        logging.debug('Inititaing get command...')
        if s3object == 'list_objects':
            logging.debug('Fetching all objects')
            s3_command = GetS3ObjectList(s3object)
        else:
            logging.debug('Fetching detaisl of particular objects')
            s3_command = GetS3Object(s3object)

        return s3_command.execute()

    def put(self, object):
        """
        Put method of REST API
        :param object:
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument("action")

        args = parser.parse_args()
        if args['action'] == 'delete':
            pass
        else:
            return object,404

    def delete(self, s3object):
        """Delete method of rest api"""
        logging.debug('Initiating delete of particular object')
        s3_command = DeleteS3Object(s3object)
        return s3_command.execute()






api.add_resource(Invoker, "/s3object/<string:s3object>")

app.run(debug=True)