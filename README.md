# WikiScraper
Microservice that scrapes introductory paragraph from Wikipedia page.



Requesting Data:

To request data from this microservice, a string must be entered into the input.txt file. In this case, the string will be something you want to search for on Wikipedia. Currently, the input is coming from app.py where the user inputs a string that is then passed to input.txt. Essentially, to request data, all that needs to be done is that the main file needs to write some string to input.txt.

Example:

some_string = <whatever you decide to search>
inp = open("input.txt", "w")
    inp.write(f"{some_string}")
    




Receiving Data:

To receive data from this microservice, the text from the file output.txt must be read. In this case, the text from the output file will be the first paragraph of data from a certain Wikipedia page. Currently, the output is read from output.txt and being printed to the console. Essentially, to receive data, all that needs to be done is that the main file needs to read the contents of output.txt

Example:

output = open("output.txt", "r+", encoding = "utf-8").read()


![image](https://user-images.githubusercontent.com/91383601/218396003-4061ed14-6847-463c-aacd-9e3214261d75.png)

