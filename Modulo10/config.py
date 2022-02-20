#PRUEBA DE TRY
# try:
#     open('config.txt')
# except FileNotFoundError:
#     print("Couldn't find the config.txt file!")

# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")

#PRUEBA DE TRY 2
# def main():
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("Couldn't find the config.txt file!")

#PRUEBA DE TRY 3
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")

# if __name__ == '__main__':
#     main()

#PRUEBA DE TRY 4
# try:
#     open("mars.jpg")
# except FileNotFoundError as err:
#     print("got a problem trying to read the file:", err)

# try:
#     open("config.txt")
# except OSError as err:
#     if err.errno == 2:
#          print("Couldn't find the config.txt file!")
#     elif err.errno == 13:
#         print("Found config.txt but couldn't read it")