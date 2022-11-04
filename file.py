import csv
import hashlib
import json
import pandas as pd
def convert():
    file_path=input(str('Enter your csv file path: '))
    json_path=input('Enter the file path to your created json file where you want the json to be generated:  ')
    data={}
    list=[]
    try:
        with open(file_path, encoding='utf-8') as csvf: 

            csvreader=csv.DictReader(csvf)
            for rows in csvreader:
                key= rows['Series Number']
                data[key]= rows
                Json_data=json.dumps(data, indent=4)
                j=hashlib.sha256(Json_data.encode('utf-8')).hexdigest()
                v=file_path+'.'+j+'.csv'
                list.append(v)
        try:
            with open(json_path, 'w') as json_file:
                print('generating json file......') 
                json_file.write(json.dumps(data, indent=4))
                print('completed') 
        except FileNotFoundError:
            print('This json file does not exist. please create a json file e.g file.json and input it')

        print('generating new csv file .....') 
        data_new= pd.read_csv(file_path)
        data_new['New']= list
        new='new_'+file_path
        data_new.to_csv(new)
        print('completed') 
        print('\nYour csv file is ready check->',new )
        print('\nYour json file is ready ->', json_path)
    except FileNotFoundError:
            print('This csv file does not exist')
  



convert()
