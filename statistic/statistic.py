def openreadtxt(file_name):
    data = {'triples':0, 'r': [],'t': [], 'a': [], 'i': [], 'o': [], 'l': []}
    file = open(file_name,'r')
    file_data = file.readlines()
    data['triples'] = len(file_data)
    for row in file_data:
        tmp_list = row.split('\t')
        tmp_list[-1] = tmp_list[-1].replace('\n','')
        if tmp_list[1] not in data['r']:
            data['r'].append(tmp_list[1])
        for temp in tmp_list:
            if '.t' in temp:
                if temp not in data['t']:
                    data['t'].append(temp)
            elif '.a' in temp:
                # without hash
                tmp_a = temp.split('_')
                if tmp_a[0] not in data['a']:
                    data['a'].append(tmp_a[0])
                # with hash
                # if temp not in data['a']:
                #     data['a'].append(temp)
            elif '.i' in temp:
                if temp not in data['i']:
                    data['i'].append(temp)
            elif '.o' in temp:
                if temp not in data['o']:
                    data['o'].append(temp)
            elif '.l' in temp:
                if temp not in data['l']:
                    data['l'].append(temp)
    return data
  
  
if __name__=="__main__":
    input_path = 'SkillKG_V1.txt'
    # input_path = 'SkillKG_V1_exclude_dbpedia.txt'
    output_path = 'data_info.txt'
    data = openreadtxt(input_path)
    with open(output_path, 'w', encoding='utf-8') as file1:
        print('triples:', data['triples'], 'entities:', len(data['t'])+len(data['a'])+len(data['i'])+len(data['o'])+len(data['l']), 'relations:', len(data['r']), '\n', file=file1)
        print('tasks:', len(data['t']), 'actions:', len(data['a']), 'subjects:', len(data['i']), 'objects:', len(data['o']), 'locations:', len(data['l']), '\n', file=file1)
        print('\nrelations:', file=file1)
        for index, r in enumerate(data['r']):
            print(index + 1, r, file=file1)
        print('\ntasks:', file=file1)
        for index, t in enumerate(data['t']):
            print(index + 1, t, file=file1)
        print('\nactions:', file=file1)
        for index, a in enumerate(data['a']):
            print(index + 1, a, file=file1)
        print('\nsubjects:', file=file1)
        for index, i in enumerate(data['i']):
            print(index + 1, i, file=file1)
        print('\nobjects:', file=file1)
        for index, o in enumerate(data['o']):
            print(index + 1, o, file=file1)
        print('\nlocations:', file=file1)
        for index, l in enumerate(data['l']):
            print(index + 1, l, file=file1)