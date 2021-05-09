# Script to download the private ssh key of code commit
import argparse
import boto3

if __name__ == '__main__':

    # Get AWS IAM Credentials as Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--access-key', required=True, type=str, help='Access Key of IAM User')
    parser.add_argument('--secret-key', required=True, type=str, help='Secret Key of IAM User')
    args = parser.parse_args()

    # Create boto3 session
    session = boto3.Session(
        aws_access_key_id=args.access_key,
        aws_secret_access_key=args.secret_key
    )
    # Create aws clients
    s3 = session.client('s3')

    # Download ssh credentials for git
    s3.download_file('cellstrat2', 'CellStratHub-private/cs_commit', 'cs_commit')
    s3.download_file('cellstrat2', 'CellStratHub-private/config', 'config')
