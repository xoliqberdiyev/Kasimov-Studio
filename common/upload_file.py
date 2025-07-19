import boto3, requests
from django.conf import settings


def upload_file(file, instance):

    s3 = boto3.client(
        "s3",
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        region_name=settings.AWS_S3_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    key = f"uploads/{file.name}"

    presigned = s3.generate_presigned_post(
        Bucket=settings.AWS_STORAGE_BUCKET_NAME,
        Key=key,
        Fields={"Content-Type": file.content_type},
        Conditions=[["eq", "$Content-Type", file.content_type]],
        ExpiresIn=3600,
    )

    # Faylni S3-compatible storage'ga yuklash
    files = {"file": (file.name, file.read(), file.content_type)}
    response = requests.post(presigned["url"], data=presigned["fields"], files=files)

    if response.status_code != 204:
        raise Exception(f"Upload failed: {response.text}")

    instance.file_url = f"{settings.AWS_S3_ENDPOINT_URL}/{key}"

    if commit:
        instance.save()
    return instance