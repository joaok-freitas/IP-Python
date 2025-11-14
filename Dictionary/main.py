def conta_carateres(string):
    dictionary = { }
    for i in string:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

def soma_quadrados_valores(dictionary):
    a = 0
    for i in dictionary:
        a += dictionary[i]**2
    return a

def len_dictionary(dictionary):
    a = 0
    for i in dictionary:
        a += 1
    return a

def remove_dictionary(dictionary, input_key):
    new_dictionary = {}
    for i in dictionary:
        if i != input_key:
            new_dictionary[i] = dictionary[i]
    return new_dictionary

def remove_dictionary2(dictionary, input_key):
    if input_key in dictionary:
        del dictionary[input_key]
    return dictionary

def combine_dictionaries(dictionary1, dictionary2):
    new_dictionary = dictionary1
    for i in dictionary2:
        if i in new_dictionary:
            new_dictionary[i] = new_dictionary[i] + dictionary2[i]
        else:
            new_dictionary[i] = dictionary2[i]
    return new_dictionary

if __name__ == '__main__':
    diction = {'a':2,'b':5,'c':3}
    diction2 = {'a':4,'d':3}
    text = "lolol"
    print(conta_carateres(text))
    print(soma_quadrados_valores(diction))
    print(len_dictionary(diction))
    print(remove_dictionary(diction, 'a'))
    print(remove_dictionary2(diction, 'a'))
    print(combine_dictionaries(diction, diction2))