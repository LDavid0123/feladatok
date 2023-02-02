import urllib.request
import sys

def downnload_function(url):
    try:
        content = urllib.request.urlopen(url)
        page_content = content_read()
        file = open('page_content.txt', 'wb')
        file.write(page_content)
        file.close()
        print(('Content downloaded succesfully'))
    except:
        print('Something went wrong')



import bleach

bleach.clean('an <script>evil()</script> example')
u'an &lt;script&gt;evil()&lt;/script&gt; example'

bleach.linkify('an http://example.com url')
u'an <a href="http://example.com" rel="nofollow">http://example.com</a> url'

bleach.clean(
    "some text",
    tags=["a", "p", "img"],
    protocols=["http", "https"],
)

bleach.linkify(
    "some text",
    skip_tags=["pre"],
)

linker = Linker(
    skip_tags=["pre"],
    recognized_tags=html5lib_shim.HTML_TAGS + ["custom-element"],
)


pi = 3.14

def kerulet(r):
    return 2 * r * pi

def terulet(r):
    return r ** 2 * pi


from kor import kerulet as k_kerulet, terulet as k_terulet
from negyzet import kerulet, terulet

print(f'Kör kerülete: {kerulet(10):.2f}')
print(f'Kör területe: {kerulet(10):.2f}')

print(f'Négyzet kerülete: {kerulet(10):.2f}')
print(f'Négyzet kerülete: {kerulet(10):.2f}')