import { Construct } from "constructs";
import { Stack, StackProps} from "aws-cdk-lib";
import { Secret } from "aws-cdk-lib/aws-secretsmanager";

const API_KEY = "/service/api-key"
/**
 * 
 */

export class SecretsStack extends Stack {
    readonly apiKey: Secret;

    constructor(scope: Construct, id: string, props: StackProps) {
        super(scope, id, props)

        this.apiKey = Secret.fromSecretNameV2(this, "ApiKeySecret", API_KEY) as Secret;
    }
}