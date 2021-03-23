""" Generate lovely ideas """

import random
import re
from ideaspace import productions

# ideas:
# - a way to indicate that a key is "widening" or not; i.e. it should behave as if inlined into the caller
#   before probabilities are calculated, or not
# - allow a dictionary as an entry; use its 'main' production
# - support for plurals
# - avoiding repeating words or choices

def randomly_generated(nt):
    template = random.choice(productions[nt])
    def replace(match):
        return randomly_generated(match.group(1))
    return re.sub(r'\$\{(\w+)\}', replace, template)

def random_idea():
    return randomly_generated('idea')

if __name__ == '__main__':
    print(random_idea())
