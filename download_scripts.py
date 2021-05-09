# Script to download the private ssh key of code commit
import argparse
import boto3

def download_git_file(file: str, commit_id: str, repo: str = 'CSHub-Scripts') -> None:
    '''Downloads a specific file from a codecommit git repository'''

    # Get file as byte string
    response = codecommit.get_file(
        repositoryName=repo,
        filePath=file,
        commitSpecifier=commit_id
    )
    # Save to file
    with open(file, "w+") as f:
        f.write(response['fileContent'].decode("utf-8"))

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
    codecommit = session.client('codecommit')

    # Download CSHub-Scripts
    download_git_file('hello.py', '782efd459a2883f257e6aeb0022fd79e15650ce8')
