import argparse

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

import json
import datetime


def format_header(text):
    """returns text
    """
    return text


def format_body(text):
    """returns text
    """
    return text


def format_sub(text):
    """returns text
    """
    return f'- {format_body(text)}'


def convert_human_readable_to_txt(json_dict):
    """ returns text
    """

    schema = json_dict['schema']
    data = json_dict['data']

    text = ''

    def out(text, data):
        text = f'{text}\n{data}'
        return text

    for header in schema:
        text = out(text, format_header(header))
        
        value = data[header]
        if isinstance(value, list):
            # iterate each item
            for item in value:
                text = out(text, format_sub(item))

        else:
            assert(isinstance(value, str))
            text = out(text, format_body(value))
        
        text = out(text, '\n')

    return text.strip('\n')


with open(args.file, 'r') as f:
    data = json.load(f)

assert(data is not None)
text = convert_human_readable_to_txt(data['humanReadable'])

print(text)

now_string = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S')

output_file = args.output_file if args.output_file else now_string
output_file = f'{output_file}'
with open(output_file, 'w+') as f:
    f.write(text)
