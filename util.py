import base64
import csv
import os

def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def check_file(path):
    try:
        with open(path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            # TODO: Read content
            global jobs_data
            jobs_data = []
            for row in reader:
                job = []
                for i in range(1, len(row) - 1):
                    if is_number(row[i]):
                        if i % 2 == 1:
                            job.append((int(row[i]), int(row[i + 1])))
                # print(job)
                jobs_data.append(job)
    except:
        print("Error! Check the template file")
        return 1
    return 0

def save_file(name, content, location):
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(location, name), "wb") as fp:
        fp.write(base64.decodebytes(data))
    return check_file(os.path.join(location, name))