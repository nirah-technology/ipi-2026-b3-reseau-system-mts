# Sans le Context Manager
# file = open("text.txt", "a")
# file.write("Bonjour à vous tous!\n")
# file.flush()
# file.close()

# Avec le Context Manager

with open("other-test.txt", "a") as file:
    file.write("Super, ça fonctionne.\n")
del file
file.write("okok")