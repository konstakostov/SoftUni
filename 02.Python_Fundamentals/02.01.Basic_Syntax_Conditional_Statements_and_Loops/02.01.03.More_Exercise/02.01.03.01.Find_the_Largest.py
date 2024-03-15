num = int(input())      # User defined number

lst = [int(i) for i in str(num)]    # Int to 04.10.01.03.List, so we can sort all the elements
lst.sort(reverse = True)            # 04.10.01.03.List is sorted in descending order

out = ''.join([str(nlst) for nlst in lst])      # 04.10.01.03.List is turned into string

print(out)      # We print final result 04.03.01.04.Multilevel_Inheritance string
