import csv

class FileReader:
    
    def __init__(self):
        pass
    
    def file_read():
        with open('task_list.csv', 'r', newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for i in reader:
                data.append(i)
            return data
    
    def write_file(data):
        with open('task_list.csv', 'w', newline = '') as csvfile:
            fieldnames = ['Task name','Description','Due date','Priority','Status','Creation date']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for i in data:
                writer.writerow(i)

        