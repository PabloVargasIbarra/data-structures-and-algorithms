# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one dict
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if query.ind in self.elems:
                self.write_chain(cur for cur in reversed(self.elems[query.ind]))
            else:
                self.write_chain([])
        else:
            hash_value = self._hash_func(query.s)
            was_found = hash_value in self.elems
            if query.type == 'find':
                self.write_search_result(was_found and query.s in self.elems[hash_value])
            elif query.type == 'add':
                if was_found:
                    if query.s not in self.elems[hash_value]:
                        self.elems[hash_value].append(query.s)
                else:
                    self.elems[hash_value] = [query.s]
            elif query.type == 'del':
                if was_found and query.s in self.elems[hash_value]:
                    self.elems[hash_value].remove(query.s)
        # print(self.elems)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
