import pyperclip as pc
from bs4 import BeautifulSoup
from urllib2 import urlopen


#grabbing from codesters
BASE_URL = "https://www.codesters.com/code/"

def get_category_links(section_url):
    # Put the stuff you see when using Inspect Element in a variable called html.
    html = urlopen(section_url).read()    
    # Parse the stuff.
    soup = BeautifulSoup(html, "lxml")    
    # The next two lines will change depending on what you're looking for. This 
    # line is looking for <dl class="boccat">.  
    boccat = soup.find("dl", "boccat")    
    # This line organizes what is found in the above line into a list of 
    # hrefs (i.e. links). 
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links


#logic in the code
one = 10
two = 8
three = 4



#logic in the thing
#math = one / two - three
math =  3 % 2 + 4 ** 3
print(math)
pc.copy(math)
#text2 = pc.paste()