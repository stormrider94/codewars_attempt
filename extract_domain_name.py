import re

# just get anything that comes before a dot 
def domain_name(url):
    domain_reg = re.compile(r'(www.)?(\w+)\.')
    matched_objects = domain_reg.search(url)
    print(matched_objects.group())

domain_name('http://google.com')
domain_name('http://google.co.jp')
domain_name("https://123.net")
domain_name("https://hyphen-site.org")
domain_name("http://codewars.com")
domain_name("https://youtube.com")
domain_name("http://www.codewars.com/kata/")
domain_name('http://google.com')
domain_name("icann.org")
domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com")
domain_name("https://www.cnet.com")