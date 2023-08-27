import boto3
import zipfile
from io import BytesIO


def list_files_in_bucket_folder(bucket_name, folder):
    """Returns a list with the files stored on the specified AWS S3 bucket.

    :param bucket_name: Bucket mane
    :param folder: Folder name inside the specified bucket
    :return: List object containing all files inside folder
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    files = list(map(lambda f: f.key, bucket.objects.filter(Prefix=(folder + '/'))))
    return files


def unzip_from_s3(bucket_name, s3_file_key, destination):
    """Unzips the file contents into destnation folder.

    Unzip the contents of the file stored into the specified bucket on the fly (without downloading it first.

    :param bucket_name: Bucket name
    :param s3_file_key: File identifier inside the bucket
    :param destination: Local folder where the contents of the file are going to be unzipped
    """
    s3 = boto3.resource('s3')
    zip_obj = s3.Object(bucket_name=bucket_name, key=s3_file_key)
    buffer = BytesIO(zip_obj.get()["Body"].read())
    z = zipfile.ZipFile(buffer)
    z.extractall(destination)
