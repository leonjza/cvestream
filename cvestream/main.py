import json
import zlib

import requests
from rich.console import Console

SOURCE = 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-recent.json.gz'
console = Console()


def get_data() -> list:
    """
        Downloads data from the NVD.

        :return:
    """

    r = requests.get(SOURCE)

    if not r.ok:
        console.print(f'[red]http request failed[/]')
        return []

    data = zlib.decompress(r.content, zlib.MAX_WBITS | 32)
    data = json.loads(data)["CVE_Items"]
    return sorted(data, key=lambda x: (x["cve"]["CVE_data_meta"]["ID"]))


def print_cve(cve: dict) -> None:
    """
        Print CVE information.

        :param cve:
        :return:
    """

    print('')
    cve = cve['cve']

    cve_id = cve["CVE_data_meta"]["ID"]
    description = cve["description"]["description_data"][0]["value"]
    references = cve["references"]["reference_data"]
    console.print(f'------ {cve_id} ------')
    console.print(f'{description}')
    for reference in references:
        console.print(f'{reference["tags"]} | url: {reference["url"]}')


def main():
    """
        The default entrypoint for CVESTREAM

        :return:
    """

    data = get_data()
    console.print(f'found {len(data)} cve\'s')

    if len(data) <= 0:
        return

    for cve in data:
        print_cve(cve)


if __name__ == '__main__':
    main()
