import csv
import random
import noiseFunctions

# TODO
# 1. Modularity of noise (noise dictionary, parametrize frequency and noise function)
# 2. "Golden ID" - ID per user, different profiles of users will have the same ID
# 3. Parametrize attributes of profiles
# 4. Parametrize percentage of shared attributes among all profiles

def readCSV(csv_file_name):
    output = []
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                output.append(row[0])
                line_count += 1
    return output

def generateData(attribute_file_dictionary, size):
    for key in attribute_file_dictionary:
        attribute_file_dictionary[key] = readCSV(attribute_file_dictionary[key])
    
    profiles = []
    index = 0
    while index < size:
        dict = {}
        for key in attribute_file_dictionary:
            attribute_data = attribute_file_dictionary[key]
            dict.update({key: attribute_data[random.randint(0, len(attribute_data) - 1)]})
        dict.update({'user_ID': index})
        profiles.append(dict)
        index += 1
    return profiles

def writeCSV(data, filename):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for element in data:
            writer.writerow(element)

def addNoise(data, noise_functions_dict, percentage_dict):
    for function in noise_functions_dict:
        noise_functions_dict[function](data, percentage_dict[function])

def main():
    pass

if __name__ == "__main__":
    main()