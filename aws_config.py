class AWSConfig:

    # Simulated AWS credentials 
    AWS_ACCESS_KEY_ID = "Pdw1OcdQk034jI9eEQHRYymut26VRmtdNmVB-PwsFt4TYTf2dBHM0BhR_AYDP00FDy-UKJhD-KT3BlbkFJziAcpMf-rz4-bLWdMxICccdh_vjCrlx1BvUe95GvwthzvfpAWaXYEeXfr_Lnq8JwkrmR7TtFkA"
    AWS_SECRET_ACCESS_KEY = "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"
    AWS_REGION = "us-east-1"


def connect_to_aws():
    print("DLP TEST: Using fake AWS credentials only.")
    print("Access Key:", AWSConfig.AWS_ACCESS_KEY_ID)
    return True


if __name__ == "__main__":
    connect_to_aws()