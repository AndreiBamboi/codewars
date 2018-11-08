import string
def alphabet_position(text):
    list_obj=list(text)
    o_lista=[]
    for x in list_obj:
        if x.isalpha()==True:
            o_lista.append(x)
    new_list = str(''.join(o_lista).lower())
    number_list = []
    for i in new_list:
        index_value=string.ascii_letters.index(i)
        number_list.append(index_value+1)
    num_to_str=str(number_list)
    print(' '.join(map(str, number_list)))
    return ' '.join(map(str, number_list))

alphabet_position("The sunset sets at twelve o' clock.")