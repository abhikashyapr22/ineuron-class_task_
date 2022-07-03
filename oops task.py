class string:
    """generalising the tasks given before, will perform operations related to list"""

    def rev_string(self, s):
        """will reverse a given string"""
        return s[::-1]

    def con_upper_split(self, s):
        """first convert the string in upper case and then splits"""
        s = s.upper()
        return s.split(" ")

    def to_lower(self, s):
        """convert string into lowercase"""
        return s.lower()

    def capitalize(self, s):
        """capitalize the whole string"""
        return s.capitalize()

    def rem_ext_spaces(self, s):
        """remove spaces before and after the string"""
        return s.strip()

    def conCat(self, *l):
        """return concatenated string of given strings"""
        return "".join(l)


test_st = string()


# print(test_st.rev_string("abhi"))
# print(test_st.con_upper_split("my name is abhishek"))
# print(test_st.to_lower("aBHISHEK"))
# print(test_st.capitalize("hello dear"))
# print(test_st.rem_ext_spaces("   hello   "))
# print(test_st.conCat("My","name","is","Abhishek"))


class ListOp:
    """includes list related operations"""

    def append(self, l, val):
        """appends val in the list l"""
        l[len(l):] = [val]
        return l

    def pop(self, l, ind=-1):
        """pop out the element at a given index, else last element, if index not given"""
        temp = l[ind]
        l.remove(l[ind])
        return temp

    def extend(self, l, l2: list):
        """append the given list l2 elements into the desired list l
        :type l, l2: list
        """
        for i in l2:
            l.append(i)
        return l

    def squre(self, l):
        """return list containing squires of given list elements"""
        return list(map(lambda x: x ** 2, l))

    def ext_lt_entity(self, l):
        """extract all the list entities from given list of list"""
        for i in l:
            if type(i) == list:
                print(i)

    # @staticmethod
    def summation(self,l):
        """given sum of all the elements of given list"""
        sm: int = 0
        for i in l:
            sm += i
        return sm

    def filter_odds(self,l):
        """filter out odd elements from given list"""
        od = []
        for i in l:
            if i%2 != 0:
                od.append(i)
        return od

test2 = ListOp()
l = [2, 3, 4, 5, 6, 7, 8]
# print(test2.pop(l, 3))
# print(l)
# test2.append(l,9)
# print(l)
# print(test2.extend(l,[2,4,8,90,8]))
# print(test2.squre(l))
l2 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
      {'k1': 'sudh', 'k2': 'ineuron', 'k3': 'kumar', 3: 6, 7: 8},
      ['ineuron', 'data science']]
#test2.ext_lt_entity(l2)
#print(test2.summation(l))
print(test2.filter_odds(l))


