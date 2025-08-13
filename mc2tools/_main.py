# -*- coding: utf-8 -*-
import argparse
import sys

from . import address


def main():
    # Init ArgParser
    parser = argparse.ArgumentParser(
        prog="mc2tools",
        description="Minecraft Tool Using Python",
    )

    # SubParsers
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    """ Address SubCommand """
    address_parser = subparsers.add_parser(
        "address",
        help="Address Tool",
    )
    address_sub = address_parser.add_subparsers(
        dest="address_command",
        required=True,
    )
    # get_ip_address
    get_ip_parser = address_sub.add_parser(
        "get_ip_address",
        help="Get IP Address From Domain",
    )
    get_ip_parser.add_argument(
        "domain",
        type=str,
        help="Domain to get IP Address",
    )

    # Command Handling
    args = parser.parse_args()
    if args.command == "address":
        if args.address_command == "get_ip_address":
            try:
                ip = address.get_ip_address(args.domain)
                print(ip)
            except Exception as e:
                raise e
                sys.exit(1)
