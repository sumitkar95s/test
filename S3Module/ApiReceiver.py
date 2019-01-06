from Utilities.BotoConnections import *
import logging

api_logger =logging.getLogger(__name__)



class ApiReceiver:
    """
    Back end logic for each actions
    """
    def __init__(self):
        self.bucket_name = 'xyz'

    def _get_filtered_s3_object(self,s3_object_name):
        """
        Action to return the details of object
        :param s3_object_name:
        :return:
        """
        try:
            s3_actions = S3Actions()
            s3_object_details = s3_actions.get_object_details(self.bucket_name,s3_object_name)
            if not s3_object_details:
                api_logger.debug('Returning details of s3object in get filtered object')
                return "Object not found",404
            else:
                return s3_object_details,200
        except Exception,e:
            logging.error(e.message)
            return 'Exception Occured',400


    def _get_s3_objects(self):
        """
        Actions for returning all the s3 objects in buckets
        :return:
        """
        try:
            s3_actions = S3Actions()
            object_details_list = s3_actions.list_objects_in_buckets(self.bucket_name)
            if not object_details_list:
                return 'Objects not found',404
            else:
                return object_details_list,200
        except Exception,e:
            logging.error(e.message)
            return 'Exception Occured',400

    def remove_s3_object(self,object_name):
        """
        Returns delete status of an object as api response
        :param object_name:
        :return:
        """
        try:
            s3_actions = S3Actions()
            s3_delete_response = s3_actions.delete_s3_object(self.bucket_name,object_name)
            if not s3_delete_response:
                return "Object not found",404
            else:
                return s3_delete_response,200
        except Exception,e:
            logging.error(e.message)
            return 'Exception Occured',400