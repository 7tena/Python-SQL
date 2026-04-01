# Regular Expressions
import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.findall('My number is 415-555-4242. My office number is 212-555-0000.')
print('Phone numbers found: ' + str(mo))
print(phoneRegex.findall('My number is 415-555-4242. My office number is 212-555-0000.'))

phoneRegex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneRegex1.search('My number is 415-555-4242.')
print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(3))
print(mo1.groups())

phoneRegex2 = re.compile(r'(\(\d\d\d\)) \d\d\d-\d\d\d\d')
mo2 = phoneRegex2.search('My number is (415) 555-4242.')
print('Phone number found: ' + mo2.group()) 
print('country code: ' + mo2.group(1))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())   
mo = batRegex.search('Batmobile is fast')
print(mo.group())
mo = batRegex.search('Batcopter is flying')
print(mo.group())
mo = batRegex.search('Batmobile and batman is a comic book hero')
print(mo.group(1))   
mo = batRegex.search('Batwoman is a heroine')
print(mo == None)

batRegex1 = re.compile(r'Bat(wo)?man') #0 or 1 occurrence of wos
mo1 = batRegex1.search('The Adventures of Batman')
print(mo1.group())
mo1 = batRegex1.search('The Adventures of Batwoman')
print(mo1 == None)  