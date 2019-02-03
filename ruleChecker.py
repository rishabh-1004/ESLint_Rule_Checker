import json
import requests
from bs4 import BeautifulSoup as soup
import time


suggestion=[]
versions=[]

#--- Open required file ---#
with open('package.json') as f:
    data = json.load(f)

with open('.eslintrc.json') as f:
    data1 = json.load(f)



#--------Get rules -----------#
def scraper():
    url="https://eslint.org/docs/rules/"
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    uClient=requests.get(url,headers=headers)
    time.sleep(3)
    page_html=uClient.text
    page_soup=soup(page_html,"html.parser")
    containers=page_soup.find_all('table',class_="rule-list table table-striped")
    containers1=page_soup.find_all('table',class_="table table-striped")
    all_rules=[]
    for elements in containers:
        rules1=elements.find_all('a')
        for rule in rules1:
            all_rules.append(rule.text)
    rules_deprecated_list=[]
    rules_new_list=[]
    deprecated_dict={}
    for elements in containers1:
        rules_deprecated=elements.find_all('td')
        rules_new=elements.find_all('td',class_="replaced-by")
        for rule in rules_deprecated:
            rules_deprecated_list.append(rule.text)
        for rule in rules_new:
            rules_new_list.append(rule.text)
    del rules_deprecated_list[1::2]
    for i in range(0,len(rules_deprecated_list)):
        deprecated_dict[rules_deprecated_list[i][1:-1]]=rules_new_list[i][1:-1]
    
    return (all_rules,deprecated_dict)


def latest_version():
    suggestion=[]
    for rule in all_rules:
        
        if rule in rules:
            continue
        else:
            suggestion.append(rule)
    return suggestion

def previous_version():
    suggestion=[]
    deprecated_rules=[]
    for rule in rules:
        if rule in all_rules:
            continue
        else:
            deprecated_rules.append(rule)

    for rule in all_rules:
        
        if rule in rules:
            continue
        else:
            suggestion.append(rule)
    return   deprecated_rules , suggestion


eslint_version=data['devDependencies']['eslint'][1:]
print(eslint_version)
rules=list(data1['rules'].keys())

latest_releases=requests.get('https://api.github.com/repos/eslint/eslint/releases').json()


for item in latest_releases:
    release=item['tag_name'][1:]
    versions.append(release)



all_rules,deprecated_dict = scraper()

if eslint_version==versions[0]:
    print("You are using latest version")
    deprecated,suggestion  = previous_version()
    if (deprecated):
        print("These rules have been deprecated and following is there newer version" )
        for item in deprecated:
            print("%s : %s " %(item,deprecated_dict[item]))
        print('\n')
        print("You can still use these rules which you havent used yet")
    print(latest_version())
elif (eslint_version in versions):
    print("You are using version " + eslint_version + " but latest version is " + versions[0])
    deprecated,suggestion  = previous_version()
    print("These rules have been deprecated and following is there newer version" )
    for item in deprecated:
        print("%s : %s " %(item,deprecated_dict[item]))
    print('/n')
    print("Here are a list of eslint rules that you are not using yet "   )
    print(str(suggestion))
else:
    print("Wrong version")



