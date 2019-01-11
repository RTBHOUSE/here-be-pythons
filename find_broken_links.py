import re
import socket
import sys
import urllib.request
from glob import iglob
from typing import Iterator, TextIO, Tuple
from urllib.error import HTTPError, URLError

from dataclasses import dataclass

REQUEST_HEADERS = {'User-Agent': 'https://github.com/RTBHOUSE/here-be-pythons'}
TIMEOUT_SECONDS = 5
URL_REGEX = re.compile(
    r'(?:http|ftp|https)://'                    # protocol
    r'(?:[\w_-]+(?:(?:\.[\w_-]+)+))'            # domain
    r'(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'  # path
)  # yapf: disable


def find_broken_links(files_glob_pattern='docs/source/**/*.rst') -> None:
    counters = Counters()

    for file in _yield_files(files_glob_pattern):
        _process_urls_from_file(file, counters)

    _print_report(counters)

    if counters.broken_links_num == 0:
        sys.exit(0)
    else:
        sys.exit(1)


@dataclass
class Link:
    url: str
    health: str = None
    status_code: int = None


@dataclass
class Counters:
    ok_links_num: int = 0
    broken_links_num: int = 0
    timeout_links_num: int = 0


def _yield_files(files_glob_pattern: str) -> Iterator[TextIO]:
    files_paths = iglob(files_glob_pattern)
    for file_path in files_paths:
        with open(file_path) as file:
            yield file


def _process_urls_from_file(file: TextIO, counters: Counters) -> None:
    for link, line_num in _yield_links_from_file(file):
        _update_link_health(link, counters)
        if link.health == 'broken':
            print(f'url:       {link.url}')
            print(f'returns:   {link.status_code}')
            print(f'file:      {file.name}:{line_num}')
            print('')


def _yield_links_from_file(file: TextIO) -> Iterator[Tuple[Link, int]]:
    for line_num, line in enumerate(file, start=1):
        urls = URL_REGEX.findall(line)
        for url in urls:
            yield Link(url), line_num


def _update_link_health(link: Link, counters: Counters) -> None:
    request = urllib.request.Request(link.url, headers=REQUEST_HEADERS)

    try:
        urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS)
        link.health = 'ok'
        counters.ok_links_num += 1

    except (HTTPError, URLError) as exc:
        link.health = 'broken'
        counters.broken_links_num += 1
        try:
            link.status_code = exc.code
        except AttributeError:
            link.status_code = -1

    except socket.timeout:
        print(f'Timeout on: {link.url}', end='\n\n')
        link.health = 'timed-out'
        counters.timeout_links_num += 1


def _print_report(counters: Counters) -> None:
    counters_kwargs = (
        {'label': 'OK', 'counter': counters.ok_links_num},
        {'label': 'Broken', 'counter': counters.broken_links_num},
        {'label': 'Timed-out', 'counter': counters.timeout_links_num},
    )  # yapf: disable

    print('Broken Links Report')
    print('===================')
    for counter_kwargs in counters_kwargs:
        _print_urls_counter(**counter_kwargs)
    print(f'')
    print('--------------------------')
    print(f'Timeout set for {TIMEOUT_SECONDS} seconds.')
    print(f'')


def _print_urls_counter(label: str, counter: int) -> None:
    label_part = f'{label + ":":<13}'
    counter_part = f'{counter} URL{"" if counter == 1 else "s"}'
    print(f'{label_part}{counter_part}')


if __name__ == '__main__':  # pragma: no cover
    find_broken_links()
