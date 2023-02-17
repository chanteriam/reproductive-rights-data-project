"""
The __main__.py file serves as the project running file and calls on particular
packages based on the flags that are passed to it.

Author(s): Michael Plunkett, Kate Habich
"""

import argparse
import visualization.service
import api.abortion_policy_api

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
        api.abortion_policy_api.main()

    if args.parse_data:
        print("We are gonna do some data parsing work")

    if args.visualize:
        visualization.service.main()
