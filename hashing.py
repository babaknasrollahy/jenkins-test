from random import randint,choice
import string 
import re

class hashing :
    dic_DB = {}
    def create_DBhash(val):
        num = [0,1,2,3,4,5,6,7,8,9]
        i = 1
        char= ""
        while i < 3 :
            char += choice(string.ascii_letters)
            i += 1
        i = 1
        while i < 3 :
            char += str(choice(num))
            i += 1
        with open("hash.txt","a") as file:
            file.write(f"{val} = {char}\n")

    def create_hash(txt):
        final_hash = ""
        hash = []
        i = 0
        with open("hash.txt") as file :
            text = file.read()
            hash = re.findall('\w{4}',text, re.DOTALL)

        for char in string.ascii_letters:
            hashing.dic_DB.update({char : hash[i]})
            i += 1
        
        for char in txt:
            final_hash += hashing.dic_DB[char]

        return final_hash
    
 
    def read_hash(hash_txt):
        list1 = []
        i = 0
        result = ""
        final_result = ""
        hash = []
        j = 0
        with open("hash.txt") as file :
            text = file.read()
            hash = re.findall('\w{4}',text, re.DOTALL)

        for char in string.ascii_letters:
            hashing.dic_DB.update({char : hash[j]})
            j += 1

        for char in hash_txt :
            result += char
            i += 1

            if i == 4 :
                for val in hashing.dic_DB :
                    if hashing.dic_DB[val] == result :
                        final_result += val
                        
                i = 0
                result = ""
        

        return final_result   
                        
                        
    
    


me = hashing
me.create_DBhash()