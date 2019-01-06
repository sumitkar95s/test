import boto3

class BotoConnections:
    """
    Class which act as an interface to AWS
    """
    s3_client = boto3.client('s3')


class S3Actions(BotoConnections):
    def __init__(self):
        pass


    def list_objects_in_buckets(self,bucket_name):
        response = self.s3_client.list_objects(
            Bucket=bucket_name,
        )

        object_details_list = list()

        for object in response['Contents']:
            object_details_list.append({'Key':object['Key'],'Size':object['Size']})
        return object_details_list


    def get_object_details(self,bucket_name,object_name):
        response = self.s3_client.get_object(
            Bucket = bucket_name,
            Key = object_name,
        )
        return response


    def delete_s3_object(self,bucket_name,object_name):
        response = self.s3_client.delete_object(
            Bucket=bucket_name,
            Key=object_name

        )
        return response