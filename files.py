fileHandler = open("text.txt", "a")

fileHandler.write("Lots of text here\n")
fileHandler.write("This is more text.")
fileHandler.write("More.")
fileHandler.write("More.")

fileHandler.close()

# import os
# os.rmdir("aFolder")