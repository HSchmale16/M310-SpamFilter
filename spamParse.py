# Contains the spam parsing functions
import email 

msg = email.message

from cStringIO import StringIO
from email.generator import Generator
fp = StringIO()
g = Generator(fp,mangle_from_=Fasle, maxheaderlen=60)
g.flatten(msg)
text = fp.getvalue()
