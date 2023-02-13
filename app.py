import time

while True:
    search = input("What would you like to search? ")
    print("\n")
    inp = open("input.txt", "w")
    inp.write(f"{search}")
    inp.close()
    time.sleep(1)
    output = open("output.txt", "r+", encoding = "utf-8")
    print(f"Received output: {output.read()}\n")
    output.truncate(0)
    output.close()


