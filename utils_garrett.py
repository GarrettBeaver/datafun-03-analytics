''' ITERATION 5

Module: Beaver Analytics - Making Data Fun!

This module displays the byline of an analytics company.  Features of the company are listed, 
then the min, max, mean, and standard deviation are calculated and displayed in the byline. 
'''

#####################################
# Import modules
#####################################
import statistics


#####################################
# Declare global variables
#####################################

#Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

#Integer variable for the number of years in operation
years_in_operation: int = 10

#list of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

#List of floats representing individual client statisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#Additional boolean variable - comapny offers satisfaction guarantee
satisfaction_guarantee: bool = True

#Additional integer - total number of clients served in company history
clients_served: int = 400

#Addition list of strings - list of core company values
core_company_values: list = ["Integrity", "Dependability", "Trustworthy"]

#Additional list of floats - leadtimes of last projects completed in days
project_leadtimes: list = [10, 20, 15, 15, 18]

#####################################
# Calculate Basic Statistics
#####################################
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_leadtime: float = min(project_leadtimes)
max_leadtime: float = max(project_leadtimes)
mean_leadtime: float = statistics.mean(project_leadtimes)
stdev_leadtime: float = statistics.stdev(project_leadtimes)


####################################
#Declare a global variable named byine
#Make it a multiline f-string 
####################################

byline: str = f"""
------------------------------------
'Beaver Analytics: Making Data Fun!'
------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Sattisfaction Score:   {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}

Satisfaction Guarantee:     {satisfaction_guarantee}
Number of CLients Served:   {clients_served}
Company Core Values:        {core_company_values}
Project Lead Times(days):   {project_leadtimes}
Minimum Lead Time: {min_leadtime}
Maximum Lead Time: {max_leadtime}
Mean Lead Time:   {mean_leadtime:.2f}
Standard Deviation of Lead Time: {stdev_leadtime:.2f}
"""

#####################################
#Define the get_byline() function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

#The main function calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
