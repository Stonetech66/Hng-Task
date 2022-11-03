import csv
import hashlib
import json
import pandas as pd
def convert():
    file_path=input(str('Enter your csv file path: '))
    json_path=input('Enter the file path to your created json file where you want the json to be generated:  ')
    index_field=input('Enter the first header parameter on the first row of your csv file. i.e enter the first word in your csv file e.g Serial_No \nEnter here: ')
    data={}
    list=[]
    try:
        with open(file_path, encoding='utf-8') as csvf: 

            csvreader=csv.DictReader(csvf)
            for rows in csvreader:
                key= rows[index_field]
                data[key]= rows
                Json_data=json.dumps(data, indent=4)
                j=hashlib.sha256(Json_data.encode('utf-8')).hexdigest()
                v=file_path+'.'+j+'.csv'
                list.append(v)
        try:
            with open(json_path, 'w') as json_file:
                json_file.write(json.dumps(data, indent=4))
        except FileNotFoundError:
            print('This json file does not exist. please create a json file e.g file.json and input it')

      
        data_new= pd.read_csv(file_path)
        data_new['New']= list
        new='new_'+file_path
        data_new.to_csv(new)
        print('\nYour csv file is ready check->',new )
        print('\nYour json file is ready ->', json_path)
    except FileNotFoundError:
            print('This file does not exist')
    except KeyError:
        print('The first Header parameter entered is incorrect. Enter the first word you see in your csv file')
    



convert()
