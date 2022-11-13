# Generate UUID - EPUB3 seems to require an identifier. If the ISBN, is not present then it will accept a UUID, DOI or .

import uuid, json

with open("metadata.json") as json_file:
    data = json.load((json_file), object_pairs_hook=OrderedDict) #For some reason the order is randomised, this preserves the order.

if data["UUID"] == "yes" or "Yes":

uuid = uuid.uuid4()
