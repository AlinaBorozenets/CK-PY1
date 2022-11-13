# TODO решить с помощью list comprehension и распечатать его
import random
from pprint import pprint
from typing import List, Dict, Any, Generator

list_dictionary = [{"bin": bin(z), "dec": z, "hex": hex(z), "oct": oct(z)} for z in range(16)]

pprint(list_dictionary)