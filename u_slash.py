import hashlib
import os
from urllib import parse
import click
import praw
import requests


reddit = praw.Reddit(
    client_id = "BwzpDHgDZ5xRqQ",
    client_secret = "B10ZUMyoUwFdhMo35SNEljJotqPj_Q",
    username = "Equssy",
    password = "WawJ9PZQgcvFK6Y",
    user_agent = "u-slash by u/Equssy"
)


@click.command()
@click.argument("usernames", nargs=-1, type=click.STRING)
@click.argument("directory", nargs=1, type=click.Path(exists=False))
def u_slash(usernames, directory):
    urls = list()
    md5s = list()
    saved = 0

    for username in usernames:
        redditor = reddit.redditor(username)

        for submission in redditor.submissions.new(limit=None):
            if submission.url in urls or submission.is_self:
                continue

            path = parse.urlparse(submission.url).path
            tail = path.rsplit("/", 1)[-1]
            if os.path.splitext(tail)[1] == "":
                continue

            click.echo(f"Downloading media from {submission.url}...")
            with requests.get(submission.url, stream=True) as r:
                r.raise_for_status()
                redditor_directory = os.path.join(directory, redditor.name)
                os.makedirs(redditor_directory, exist_ok=True)
                filepath = os.path.join(redditor_directory, tail)
                with open(filepath, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)
            click.echo(f"Saved media at {filepath}")

            with open(filepath, "rb") as f:
                md5 = hashlib.md5(f.read()).hexdigest()
            click.echo(md5)
            if md5 in md5s:
                os.remove(filepath)
                click.echo("Removed duplicate")
                continue

            urls.append(submission.url)
            md5s.append(md5)
            saved += 1

        click.echo(f"Saved all media from {redditor.name}")

    click.echo(f"Saved {saved} file{'' if saved == 1 else 's'}")


if __name__ == "__main__":
    u_slash()
