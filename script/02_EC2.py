import boto3
from region import region
templates_path = '../02_EC2.yaml'
client = boto3.client('cloudformation', region_name=region)

response = client.create_stack(
    StackName='v2rayEC2',
    TemplateBody=open(templates_path, encoding='utf-8').read(),
    Parameters=[{'ParameterKey': "KeyPair", 'ParameterValue': 'us-east-1-key'},
                {'ParameterKey': "EnvType", 'ParameterValue': 'dev'},
                {'ParameterKey': "VPCStackName", 'ParameterValue': 'v2rayVPC'},
                ],
    Tags=[
        {
            "Key": "Name",
            "Value": 'v2rayEC2'
        },
        ],
    Capabilities=['CAPABILITY_IAM'],
)
