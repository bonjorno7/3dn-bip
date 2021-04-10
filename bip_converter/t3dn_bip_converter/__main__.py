from argparse import ArgumentParser
from .convert import convert_file

if __name__ == '__main__':
    parser = ArgumentParser(description='convert between BIP and other formats')
    parser.add_argument('--src', type=str, required=True, help='input path')
    parser.add_argument('--dst', type=str, required=False, help='output path')

    args = parser.parse_args()
    convert_file(args.src, args.dst)
