# Script to download the CSHub scripts from code commit repository
import argparse
import boto3

def download_git_file(file: str, repo: str = 'CSHub-Scripts') -> None:
    '''Downloads a specific file from a codecommit git repository'''

    # Get file as byte string
    response = codecommit.get_file(
        repositoryName=repo,
        filePath=file
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
    download_git_file('sess_start.py')
    download_git_file('packs.py')
    download_git_file('autostop.py')
