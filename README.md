# Github archiver

Github archiver is a small tool to batch download repository archives.
It may be useful for downloading old repositories for organisations reaching their private repos limit

## Installation

You need to download requirements

```
pip install -r requirements.txt
```

## Usage

To download the repos you need to pass them as parameteres:

```
python archiver.py --u aniav --r myrepo,myotherrepo
```

If you want to download private repos you need to generate a private access token here: https://github.com/settings/tokens and use it along with your username

```
python archiver.py --u aniav --t my_token --r myrepo,myotherrepo
```

If the repo you require does not belong to the user put in the request, but to another user or organisation you need to pass it in the `--o` param:

```
python archiver.py --u aniav --t my_token --r myrepo,myotherrepo --o 10clouds
```
