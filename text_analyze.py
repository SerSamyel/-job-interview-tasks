def my_input(file:str):
    '''
    open text file, separate in line, iterate word for line, filter . , ' and word in ignore list
    return generator - word's start is title
    '''
    ignore_list = ('I', 'Sir','The','He','It','Dr','We','But', 'If', 'There','And','You','Mr','A',
                   'What', 'No', 'Yes', 'Then', 'My', 'That', 'Well', 'In', 'Hall', 'Mrs')
    with open(file) as input_file:
        for line in input_file:
            line = line.strip().split()
            for word in line:
                if word.startswith('"'):
                    word = word[1:]
                if word.endswith((',', '.')):
                    word = word[:-1]
                if word.istitle() and word not in ignore_list:
                        yield word

def word_count(iterable_object):
    '''
    input - iterable object
    return dictionary - word: count word in iterable_object
    '''
    storage = dict()
    for word in iterable_object:
        if word in storage:
            storage[word] += 1
        else:
            storage[word] = 1
    return storage

def sort_10_top(dictionary):
    '''
    return top 10 most common word
    '''
    temp = list()
    for i in sorted(dictionary.items(), key=lambda para: para[1], reverse=True):
        temp.append(i)
    return temp[:10]

if __name__ == '__main__':
# Тесты
    print("Test one - func word_count")
    if word_count([1,2,3,4,5,5,0,0]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 0: 2}:
        print('Test - OK')
    else:
        print('Test - Faild!')
    print("Test two - func sort_10_top")
    if sort_10_top({1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 0: 2}) == [(5, 2), (0, 2), (1, 1), (2, 1), (3, 1), (4, 1)]:
        print('Test - OK')
    else:
        print('Test - Faild!')
# Замер времени выполнения для оптимизации.
    import time
    print("time test begin")
    start_time = time.time()
    temp_dict = word_count(my_input("test_text.txt"))
    print(sort_10_top(temp_dict))
    print("Time test end - {0} sec".format(time.time() - start_time))
