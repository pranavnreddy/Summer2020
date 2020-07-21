import dataGen as dg
import noiseFunctions as nf

def printFormat(data):
    for x in data:
        print(x)

def testReadCSV():
    print('testReadCsv: '+ str(len(dg.readCSV('first_names.csv')) == 27491))

def testGenerateData():
    af_dict = {
        'first_name':'first_names.csv',
        'last_name':'last_names.csv',
        'street_name':'street_names.csv',
        'street_number':'street_numbers.csv'
    }
   #printFormat(dg.generateData(af_dict, 10))

def testSwapNames():
    data = [{'first_name': 'Brenda', 'last_name': 'SHONKA', 'street_name': 'CORDOVA ST', 'street_number': '8', 'user_ID': 0},
            {'first_name': 'Hanna', 'last_name': 'BASNER', 'street_name': 'GATEVIEW CT', 'street_number': '250', 'user_ID': 1},
            {'first_name': 'Jacqueline', 'last_name': 'MIZRAHI', 'street_name': 'GRIFFITH ST', 'street_number': '9', 'user_ID': 2},
            {'first_name': 'LORENZO', 'last_name': 'GEARLDS', 'street_name': 'BURNETT AVE NORTH', 'street_number': '5', 'user_ID': 3},
            {'first_name': 'JORDYN', 'last_name': 'ANGELOV', 'street_name': 'BIRCH ST', 'street_number': '8', 'user_ID': 4},
            {'first_name': 'BIANCA', 'last_name': 'FILIPPOV', 'street_name': 'DAVIS ST', 'street_number': '32', 'user_ID': 5},
            {'first_name': 'MACKENZIE', 'last_name': 'DICOB', 'street_name': 'PELICAN COVE TER', 'street_number': '150', 'user_ID': 6},
            {'first_name': 'Marc', 'last_name': 'CORANADO', 'street_name': 'PARK PRESIDIO BYPASS DR', 'street_number': '26', 'user_ID': 7},
            {'first_name': 'MOHAMMED', 'last_name': 'CARTAGENA', 'street_name': 'OPHIR ALY', 'street_number': '50', 'user_ID': 8},
            {'first_name': 'Layla', 'last_name': 'MANTHEY', 'street_name': 'BADEN ST', 'street_number': '628', 'user_ID': 9}]

    nf.swapNames(data, 0.5)
    printFormat(data)

def testInitialFirstName():
    data = [{'first_name': 'Brenda', 'last_name': 'SHONKA', 'street_name': 'CORDOVA ST', 'street_number': '8', 'user_ID': 0},
            {'first_name': 'Hanna', 'last_name': 'BASNER', 'street_name': 'GATEVIEW CT', 'street_number': '250', 'user_ID': 1},
            {'first_name': 'Jacqueline', 'last_name': 'MIZRAHI', 'street_name': 'GRIFFITH ST', 'street_number': '9', 'user_ID': 2},
            {'first_name': 'LORENZO', 'last_name': 'GEARLDS', 'street_name': 'BURNETT AVE NORTH', 'street_number': '5', 'user_ID': 3},
            {'first_name': 'JORDYN', 'last_name': 'ANGELOV', 'street_name': 'BIRCH ST', 'street_number': '8', 'user_ID': 4},
            {'first_name': 'BIANCA', 'last_name': 'FILIPPOV', 'street_name': 'DAVIS ST', 'street_number': '32', 'user_ID': 5},
            {'first_name': 'MACKENZIE', 'last_name': 'DICOB', 'street_name': 'PELICAN COVE TER', 'street_number': '150', 'user_ID': 6},
            {'first_name': 'Marc', 'last_name': 'CORANADO', 'street_name': 'PARK PRESIDIO BYPASS DR', 'street_number': '26', 'user_ID': 7},
            {'first_name': 'MOHAMMED', 'last_name': 'CARTAGENA', 'street_name': 'OPHIR ALY', 'street_number': '50', 'user_ID': 8},
            {'first_name': 'Layla', 'last_name': 'MANTHEY', 'street_name': 'BADEN ST', 'street_number': '628', 'user_ID': 9}]

    nf.initialFirstName(data, 0.5)
    printFormat(data)

def testDeleteAttribute():
    data = [{'first_name': 'Brenda', 'last_name': 'SHONKA', 'street_name': 'CORDOVA ST', 'street_number': '8', 'user_ID': 0},
            {'first_name': 'Hanna', 'last_name': 'BASNER', 'street_name': 'GATEVIEW CT', 'street_number': '250', 'user_ID': 1},
            {'first_name': 'Jacqueline', 'last_name': 'MIZRAHI', 'street_name': 'GRIFFITH ST', 'street_number': '9', 'user_ID': 2},
            {'first_name': 'LORENZO', 'last_name': 'GEARLDS', 'street_name': 'BURNETT AVE NORTH', 'street_number': '5', 'user_ID': 3},
            {'first_name': 'JORDYN', 'last_name': 'ANGELOV', 'street_name': 'BIRCH ST', 'street_number': '8', 'user_ID': 4},
            {'first_name': 'BIANCA', 'last_name': 'FILIPPOV', 'street_name': 'DAVIS ST', 'street_number': '32', 'user_ID': 5},
            {'first_name': 'MACKENZIE', 'last_name': 'DICOB', 'street_name': 'PELICAN COVE TER', 'street_number': '150', 'user_ID': 6},
            {'first_name': 'Marc', 'last_name': 'CORANADO', 'street_name': 'PARK PRESIDIO BYPASS DR', 'street_number': '26', 'user_ID': 7},
            {'first_name': 'MOHAMMED', 'last_name': 'CARTAGENA', 'street_name': 'OPHIR ALY', 'street_number': '50', 'user_ID': 8},
            {'first_name': 'Layla', 'last_name': 'MANTHEY', 'street_name': 'BADEN ST', 'street_number': '628', 'user_ID': 9}]

    for element in data:
        if element['user_ID'] == '':
            raise Exception('user id missing')

    nf.deleteAttribute(data, 0.5)
    printFormat(data)

def testShareAttributes():
    data = [{'first_name': 'Brenda', 'last_name': 'SHONKA', 'street_name': 'CORDOVA ST', 'street_number': '8', 'user_ID': 0},
            {'first_name': 'Hanna', 'last_name': 'BASNER', 'street_name': 'GATEVIEW CT', 'street_number': '250', 'user_ID': 1},
            {'first_name': 'Jacqueline', 'last_name': 'MIZRAHI', 'street_name': 'GRIFFITH ST', 'street_number': '9', 'user_ID': 2},
            {'first_name': 'LORENZO', 'last_name': 'GEARLDS', 'street_name': 'BURNETT AVE NORTH', 'street_number': '5', 'user_ID': 3},
            {'first_name': 'JORDYN', 'last_name': 'ANGELOV', 'street_name': 'BIRCH ST', 'street_number': '8', 'user_ID': 4},
            {'first_name': 'BIANCA', 'last_name': 'FILIPPOV', 'street_name': 'DAVIS ST', 'street_number': '32', 'user_ID': 5},
            {'first_name': 'MACKENZIE', 'last_name': 'DICOB', 'street_name': 'PELICAN COVE TER', 'street_number': '150', 'user_ID': 6},
            {'first_name': 'Marc', 'last_name': 'CORANADO', 'street_name': 'PARK PRESIDIO BYPASS DR', 'street_number': '26', 'user_ID': 7},
            {'first_name': 'MOHAMMED', 'last_name': 'CARTAGENA', 'street_name': 'OPHIR ALY', 'street_number': '50', 'user_ID': 8},
            {'first_name': 'Layla', 'last_name': 'MANTHEY', 'street_name': 'BADEN ST', 'street_number': '628', 'user_ID': 9}]

    nf.shareAttributes(data, 0.5)
    printFormat(data)

def testSameProfiles():
    data = [{'first_name': 'Brenda', 'last_name': 'SHONKA', 'street_name': 'CORDOVA ST', 'street_number': '8', 'user_ID': 0},
            {'first_name': 'Hanna', 'last_name': 'BASNER', 'street_name': 'GATEVIEW CT', 'street_number': '250', 'user_ID': 1},
            {'first_name': 'Jacqueline', 'last_name': 'MIZRAHI', 'street_name': 'GRIFFITH ST', 'street_number': '9', 'user_ID': 2},
            {'first_name': 'LORENZO', 'last_name': 'GEARLDS', 'street_name': 'BURNETT AVE NORTH', 'street_number': '5', 'user_ID': 3},
            {'first_name': 'JORDYN', 'last_name': 'ANGELOV', 'street_name': 'BIRCH ST', 'street_number': '8', 'user_ID': 4},
            {'first_name': 'BIANCA', 'last_name': 'FILIPPOV', 'street_name': 'DAVIS ST', 'street_number': '32', 'user_ID': 5},
            {'first_name': 'MACKENZIE', 'last_name': 'DICOB', 'street_name': 'PELICAN COVE TER', 'street_number': '150', 'user_ID': 6},
            {'first_name': 'Marc', 'last_name': 'CORANADO', 'street_name': 'PARK PRESIDIO BYPASS DR', 'street_number': '26', 'user_ID': 7},
            {'first_name': 'MOHAMMED', 'last_name': 'CARTAGENA', 'street_name': 'OPHIR ALY', 'street_number': '50', 'user_ID': 8},
            {'first_name': 'Layla', 'last_name': 'MANTHEY', 'street_name': 'BADEN ST', 'street_number': '628', 'user_ID': 9}]

    nf.sameProfiles(data, 0.5)
    printFormat(data)

def testWhole():
    af_dict = {
        'first_name':'first_names.csv',
        'last_name':'last_names.csv',
        'street_name':'street_names.csv',
        'street_number':'street_numbers.csv'
    }

    noise_functions = {
        'swapNames': nf.swapNames,
        'initialFirstName':nf.initialFirstName,
        'initialLastName':nf.initialLastName,
        'deleteAttribute':nf.deleteAttribute,
        'shareAttributes':nf.shareAttributes,
        'sameProfiles':nf.sameProfiles,
    }

    noise_function_percentages = {
        'swapNames': 0.05,
        'initialFirstName':0.1,
        'initialLastName':0.05,
        'deleteAttribute':0.05,
        'shareAttributes':0.3,
        'sameProfiles':0.8
    }

    profiles = dg.generateData(af_dict, 200)

    dg.addNoise(profiles, noise_functions, noise_function_percentages)

    dg.writeCSV(profiles, "noisyv2.csv")


def main():
    #testReadCSV()
    #testGenerateData()
    #testInitialFirstName()
    #testDeleteAttribute()
    #testShareAttributes()
    #testSameProfiles()
    testWhole()

if __name__ == "__main__":
    main()