import json
import datetime


def _format_header(text):
    """returns text
    """
    return text


def _format_body(text):
    """returns text
    """
    return text


def _format_sub(text):
    """returns text
    """
    return f'- {_format_body(text)}'


def convert_to_hr(jsphr_data):
    """ returns text
    """
    
    schema = jsphr_data['humanReadable']['schema']
    data = jsphr_data['humanReadable']['data']

    text = ''

    def out(text, data):
        text = f'{text}\n{data}'
        return text

    for header in schema:
        text = out(text, _format_header(header))
        
        value = data[header]
        if isinstance(value, list):
            # iterate each item
            for item in value:
                text = out(text, _format_sub(item))

        else:
            text = out(text, _format_body(value))
        
        text = out(text, '\n')

    return text.strip('\n')


def jsphr_file_loader(file_path):
    """Loads a JobSchema+ HumanReadable JSON file
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_output(hr_text, output_file):
    with open(output_file, 'w+') as f:
        f.write(hr_text)


def load_passed_jsphr(jsphr):
    if isinstance(jsphr, dict):
        return jsphr

    elif isinstance(jsphr, str):
        return jsphr_file_loader(jsphr)


def convert_to_hr_and_save(jsphr, output_file=None):
    """jsphr: dict or file
    output_file: Full file path to output to
    """
    now_string = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S.txt')
    output_file = output_file if output_file else now_string

    jsphr_data = load_passed_jsphr(jsphr)
    
    hr_text = convert_to_hr(jsphr_data)
    assert(hr_text is not None)
    print(hr_text)

    save_output(hr_text, output_file)
