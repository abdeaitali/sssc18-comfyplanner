########################
### MAIN PROGRAM
########################

### IMPORTS
import sys
from plan import get_siteid # get station id from name
from plan import get_tripList # get trip ref from pair of station id

from deviation import test_for_deviations
#RESULTS = []
def main(departure_station, arrival_station):
    RESULTS = []
    ## Abdou's key
    KEY_PLANNER = 'b3c091d5ffdf49d2b2bfaea153c905d9'
    KEY_LOCATER = 'cf745532e18d426f8f3a40933f2fbc51'
    
    ### INPUT
    #departure_station = "Solna Centrum"
    #arrival_station = "Tekniska högskolan"
    #departure_station = sys.argv[1]
    #arrival_station   = sys.argv[2]
    
    ### TRIP Planner 4.0
    # get id of stations
    depId=get_siteid(departure_station,KEY_LOCATER)
    arrId=get_siteid(arrival_station,KEY_LOCATER)
    
    # get list of trips
    tripList=get_tripList(depId,arrId, KEY_PLANNER)
    tripListNoDeviation = list()
    tripsNoDeviation = test_for_deviations(tripList)
    
    ### RESULTS (as a list of journeys without deviations)
    #print(tripsNoDeviation)
    
    if len(tripsNoDeviation)==0:
        RESULTS.append("We are sorry, but there are no routes without deviations for you. \nThis route works, but might be a bit crowded:\n")
        #print(tripList[0]['LegList']['Leg'])
        for j in tripList[0]['LegList']['Leg']:
            if j['type']=='WALK':
                RESULTS.append(str('Transfer from '+j['Origin']['name']+' to '+j['Destination']['name'] + '\n'))
            else:    
                RESULTS.append(str("With: " + j['Product']['name'] + '\n' \
                    +  "From: " + j['Origin']['name']  + '\n' \
                    +  "To: " + j['Destination']['name'] + '\n'))
            if j['Destination']['name'].lower() == arrival_station.lower():
                break
            """print("With: "+ j[0]['name'])
            print("From: "+ j[0]['Origin']['name'])
            print("To: "+ j[0]['Destination']['name'])"""
    else:
        RESULTS.append(str("We found a comfortable trip for you!\n"))
        #print("We found a comfortable trip for you!")
        #for i in tripsNoDeviation:
        """print("With: "+ tripsNoDeviation[0]['name'])
        print("From: "+ tripsNoDeviation[0]['Origin']['name'])
        print("To: "+ tripsNoDeviation[0]['Destination']['name'])"""
        #print(len(tripsNoDeviation))
        for i in tripsNoDeviation[0]:
            if i['type']=='WALK':
                RESULTS.append(str('Transfer from '+i['Origin']['name']+' to '+i['Destination']['name']+'\n'))
            else:    
                RESULTS.append(str("With: "+ i['Product']['name'] + '\n' \
                     + "From: "+ i['Origin']['name']  +  '\n' \
                     + "To: " + i['Destination']['name']+'\n'))
            if i['Destination']['name'].lower() == arrival_station.lower():
                break
    # output one random tripsNoDeviation
    return(''.join(RESULTS))

if __name__ == '__main__':
    main()

