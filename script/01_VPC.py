import boto3
from region import region
templates_path = '../01_VPC.yaml'
client = boto3.client('cloudformation', region_name=region)

response = client.create_stack(
    StackName='v2rayVPC',
    TemplateBody=open(templates_path, encoding='utf-8').read(),
    Tags=[
        {
            "Key": "Name",
            "Value": 'v2rayEC2'
        },
    ],
)
