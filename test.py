from jsphr_converter import convert_to_hr_and_save, convert_to_hr

# case 1 -- file
# Scenario: 
# Given a user has a JobSchema+ file,
# When they put their file into the utility,
# Then a human readable JD is produced and saved.
# -o output_file.txt
convert_to_hr_and_save(
    '07-19-2019_23-07-05_fcce43fa-cd52-4c6e-b202-7cc58b0de789_human-readable.json',
    'output_file.txt' # optional
)

convert_to_hr_and_save(
    '07-19-2019_23-07-05_fcce43fa-cd52-4c6e-b202-7cc58b0de789_human-readable.json'
)

# case 2 -- dict
# Scenario: 
# Given a user goes through the JDX workflow,
# When they finish,
# Then a human readable JD is produced and saved.
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