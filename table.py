import panda as pd

#url
url = "https://collegedunia.com/courses/bachelor-of-technology-btech-electronics-and-communication-engineering"

table = pd.read_html(url)[0]

print(table)