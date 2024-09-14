
''' This module will:
    -get data from various websites
    -save that information in a specified folder
    -then analyse that information and save it to a text file.


    
'''

#####################################
# Import modules
#####################################
import csv
import pathlib 

#import external library modules
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

#import local module
import utils_garrett



#####################################
# Define data acquisition functions
#####################################


def fetch_and_write_txt_data(folder_name: str, filename: str, url: str):
    '''
    This function gets text data from website and calls another function to save it.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        url(str)         - where data is being pulled from
    '''
    #get data from url
    response = requests.get(url)

    #test if get was successful, then call write function
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch text data: {response.status_code}")


def fetch_and_write_excel_data(folder_name: str, filename: str, url: str):
    '''
    This function gets excel data from website and calls another function to save it.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        url(str)         - where data is being pulled from
    '''
    #get data from url
    response = requests.get(url)

    #test if get was successful, then call write function
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")


def fetch_and_write_csv_data(folder_name: str, filename: str, url: str): 
    '''
    This function gets csv data from website and calls another function to save it.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        url(str)         - where data is being pulled from
    '''
    #get data from url
    response = requests.get(url)

    #test if get was successful, then call write function
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")


def fetch_and_write_json_data(folder_name: str, filename: str, url: str):
    '''
    This function gets json data from website and calls another function to save it.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        url(str)         - where data is being pulled from
    '''
    #request response from url, provide more infomation if it was not successful
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code
        json_data=response.content
        #call write function
        write_excel_file(folder_name, filename, json_data)
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")


#####################################
# Define data writing functions
#####################################

def write_txt_file(folder_name: str, filename: str, data: str):
    file_path = pathlib.Path(folder_name) 
    new_text_file=file_path / filename
    file_path.mkdir(exist_ok=True)
    with new_text_file.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name: str, filename: str, data: str):
    file_path = pathlib.Path(folder_name) 
    new_excel_file=file_path / filename
    file_path.mkdir(exist_ok=True)
    with open(new_excel_file, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_csv_file(folder_name: str, filename: str, data: str):
    file_path = pathlib.Path(folder_name) 
    new_csv_file=file_path / filename
    file_path.mkdir(exist_ok=True)
    with open(new_csv_file, 'wb') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name: str, filename: str, data: str):
    data=bytes(data)
    file_path = pathlib.Path(folder_name) 
    new_json_file=file_path / filename
    file_path.mkdir(exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f)
        print(f"CSV data saved to {file_path}")


#####################################
# Define processing functions
#####################################
def process_txt_file(folder_name: str,filename: str, output_filename: str):
    file_path = pathlib.Path(folder_name) / filename
    #read text file in
    file = open(file_path, "r")
    content = file.read()
    #analyse content of txt
    num_unique = len(content)  
    words = content.split()
    # Convert the string to lowercase for case-insensitive counting
    text = content.lower()
    num_words = len(words)  
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    # Count occurrences of the words "war" and "peace"
    war_count = text.count("war")
    peace_count = text.count("peace")

    # Prepare data for plotting
    words = ['War', 'Peace']
    counts = [war_count, peace_count]
    '''
    # Plotting
    plt.bar(words, counts, color=['red', 'blue'])
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title('Occurrences of "War" and "Peace"')
    plt.show()
    '''
    #save txt file results
    # Save the counts to a txt file
    new_text_file=pathlib.Path(folder_name) / output_filename
    with new_text_file.open('w') as file:
        file.write(f"Number of counts of war: {war_count}\n"
                   f"x{num_words}\n"
                   f"x{war_count}\n"
                   f"x{peace_count}")
        print(f"Text data saved to {file_path}")

def process_csv_file(csv_folder_name: str, filename: str, output_filename: str):
    file_path = pathlib.Path(csv_folder_name) / filename
    #read text file in
    file = open(file_path, "r")
    content = file.read()
    df = pd.read_csv(file_path)
    stats = df.describe()
    

    results_path = pathlib.Path(csv_folder_name) / output_filename
    with open(results_path, 'w') as file:
        file.write("Basic Statistical Analysis:\n")
        file.write(stats.to_string())
  
    print(f"Analysis saved to {output_filename}.")

def process_excel_file(excel_folder_name: str, filename: str, output_filename: str):
    file_path = pathlib.Path(excel_folder_name) / filename
    #read file in
    df = pd.read_excel(file_path)
    
    stats = df.describe()
    

    results_path = pathlib.Path(excel_folder_name) / output_filename
    with open(results_path, 'w') as file:
        file.write("Basic Statistical Analysis:\n")
        file.write(stats.to_string())
  
    print(f"Analysis saved to {output_filename}.")

def process_json_file(folder_name: str, filename: str, output_filename: str):
    file_path = pathlib.Path(folder_name) / filename
    #read file in
    df = pd.read_json(file_path)
    df = pd.DataFrame(df['data'])
    df = pd.json_normalize(df['data'])
    
    df = df[['year', 'Value']]
    stats=df['Value'].describe()
    #df = df.sort_values(by='year')
    df.to_csv('testdf.csv')

    

    results_path = pathlib.Path(folder_name) / output_filename
    with open(results_path, 'w') as file:
        file.write("Basic Statistical Analysis:\n")
        file.write(stats.to_string())
  
    print(f"Analysis saved to {output_filename}.")

#####################################
# Define a main() function for this module.
#####################################

#The main function calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
   # print(utils_garrett.get_byline())

    ''' Main function to demonstrate module capabilities. '''



    txt_url = 'https://www.gutenberg.org/cache/epub/2600/pg2600-images.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = "https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls"
    
    json_url = "https://quickstats.nass.usda.gov/api/api_GET/?key=9223C2A1-8766-311D-97E0-9C0777807BCE&source_desc=SURVEY&commodity_desc=CHICKENS&short_desc=CHICKENS, (EXCL BROILERS) - SALES FOR SLAUGHTER, MEASURED IN $&doman_desc=TOTAL&agg_level_desc=NATIONAL"
    
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')



#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
