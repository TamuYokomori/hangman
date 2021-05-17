# find words having 'oo' after some characters.

import re

docs = "The ghost that says boo haunts the loo."

m = re.findall(".oo", docs, re.IGNORECASE)
print(m)
