# Jespher conversion

Converts interval intermediate format of JobSchema+ Human Readable (jspher) files to txt format for dissemination.

## Package

Use pipenv to import this repo
```python
from jsphr_converter import convert_to_hr_and_save, convert_to_hr

convert_to_hr_and_save(
    '07-19-2019_23-07-05_fcce43fa-cd52-4c6e-b202-7cc58b0de789_human-readable.json',
    'output_file.txt' # optional
)

jsphr = {
    'humanReadable': {
        'schema': [
            'title',
            'salary'
        ],
        'data': {
            'title': 'This is the title',
            'salary': '50k'
        }
    }
}

convert_to_hr_and_save(
    jsphr
)

print(
    convert_to_hr(jsphr)
)
```

## Command line Usage

Get arg help

```bash
python3 command_line.py -h
```

Specify an input file

```bash
python3 command_line.py -f 07-19-2019_23-07-05_fcce43fa-cd52-4c6e-b202-7cc58b0de789_human-readable.json
```

Specify an output file

```bash
python3 command_line.py -f 07-19-2019_23-07-05_fcce43fa-cd52-4c6e-b202-7cc58b0de789_human-readable.json -o output_file.txt
```

