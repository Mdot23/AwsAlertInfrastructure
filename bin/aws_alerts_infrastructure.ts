#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AwsAlertsInfrastructureStack } from '../lib/aws_alerts_infrastructure-stack';

const app = new cdk.App();
new AwsAlertsInfrastructureStack(app, 'AwsAlertsInfrastructureStack');
