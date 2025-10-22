class Hashmap:

    def __init__(self, size=7):
        self.data_map = [None] * size
        
    
    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash
    

    def print_hashmap(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")


    def set(self, key, value):

        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        for pair in self.data_map[index]:
            if pair[0] == key:
                pair[1] = index
        

        self.data_map[index].append([key, value])

        

    def get(self, key):
        index = self.__hash(key)
        bucket = self.data_map[index]

        if bucket is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair
        return None
    
    def remove(self, key):
        index = self.__hash(key)
        bucket = self.data_map[index]

        if bucket is not None:
            for pair in bucket:
                if pair[0] == key:
                    temp = pair[1]
                    bucket.remove(pair)
                    if len(bucket) == 0:
                        self.data_map[index] = None
                    return temp

        return None
    

    def keys(self):
        keys = []
        for bucket in self.data_map:
            if bucket is not None:
                for item in bucket:
                    keys.append(item[0])
        return keys


