import argparse
import requests
from requests.auth import HTTPBasicAuth

url_base = 'https://github.com'


def download_repos(organisation, repos, user, token=None):
    for repo in repos:
        url = '{url_base}/{organisation}/{repo}/archive/master.zip'.format(
              url_base=url_base, organisation=organisation, repo=repo)
        filename = '{}.zip'.format(repo)

        response = requests.get(url, auth=HTTPBasicAuth(user, token))
        response.raise_for_status()

        if response.status_code == 200:
            print('Downloading repository {}'.format(url))
            with open(filename, "wb") as file:
                file.write(response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="authorization user")
    parser.add_argument("-t", "--token", help="token for the user",
                        default=None)
    parser.add_argument("-o", "--organisation",
                        help="organisation or user of the repo")
    parser.add_argument("-r", "--repos",
                        help="repos to download, comma separated")

    args = parser.parse_args()

    if not all([args.user, args.repos]):
        raise Exception("You have to provide user and repos")

    repos = args.repos.split(',')
    organisation = args.organisation or args.user

    download_repos(organisation, repos, args.user, args.token)

if __name__ == '__main__':
    main()
