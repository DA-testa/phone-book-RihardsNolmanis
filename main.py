#python3
# Rihards Nolmanis 221RDB431
## kods strādā, bet inputiem ir jābut bez atstarpēm.
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n_new = int(input())
    return [Query(input().split()) for i in range(n_new)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    phonebook = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            phonebook[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in phonebook:
                del phonebook[cur_query.number]
        else:   
            response = phonebook.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))    