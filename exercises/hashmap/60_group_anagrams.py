
                
# brutish and slow!
def group_anagrams(words):
    anagrams = []
    output_list = []

    # iterate over every word in input list
    for word in words:

        added = False

        temp_anagram = {
            "letters": {},
            "words": []
        }

        for letter in word:
            if letter not in temp_anagram["letters"]:
                temp_anagram["letters"][letter] = 1
            else:
                temp_anagram["letters"][letter] += 1
        
        for anagram in anagrams:
            if len(word) != len(anagram["words"][0]):
                continue
            
            is_anagram = True

            for letter in temp_anagram["letters"]:
                if letter not in anagram["letters"]:
                    is_anagram = False
                    break
                
                if temp_anagram["letters"][letter] != anagram["letters"][letter]:
                    is_anagram = False
                    break
            
            if is_anagram:
                anagram["words"].append(word)
                added = True
                break

        if not added:
            temp_anagram["words"].append(word)
            anagrams.append(temp_anagram)


    for anagram in anagrams:
        output_list.append(anagram["words"])

    return output_list


# more elegant solution O(n*m)
def group_anagrams_signature(words):

    output_list = []

    signatures = {}

    for word in words:

        default_signature = [0] * 26

        for char in word:
            index = ord(char) - ord('a')
            default_signature[index] += 1

        signature = tuple(default_signature)

        if signature in signatures:
            signatures[signature].append(word)
        else:
            signatures[signature] = [word]

    for signature in signatures:
        output_list.append(signatures[signature])   
    
    return output_list






print(group_anagrams_signature(["eat", "tea", "tan", "ate", "nat", "bat"]))