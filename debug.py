import os

def parse_csv(csv_file):
    """Parse a CSV file and return the data in a list of lists"""
    with open(csv_file, 'r') as file:
      return [line.strip().split(',') for line in file.readlines()]


def count_males_from_titanic(data):
    """Count the number of people from France in the data"""
    return len([row for row in data if row[5] == 'male'])
    
if __name__ == "__main__":
    print("## Welcome to CSV Parser Crew")
    print('-------------------------------')
    print("## Let's start the process")
    path_str = "./titanic.csv"
    path = os.path.normpath(path_str)

    data = parse_csv(path)
    result = count_males_from_titanic(data)
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)

