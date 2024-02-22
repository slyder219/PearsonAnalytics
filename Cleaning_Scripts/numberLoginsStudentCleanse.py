import pandas as pd
from datetime import datetime
import json 


def time_to_seconds(time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds

def numLoginsCleanse(dataFilePath, outputFilePath):
    df = pd.read_csv(dataFilePath)

    # empty list to store student data
    newData = []

    # iter through each row
    for index, row in df.iterrows():

        # check if we have header table, if so then grab header info 
        if "BITM" in row["Section"]:
            data = {
                "StudentID": row["StudentNumber"],
                "AvgNumLogins": row["Average number of logins"].strip(),
                "NumSubmissions": row["Number of student submissions"].strip(),
                "TotalCourseTime": row["Total Time in Course"].strip(),
                "TotalLogins": row["Total Logins"].strip(),
                "LastLogin": row["Last Login"].strip(),
                "EnrollmentDate": row["Enrollment Date"].strip(),
                "Instructor": row["Instructor"].strip(),
                "Section": row["Section"].strip() }
            
            # add all that data to list 
            newData.append(data)
    
    # Create a new DataFrame from the list of dictionaries
    new_df = pd.DataFrame(newData)

    # add new columnt total_course_time_seconds
    new_df['TotalCourseTimeSeconds'] = new_df['TotalCourseTime'].apply(time_to_seconds)

    # convert that to integers
    new_df['TotalCourseTimeSeconds'] = new_df['TotalCourseTimeSeconds'].astype(int)

    # convert total logins column to integers
    new_df['TotalLogins'] = new_df['TotalLogins'].astype(int)

    # calculate average session time in seconds
    new_df['AvgSessionTimeSeconds'] = new_df['TotalCourseTimeSeconds'] / new_df['TotalLogins']

    # round that to whole number
    new_df['AvgSessionTimeSeconds'] = new_df['AvgSessionTimeSeconds'].round().astype(int)

    # also make student id, avg logins, and num submissions integers
    # new_df['StudentID'] = new_df['StudentID'].astype(int)
    new_df['AvgNumLogins'] = new_df['AvgNumLogins'].astype(int)
    new_df['NumSubmissions'] = new_df['NumSubmissions'].astype(int)
    
    # drop any duplicate rows
    new_df = new_df.drop_duplicates()

    # map section from json file 
    with open('sessionMap.json') as f:
        sectionMap = json.load(f)
    
    new_df['Section'] = new_df['Section'].map(sectionMap)

    # rename that column to Session
    new_df = new_df.rename(columns={'Section': 'Session'})

    # EnrollmentDate format: 8/31/2021 3:17:52 PM
    # Last Login Format: 11/22/2021 7:32:11 PM
    # caclulate time between enrollment and last login
    new_df['EnrollmentDate'] = pd.to_datetime(new_df['EnrollmentDate'], format='%m/%d/%Y %I:%M:%S %p')
    new_df['LastLogin'] = pd.to_datetime(new_df['LastLogin'], format = '%m/%d/%Y %I:%M:%S %p')
    new_df['TimeBetweenEnrollmentAndLastLogin'] = new_df['LastLogin'] - new_df['EnrollmentDate']

    # output looks like: 83 days 04:14:19
    # convert to just days
    new_df['DaysBetweenEnrollmentAndLastLogin'] = new_df['TimeBetweenEnrollmentAndLastLogin'].dt.days

    # Save the updated DataFrame to a CSV file
    new_df.to_csv(outputFilePath, index=False)





def main():
    
    dataFilePath = "C:/Users/seanl/Documents/PearsonData/Number_of_Logins_per_Student.csv"

    outputFilePath = "C:/Users/seanl/Documents/PearsonData/cleaned_number_of_logins.csv"

    numLoginsCleanse(dataFilePath, outputFilePath)

if __name__ == "__main__":
    main()