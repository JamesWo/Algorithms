# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> %s > %s" % ( attr[0], attr[1] ))

inp = "".join( [input() for _ in range(int(n))] ) 

parser = MyHTMLParser()
parser.feed( inp )
