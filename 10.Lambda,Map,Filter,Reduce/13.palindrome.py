"""Write a Python program to find palindromes in a given list of strings using Lambda.
Original list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""
lis=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
res=list(filter(lambda x:(x == x[::-1]),lis))
print(res)