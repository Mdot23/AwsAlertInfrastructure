import { LambdaFunction } from "aws-cdk-lib/aws-events-targets";
import { Construct } from "constructs";
import { Function } from "aws-cdk-lib/aws-lambda";
import * as cdk from "aws-cdk-lib";

interface EventRuleStackProps extends cdk.StackProps {
    lambdaArn: string;
}