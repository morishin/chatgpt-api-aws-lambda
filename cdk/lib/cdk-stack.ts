import { Stack, type StackProps } from "aws-cdk-lib";
import {
  FunctionUrlAuthType,
  DockerImageFunction,
  DockerImageCode,
} from "aws-cdk-lib/aws-lambda";
import { Repository } from "aws-cdk-lib/aws-ecr";
import { Construct } from "constructs";

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const ecrRepo = Repository.fromRepositoryName(
      this,
      "EcrRepository",
      process.env.ECR_REPO ?? ""
    );

    const chatBotFunction = new DockerImageFunction(this, "ChatBotFunction", {
      functionName: "ChatBotFunction",
      code: DockerImageCode.fromEcr(ecrRepo, {
        tagOrDigest: process.env.ECR_TAG,
      }),
      environment: {
        OPENAI_API_KEY: process.env.OPENAI_API_KEY ?? "",
      },
    });

    chatBotFunction.addFunctionUrl({
      authType: FunctionUrlAuthType.NONE,
    });
  }
}
