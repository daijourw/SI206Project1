# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:09:52 2021

@author: ashbu
"""

# Your name: Daijour Williams
# Your student id: 49521451
# Your email: daijourw@umich.edu
# List who you have worked with on this project: Collaborated with students at office hours, Jasper, and recieved help during office hours.

import io
import sys
import csv
import unittest
from unittest.case import skip
          

def read_csv(file):
    '''
    Function to read in a CSV

    Parameters
    ----------
    file : string
        the name of the file you're reading in

    Returns
    -------
    data_dict : dict
        the double-nested dictionary that holds the data from the csv.

    '''
    
    data_dict = {}
    row_count =  1
    
    # write your code here that does things
    # it should read in the lines of data
    # it should also seperate the first row as header information
    # at the same time, it should grab the first item as the state information
    # the end result of the data should be formated like so
    # ex: (ap_dict) {“Alabama”: {“AMERICAN INDIAN/ALASKA NATIVE”: 1, “ASIAN”: 61,...},...}

    fl = open(file,"r")
    lines = fl.readlines()
    fl.close
    
    lines[0] = lines[0].strip()
    header = lines[0].split(',')


    for line in lines[1:]:
        line = line.strip()
        lst = line.split(',')
        state_dict = {}
        for indx in range(1,len(lst)):
            state_dict[header[indx]] = int(lst[indx])
        data_dict[lst[0]] = state_dict
    
    return data_dict


def pct_calc(data_dict):
    '''
    Function to compute demographic percentages
    Parameters
    ----------
    data_dict : dict
        the dictionary you're passing in. Should be the data dict from the 
        census or AP data. 

    Returns
    -------
    pct_dict: dict
        the dictionary that represents the data in terms of percentage share 
        for each demographic for each state in the data set.
    '''
    
    # declaring dict to hold pct vals
    pct_dict = {}

    # write in code here
    # it should take the number for each demographic for each state and divide it by the state total column
    # ex: value = ensus_data["Alabama"]["WHITE]/census_data["Alabama]["State Totals"]
    # ex: round(value * 100, 2))      
    for state in data_dict:
        dict_ethn = {}
        for ethn in data_dict[state]:
            if ethn != 'State Totals':
                # dict_ethn = {}
                #print(data_dict[state][ethn])
                #print(data_dict[state]['State Totals'])
                num1 = float(data_dict[state][ethn])
                num2 = float(data_dict[state]['State Totals'])
                # print(num1)
                # print(num2)
                #prop = (int(data_dict[state][ethn]))/(int(data_dict[state]['State Totals']))
                prop = num1/num2
                #print(prop)
                pct = round(prop*100,2)
                dict_ethn[ethn] = pct
        pct_dict[state] = dict_ethn
    pass
    # print(len(pct_dict))
    return(pct_dict)


def pct_dif(data_dict1, data_dict2):
    '''
    Function to compute the difference between the demographic percentages

    Parameters
    ----------
    data_dict1 : dict
        the first data_dict you pass in. In this case, the ap_data
    data_dict2 : dict
        the second data_dict you pass in. In this case, the census_data

    Returns
    -------
    pct_dif_dict: dict
        the dictionary of the percent differences.
    '''
    
    pass
    
    # creating the dictionary to hold the pct diferences for each "cell"
    pct_dif_dict = {}
    
    # write code here
    # it should subtract the % val of each val in the 2nd dict from the 1st dict
    # it should take the absolute value of that difference and round it to 2 decimal places
    # ex: value = ap_data["Alabama"]["WHITE] - census_data["Alabama"]["WHITE] 
    # ex: abs(round(value, 2))
    # hint: you want to have a way to deal with the difference in naming conventions
    # ex: "North Carolina" vs "North-Carolina" string.replace is your friend
    # pct_1 = pct_calc(data_dict1)
    # pct_2 = pct_calc(data_dict2)
    # print(pct_1)
    # print(data_dict1)
    # print(data_dict2)
    for state in data_dict1.keys():
        dif_dict = {}
        if state == 'State Totals' or state == 'NO RESPONSE':
            continue
        else:
            for ethn in data_dict1[state]:
                if ethn != 'NO RESPONSE':
                    #print(data_dict1[state][ethn])
                    #print(data_dict2[state])
                    dict1 = data_dict1[state][ethn] 
                    dict2 = data_dict2[state.replace("-"," ")][ethn]
                    dif = dict1 - dict2
                    dif_dict[ethn] = abs(dif)
        pct_dif_dict[state] = dif_dict
    pass
    return(pct_dif_dict)

def csv_out(data_dict, file_name):
    '''
    Function to write output to a file    

    Parameters
    ----------
    data_dict : dict
        the data dictionary you are writing to the file. In this case, 
        the result from pct_dif_dict
        
    file_name : str
        the name of the file you are writing.

    Returns
    -------
    None. (Doesn't return anything)
    '''
    row_count = 0
    with open(file_name, "w") as fileout:
        header = ["State"] + list(data_dict["Alabama"].keys())
        header = ','.join(header)
        fileout.write(header+'\n')
        for item in data_dict:
            line = list(data_dict[item].values())
            line = str(line)[1:-1]
            fileout.write(item+','+line+'\n')
        pass
        return None




    # with open(file_name, "w", newline="") as fileout:

        # writer = csv.writer(fileout)

        # header = ["State"] + list(data_dict["Alabama"].keys())
        # #writer.writerow(header)
        # print(header)

        # for state in data_dict:
        #     rowlst = []
        #     rowlst.append(state)
        #     for ethn in state:
        #        rowlst.append(data_dict[state][ethn])
        #     print(rowlst)
            #writer.writerow(rowlst)

        # you'll want to write the rest of the code here
        # you want to write the header info as the first row 
        # you want to then write each subsequent row of data 
        # the rows will look like this
        # ex: Alabama,0.2,18.32,21.16,2.17,0.05,3.58,1.98,1.45
        #pass
            
def max_min_mutate(data_dict, col_list):
    # Do not change the code in this function
    '''
    function to mutate the data to simplify sorting

    Parameters
    ----------
    data_dict : dict
        dictionary of data passed in. In this case, it's the 
    col_list : list
        list of columns to mutate to.

    Returns
    -------
    demo_vals: dict
        DESCRIPTION.

    '''
    # Do not change the code in this function
    demo_vals = {}
    
    for demo in col_list:
        demo_vals.setdefault(demo, {})
        
        for state in data_dict:
            demo_vals[demo].setdefault(state, data_dict[state][demo])
    pass 
    return(demo_vals)

def max_min(data_dict):
    '''
    function to find the 5 max and min states & vals for each demographic

    Parameters
    ----------
    data_dict : dict
        the data_dictionary you're passing in. In this case, the mutated dict

    Returns
    -------
    max_min: 
        a triple nested dict with the this basic format
        {"max":{demographic:{"state":value}}}
    '''
    max_min = {"max":{},"min":{}}
    # for item in data_dict:
    #     print(data_dict[item]
        #item = race
        #data_dict[item]
    ethmax = {}
    ethmin = {}
    for item in data_dict.keys():
        max_min['max'].setdefault(item, {})
        max_min['min'].setdefault(item,{})

        for eth in max_min['max']:
            maxlst = sorted(data_dict[eth].items(),key =lambda x: x[1], reverse = True)
            max_5 = maxlst[:5]
            maxx = dict(max_5)
        ethmax[eth] = maxx
        for eth in max_min['min']:
            minlst = sorted(data_dict[eth].items(),key = lambda x: x[1])
            min_5 = minlst[:5]
            minn = dict(min_5)
        ethmin[eth] = minn
    max_min = {'max':ethmax, 'min':ethmin}
    pass
    return max_min


    
    # fill out the code in between here
    # you'll want to make code to fill the dictionary
    # the second inner layer will look like {"max":{demographic:{}}
    # the innermost layer will look like {demographic:{"state":value}}
    
    # printing and returning the data
    #print(max_min)

    #pass
    #return(max_min)

def nat_pct(data_dict, col_list):
    '''
    EXTRA CREDIT
    function to calculate the percentages for each demographic on natl. level    

    Parameters
    ----------
    data_dict : dict
        the data dictionary you are passing in. Either AP or Census data
    col_list : list
        list of the columns to loop through. helps filter out state totals cols

    Returns
    -------
    data_dict_totals
        dictionary of the national demographic percentages

    '''
    data_dict_totals = {}
    
    # fill out code here
    # you'll want to add the demographics as the outerdict keys
    # then you'll want to cycle through the states in the data dict
    # while you're doing that, you'll be accumulating the totals for each demographic
    # you'll then convert each value to a demographic percentage
    # finally, you'll return the dictionary
    result = dict.fromkeys(col_list, 0)
    for state in data_dict:
        #print(state)
        for ethn in data_dict[state]:
            # print(ethn)
            # if ethn == 'State Totals':
            #     result[ethn] += int(data_dict[state][ethn])
            if ethn == 'NO RESPONSE':
                continue
            else:
                result[ethn] += int(data_dict[state][ethn])
    for ethn in result:
        if ethn == 'State Totals':
            continue
        else:
            pct = (int(result[ethn])/int(result['State Totals']))*100
            result[ethn] = pct
                                        
    return(data_dict_totals)
        
def nat_dif(data_dict1, data_dict2):
    '''
    EXTRA CREDIT
    function to calculate the difference on the national level

    Parameters
    ----------
    data_dict1 : dict
        the first data dict you are passing in
    data_dict2 : dict
        the 2nd data dict you are passing in.

    Returns
    nat_dif: dict
        the dictionary consisting of the demographic difference on natl. level
    
    '''
    result = {}
    # fill out code here
    for ethn in data_dict1:
        if ethn == 'State Totals':
            continue
        else:
            difference = int(data_dict1[ethn]) - int(data_dict2[ethn])
            result[ethn] = difference

    # you'll want to remove the state totals 
    # then you'll want to loop through both dicts and find the differences
    # finally, you'll want to return those differences
    return(result)
             
def main():
    # reading in the data
    ap_data = read_csv("ap_cleaned.csv")
    census_data = read_csv("census_cleaned.csv")
    
    # computing demographic percentages
    ap_pct = pct_calc(ap_data)
    census_pct = pct_calc(census_data)
    
    # computing the difference between test taker and state demographics
    pct_dif_dict = pct_dif(ap_pct, census_pct)
    
    # outputing the csv
    csv_out(pct_dif_dict, "HW5V1.csv")
        
    # creating a list from the keys of inner dict
    col_list = list(pct_dif_dict["Alabama"].keys())
    
    # mutating the data
    mutated = max_min_mutate(pct_dif_dict, col_list)
    
    # finding the max and min vals
    max_min_vals = max_min(mutated)
        
    # extra credit
    # providing a list of col vals to cycle through
    col_list = census_data["Alabama"].keys()
    
    # computing the national percentages
    ap_nat_pct = nat_pct(ap_data, col_list)
    census_nat_pct = nat_pct(census_data, col_list)    
    
    print(ap_nat_pct)
    print(census_nat_pct)
    
    # computing the difference between them
    dif = nat_dif(ap_nat_pct, census_nat_pct)
        
    print("Difference between AP Comp Sci A and national demographics:\n",
          dif)
        
main()

# unit testing
# Don't touch anything below here
class HWTest(unittest.TestCase):
    
    def setUp(self):
        # surpressing output on unit testing
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        
        # setting up the data we'll need here
        # basically, redoing all the stuff we did in the main function
        self.ap_data = read_csv("ap_cleaned.csv")
        self.census_data = read_csv("census_cleaned.csv")
        
        self.ap_pct = pct_calc(self.ap_data)
        self.census_pct = pct_calc(self.census_data)
        
        self.pct_dif_dict = pct_dif(self.ap_pct, self.census_pct)
        
        self.col_list = list(self.pct_dif_dict["Alabama"].keys())

        self.mutated = max_min_mutate(self.pct_dif_dict, self.col_list)
        
        self.max_min_val = max_min(self.mutated)
        
        # extra credit
        # providing a list of col vals to cycle through
        self.col_list = self.census_data["Alabama"].keys()
        
        # computing the national percentages
        self.ap_nat_pct = nat_pct(self.ap_data, self.col_list)
        self.census_nat_pct = nat_pct(self.census_data, self.col_list)    
        
        self.dif = nat_dif(self.ap_nat_pct, self.census_nat_pct)
        
    # testing the csv reading func is working properly
    def test_read_csv(self):
         test = read_csv("ap_cleaned.csv")
        
         self.assertEqual(test["Alabama"]["ASIAN"], 61)
         
    # testing the pct_calc function
    def test_pct_calc(self):
        self.assertEqual(pct_calc({"state":{"demo":5,"State Totals":10}}), 
                         {"state":{"demo": 50.0}})

    # second test on the pct_calc function
    # fails because my value is wrong (doh!)
    def test2_pct_calc(self):
        self.assertEqual(
            self.ap_pct["Alabama"]["ASIAN"], 
            19.68)

    # testing the pct_dif function
    def test_pct_dif(self):
        self.assertEqual(
            pct_dif({"state":{"demo":50.0}},{"state":{"demo":50.0}}),
            {'state': {'demo': 0.0}}           
            )
        
    # second test on the pct_dif function
    # needs a valid value though brah
    def test2_pct_dif(self):
        self.assertEqual(
            self.pct_dif_dict["Alabama"]["AMERICAN INDIAN/ALASKA NATIVE"],
            0.2)
    
    # testing the max_min function
    def test_max_min(self):
        self.assertEqual(
            max_min({"demo":{"a":1,"b":2,"c":3,"d":4,"e":5}})
            ,
            {'max': {'demo': {'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1}},
             'min': {'demo': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}}}
            )
        
    # second test on the max_min function
    def test2_max_min(self):
        self.assertEqual(
            self.max_min_val["max"]["BLACK"]["District-of-Columbia"],
            23.92)
    
    # testing the nat_pct extra credit function
    def test_nat_pct(self):
       self.assertEqual(
       nat_pct({"state":{"demo":5,"State Totals":10}},["demo", "State Totals"]),
       {"demo":50.0, "State Totals":10})
        
    # second test for the nat_pct extra credit function
    def test2_nat_pct(self):
        self.assertEqual(
            self.ap_nat_pct["AMERICAN INDIAN/ALASKA NATIVE"], 
            0.29)
    
    # testing the nat_dif extra credit function
    def test_nat_dif(self):
        self.assertEqual(
            nat_dif({"demo":0.53, "State Totals": 1},{"demo":0.5, "State Totals": 1}),
            {"demo":0.03}
            )
     
    # second test for the nat_dif extra credit function
    def test2_nat_dif(self):
        self.assertEqual(
            self.dif["ASIAN"],
            27.93)

if __name__ == '__main__':
    unittest.main(verbosity=2)






        

