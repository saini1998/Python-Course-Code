# Learn
# 1. Files
# 2. SQLite
# 3. Date/Time
# 4. Random Values
# 5. Email

# WORKING WITH PATHS

# Google python3 pathlib
import subprocess
import sys
from string import Template
from email.mime.image import MIMEImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import shutil
import csv
import json
import sqlite3
import time
import random
import string
from datetime import datetime, timedelta
from time import ctime
from pathlib import Path
from zipfile import ZipFile
path = Path("ecommerce/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.suffix)
print(path.stem)
print(path.parent)
path = path.with_name("file.txt")
# path = path.with_suffix(".txt")
print(path)


# WORKING WITH DIRECTORIES

# path.mkdir()
# path.rmdir()
# path.rename()
path = Path("ecommerce")
for p in path.iterdir():
    print(p)
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
py_files = [p for p in path.rglob("*.py")]
print(py_files)


# WORKING WITH FILES

# from time import ctime
path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))
# print(path.read_text())
# path.write_text("...")
# path.write_bytes()

source = Path("ecommerce/__init__.py")
target = Path() / "__init.py"
target.write_text(source.read_text())
# import shutil
shutil.copy(source, target)


# WORKING WITH ZIP FILES

# from zipfile import ZipFile
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")


# WORKING WITH CSV FILES

# import csv
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)


# WORKING WITH JSON FILES

# import json
# movies = [
#     {"id": 1, "title": "terminator", "year": 1984},
#     {"id": 2, "title": "kindergarden cop", "year": 1990}
# ]
# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])


# WORKING WITH SQLite DATABASE

# import sqlite3
# NOTE to write in SQLite
# movies = json.loads(Path("movies.json").read_text())
# print(movies)
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()
# db browser for sqlite
# NOTE to read from Movies
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    # movies = cursor.fetchall()
    # print(movies)


# WORKING WITH TIMESTAMPS

# import time
# import datetime
# print(time.time())
def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end-start
print(duration)


# WORKING WITH DATETIMES

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
# google python 3 strptime
dt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)


# WORKING WITH TIME DELTAS

dt1 = datetime(2018, 1, 1) + timedelta(days=1)
print(dt1)
dt2 = datetime.now()
duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())


# GENERATING RANDOM VALUES

# import random
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices("abcdefghi", k=4)))
print(",".join(random.choices("abcdefghi", k=4)))
print(string.digits)
print("".join(random.choices(string.ascii_letters+string.digits, k=4)))
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)


# OPENING THE BROWSER

# import webbrowser
print("Deployement completed")
# webbrowser.open("https://google.com")


# SENDING EMAILS

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# NOTE templete topic part
template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "mosh hemadani"
message["to"] = "sainiaaryaman1998@gmail.com"
message["subject"] = "This is a test"
# message.attach(MIMEText("Body"))
message.attach(MIMEText(template.substitute({"user": "John"}), "html"))
# message.attach(MIMEImage(Path("mosh.png").read_bytes()))

# import smtplib
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    try:
        smtp.login("sainiaaryaman1998@gmail.com", "#vbnm007")

    except (smtplib.SMTPAuthenticationError) as ex:
        print("Google does not allow login")

    else:
        smtp.send_message(message)
        print("message sent")

    print("message dealt")

# from email.mime.image import MIMEImage


# TEMPLATES

# from string import Template


# COMMAND LINE ARGUMENTS

# import sys
print(sys.argv)

if len(sys.argv) == 1:
    print("not entered <password>")

else:
    password = sys.argv[1]
    print("Password: ", password)


# RUNNING EXTERNAL PROGRAMS

# import subprocess
# completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# completed = subprocess.run(
    # ["python_standard_library", "others.py"], capture_output=True, text=True)
try:

    completed = subprocess.run(
        ["false"], capture_output=True, text=True, check=True)
    # subprocess.call
    # subprocess.check_call
    # subprocess.check_output
    # subprocess.Popen

    print(completed.args)
    print(completed.returncode)
    print(completed.stderr)
    print(completed.stdout)

except subprocess.CalledProcessError as ex:
    print(ex)
