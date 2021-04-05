# u-slash

Command line script that downloads unique files from Reddit users' submissions

## Installation

    $ git clone https://github.com/2yr434hgd7fy384/u-slash
    $ pip install u-slash/

## Usage

    u-slash [OPTIONS] [USERNAMES]... DIRECTORY

`u-slash` downloads all of the files posted on Reddit by any number of users, and saves them to the specified directory. Each file is sorted into a subdirectory for the Reddit user that posted it.

By recording the URL and MD5 hash of each file that it saves, `u-slash` is able to ignore or remove duplicate files as it goes.

`u-slash` can only download a file if the Reddit submission links to it directly.
