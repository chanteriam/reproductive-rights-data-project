"""
The __main__.py file serves as the project running file and calls on particular
packages based on the flags that are passed to it.

Author(s): Michael Plunkett, Kate Habich
"""

import argparse
import visualization.service
import api.service
import data_handling.service

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--api",
        help="Get data from API",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--parse-data",
        help="Parse data from the API and external sources",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--visualize",
        help="Use data from the ",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )

    args = parser.parse_args()

    if args.api:
        api.service.main()

    if args.parse_data:
        data_handling.service.main()

    if args.visualize:
        visualization.service.main()
