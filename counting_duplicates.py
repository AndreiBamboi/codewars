def duplicate_count(text):
    create_list=list(text.lower())
    count_list=[]
    print(create_list)
    multiple_values = set(count_list)
    for i in create_list:
        if create_list.count(i)>1 == True:
            count_list.append(i)
    print(type(count_list))
    print(set(count_list))
    print(len(set(count_list)))
    return len(set(count_list))
duplicate_count('abcdeaaaa')
