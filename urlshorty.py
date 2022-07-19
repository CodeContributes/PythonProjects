import pyshorteners

user_url = input("Enter a URL: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(user_url)

print(short_url)