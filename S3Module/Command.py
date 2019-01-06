from S3Module.ApiReceiver import ApiReceiver

import logging

api_logger =logging.getLogger(__name__)


class Command():
    """
    All commands from the rest api are encapsulated as an object and sent to
    receiver.
    """
    api_receiver = ApiReceiver()

class GetS3Object(Command):
    """
    Returns details of the S3 Object
    """
    def __init__(self,s3object_name):
        api_logger.debug('Gets3object constructor')
        self.s3object = s3object_name

    def execute(self):
        return self.api_receiver._get_filtered_s3_object(self.s3object)


class GetS3ObjectList(Command):
    """
    Returns all objects in the S3 bucket
    """
    def __init__(self):
        api_logger.debug('GetS3objectlist constructor')

    def execute(self):
        return self.api_receiver._get_s3_objects()


class DeleteS3Object(Command):
    """
    Delete the s3 object if present
    """
    def __init__(self,s3object_name):
        api_logger.debug('Deletes3object constructor')
        self.s3object = s3object_name

    def execute(self):
        return self.api_receiver._remove_s3_object(self.s3object)



class UploadS3Object(Command):
    pass


