from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda_python_alpha as _lambda
from aws_cdk.aws_lambda import Runtime
from constructs import Construct


class CdkFastapiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        api_lambda = _lambda.PythonFunction(
            self, 
            'FastApiHandler',
            entry="lambda/api",
            runtime=Runtime.PYTHON_3_9,
            index="main.py",
            handler='handler',
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=api_lambda,
        )