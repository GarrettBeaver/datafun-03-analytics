
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
import csv


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
        write_json_file(folder_name, filename, json_data)
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
    '''
    This function writes a text file.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        data(str)         - data to be written to file
    '''
    #create file path where data will be saved and save directory
    file_path = pathlib.Path(folder_name) 
    file_path.mkdir(exist_ok=True)
    
    #create new file name in correct folder
    new_text_file=file_path / filename
    
    #save data
    with new_text_file.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name: str, filename: str, data: str):
    '''
    This function writes an excel file.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        data(str)         - data to be written to file
    '''
    #create file path where data will be saved and save directory
    file_path = pathlib.Path(folder_name) 
    file_path.mkdir(exist_ok=True)

    #create new file name in correct folder
    new_file=file_path / filename
    
    #save data
    with open(new_file, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_csv_file(folder_name: str, filename: str, data: str):
    '''
    This function writes a csv file.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        data(str)        - data to be written to file
    '''
    #create file path where data will be saved and save directory
    file_path = pathlib.Path(folder_name) 
    file_path.mkdir(exist_ok=True)

    #create new file name in correct folder
    new_file=file_path / filename
    #save data
    with open(new_file, 'wb') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name: str, filename: str, data: str):
    '''
    This function writes an json file.
    Parameters for this function are:
        folder_name(str) - where file will be written
        filename(str)    - name of file to save
        data(str)         - data to be written to file
    '''
    #create file path where data will be saved and save directory
    file_path = pathlib.Path(folder_name) 
    file_path.mkdir(exist_ok=True)

    #create new file name in correct folder
    new_file=file_path / filename
    
    #save data
    with open(new_file, 'wb') as file:
        file.write(data)
        print(f"Json data saved to {file_path}")
    


#####################################
# Define processing functions
#####################################

def process_txt_file(folder_name: str,filename: str, output_filename: str):
    '''
    This function processes takes a text file, staticially analyzes it, creates a plot, and saves the results.

    Specfically in this example it will plot the number of occurances of the words "war" and "peace" in the book war and peace.
    Arguments:
        folder_name(str) - directory that information will be saved/retreved
        filename(str)    - name of file to analyzed
        output_filename(str)-name of results file
    '''
 
    #create file path of data to be opened
    file_path = pathlib.Path(folder_name) / filename

    #read text file in
    file = open(file_path, "r")
    content = file.read()

    #length of book
    num_unique = len(content)  

    #split book into words
    words = content.split()

    #count number of words
    num_words = len(words)  

    #find longest and shortest word
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    # Count occurrences of the words "war" and "peace"
    # Convert the string to lowercase
    text = content.lower()
    war_count = text.count("war")
    peace_count = text.count("peace")

    # Prepare data for plotting
    words = ['War', 'Peace']
    counts = [war_count, peace_count]
    
    # Plotting
    plt.bar(words, counts, color=['red', 'blue'])
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title('Occurrences of "War" and "Peace"')
    plt.show()
    
    #save txt file results
    new_text_file=pathlib.Path(folder_name) / output_filename
    with new_text_file.open('w') as file:
        file.write(f"Occurances of word war: {war_count}\n"
                   f"Occurances of word peace:{peace_count}\n"
                   f"Number of characters in book:{num_unique}\n"
                   f"Number of words:{num_words}\n"
                   f"Longest word:{longest_word}\n"
                   f"Shortest word:{shortest_word}\n")
        print(f"Analysis saved to {new_text_file}")

def process_csv_file(csv_folder_name: str, filename: str, output_filename: str):
    '''
    This function processes takes a csv file, staticially analyzes it, and saves the results.
    This function showcases the use of tuples and manipulating tablular data
    Arguments:
        csv_folder_name(str) - directory that information will be saved/retreved
        filename(str)    - name of file to analyzed
        output_filename(str)-name of results file
    '''
    #create directory where files will be read 
    file_path = pathlib.Path(csv_folder_name) / filename
    
    # Read the file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
 
        data = [tuple(row) for row in reader]
    
    #select specific column 
    ladder_score_error = [row[3] for row in data if len(row) > 1]
    #exclude header
    ladder_score_error = ladder_score_error[1:]

    #find average of ladder score error
    numbers=[]
    for score in ladder_score_error:
        number=float(score)
        numbers.append(number)
        ladder_score_error_average = sum(numbers) / len(numbers)


    #create path where results will be saved
    results_path = pathlib.Path(csv_folder_name) / output_filename
    #save results
    with open(results_path, 'w') as file:
        file.write("Basic Statistical Analysis:\n")
        file.write(f"Average of Ladder Score error is:{ladder_score_error_average}")
  
    print(f"Analysis saved to {output_filename}.")
    
def process_excel_file(excel_folder_name: str, filename: str, output_filename: str):
    '''
    This function processes takes an excel file, staticially analyzes it, and saves the results.

    Arguments:
        excel_folder_name(str) - directory that information will be saved/retreved
        filename(str)       - name of file to analyzed
        output_filename(str)-name of results file
    '''
    #create directory where files will be read and saved
    file_path = pathlib.Path(excel_folder_name) / filename

    #read file into a dataframe
    dataframe_of_excel = pd.read_excel(file_path)
    
    #analyse the dataframe information
    stats = dataframe_of_excel.describe()
    
    #save the results
    results_path = pathlib.Path(excel_folder_name) / output_filename
    with open(results_path, 'w') as file:
        file.write("Basic Statistical Analysis:\n")
        file.write(stats.to_string())
  
    print(f"Analysis saved to {output_filename}.")

def process_json_file(folder_name: str, filename: str, output_filename: str):
    '''
    This function processes takes a json file and saves it in a readable format.

    Arguments:
        folder_name(str)    - directory that information will be saved/retreved
        filename(str)       - name of file to analyzed
        output_filename(str)-name of results file
    '''
    #create folder path
    file_path = pathlib.Path(folder_name) / filename
    #open json file as a dictionary
    with file_path.open('r', encoding='utf-8') as file:
        json_data = json.load(file)

    #create new output path
    output_file_path = pathlib.Path(folder_name) / output_filename
    #save in readable format
    with open(output_file_path, 'w') as file:
        json.dump(json_data, file, indent=4, sort_keys=True)

#####################################
# Define a main() function for this module.
#####################################

#The main function calls get_byline() to retrieve the byline.
def main() -> None:
    '''Main function to demonstrate all features of module
    '''
    #print byline as demonstration
    print(utils_garrett.get_byline())


    #urls where data is being pulled
    txt_url = 'https://www.gutenberg.org/cache/epub/2600/pg2600-images.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = "https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls"
    
    json_url = "https://quickstats.nass.usda.gov/api/api_GET/?key=9223C2A1-8766-311D-97E0-9C0777807BCE&source_desc=SURVEY&commodity_desc=CHICKENS&short_desc=CHICKENS, (EXCL BROILERS) - SALES FOR SLAUGHTER, MEASURED IN $&doman_desc=TOTAL&agg_level_desc=NATIONAL"
    
    #folder name where each data type will be saved
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    #name of file where each data type will be saved
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    #call fetch and write functions
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    #once data is collected, save statistical results
    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')



#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
