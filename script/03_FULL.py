import boto3
from region import region
templates_path = '../03_FULL.yaml'
client = boto3.client('cloudformation', region_name=region)

response = client.create_stack(
    StackName='v2rayFULL',
    TemplateBody=open(templates_path, encoding='utf-8').read(),
    Parameters=[{'ParameterKey': "KeyPair", 'ParameterValue': 'us-east-1-key'},
                {'ParameterKey': "EnvType", 'ParameterValue': 'dev'},
                ],
    Tags=[
        {
            "Key": "Name",
            "Value": 'v2rayFULL_Stack'
        },
        ],
    Capabilities=['CAPABILITY_IAM'],
)
