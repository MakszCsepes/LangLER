import json

from file_lines import *

people_string = '''
{
    "people": [
        {
            "name": "John",
            "phone": "674-585"
        },
        {
            "name": "Mark",
            "phone": "524-705"
        }
    ]
}
'''

data = json.loads(people_string)

print(type(data))
print(data)



# json
def json_interpreter():
    with open('languages/english.txt', 'r') as outfile:
        lines_array = outfile.readlines()

    a = {}
    for i in lines_array:
        if i == lines_array[0]:
            print(i)
            continue
        word = get_word_from_line(i)
        trans = get_translation_from_line(i)

        a[word] = trans

    with open('english.json', 'w') as outfile:
        json.dump(a, outfile, indent=4, ensure_ascii=False)