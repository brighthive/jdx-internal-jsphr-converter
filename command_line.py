import argparse
from jsphr_converter import convert_to_hr_and_save

parser = argparse.ArgumentParser(description='converts')
parser.add_argument(
    '-f',
    '--file',
    help='file to convert'
)
parser.add_argument(
    '-o',
    '--output-file',
    help='where to save?'
)
# parser.add_argument(
#     '-s',
#     '--silent',
#     help='no console output'
# )
args = parser.parse_args()

convert_to_hr_and_save(args.file, args.output_file)