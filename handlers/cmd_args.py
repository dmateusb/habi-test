import argparse

class HandleArgs:
    @staticmethod
    def get_args():
        ap = argparse.ArgumentParser(
            prog='args',
            allow_abbrev=False,
            description='List of optional arguments for selecting from the CLI',
            epilog='Enjoy the work! :)'
        )
        ap.add_argument('-ms', '--microservice',
                        type=str,
                        required=False,
                        help="Select a specific service to be a module.")
        
        args = ap.parse_args()
        return args
