import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--api", help="Get data from API", type=bool,
                        default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument("--parse-data",
                        help="Parse data from the API and external sources",
                        type=bool, default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--visualize", help="Use data from the ",
                        type=bool, default=False,
                        action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    if args.api:
        print("We are gonna do some API work")

    if args.parse_data:
        print("We are gonna do some data parsing work")

    if args.visualize:
        print("We are gonna do some visualizations")
