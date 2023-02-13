import time
from urllib.request import urlopen
import json

while True:
    input = open("input.txt", "r+")
    data = input.read()
    
    #checks for empty text file
    if data != "":
        # makes data readable for URL
        print(f"Received input: {data}")
        data = data.replace(" ", "_") 

        # Wikpedia's API prop extracts source: https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bextracts
        url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={data}" 
        # gets information from webpage as json object
        response = urlopen(url)
        # parses json object
        data_json = json.loads(response.read())
        # code block for returning only extracted text, raises error if page could not be found
        try:
            page_id_find = data_json["query"]["pages"]
            for item in page_id_find:
                page_id = item
            extract = page_id_find[page_id]["extract"]
        except:
            extract = "Error: Could not find page."
        # writes text to output file
        output = open("output.txt", "w", encoding = "utf-8")
        output.write(f"{extract}")
        input.truncate(0)
        output.close()
    input.close()