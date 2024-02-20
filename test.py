import json
with open('data/machine_generate_dialog_zh.json', 'r', encoding='utf8') as f:
    rlist = [json.loads(s) for s in f.readlines()]

import re

rlist1 = [re.split('<Round \d>\n', e['response']) for e in rlist if e]
rlist2 = []
for i, e in enumerate(rlist1):
    template = {
        'id': f'{i}',
        "conversations": []
    }
    for ee in e:
        st = ee.strip()
        if st:
            stlist = st.split('\n')
            for se in stlist:
                if se.strip():
                    role = 'user'
                    if se.strip()[1]=='A':
                        role = 'assistant'
                    template['conversations'].append({'from':role, 'value': se.strip()[4:].strip()})
    rlist2.append(template)
    # break

def write2json_file(fp, data, encoding='utf-8'):
    """
    Converts arbitrary object recursively into JSON file. 
    Use ensure_ascii=false to output UTF-8.
    """
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
write2json_file('test1087.json', rlist2)