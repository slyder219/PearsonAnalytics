import pandas as pd
from datetime import datetime



def sessionDataCleanse():
    # load the data
    df = pd.read_csv('data/SessionData.csv')

    # empty list to store student data
    newData = []

    # iter through each row
    for index, row in df.iterrows():

        # check if we have header table, if so then grab header info 
        if row['Status'] == "	Active":
            data = {
                "StudentID": row["StudentID"],
                "AvgNumLogins": row["AvgNumLogins"].strip(),
                "NumSubmissions": row["NumSubmissions"].strip(),
                "TotalCourseTime": row["TotalCourseTime"].strip(),
                "TotalLogins": row["TotalLogins"].strip(),
                "LastLogin": row["LastLogin"].strip(),
                "EnrollmentDate": row["EnrollmentDate"].strip(),
                "Instructor": row["Instructor"].strip(),
                "Section": row["Section"].strip() }
            
            # add all that data to list 
            newData.append(data)

    # Create a new DataFrame from the list of dictionaries
    new_df = pd.DataFrame(newData)

    # Save the new DataFrame to a CSV file
    new_df.to_csv('Data_Outputs/cleaned_session_data.csv', index=False)       

    return new_df


def addSecondsColumn(cleanedDF):

    df = cleanedDF

    def time_to_seconds(time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds

    # Add a new column 'TotalTimeSeconds' to the DataFrame
    df['TotalTimeSeconds'] = df['TotalCourseTime'].apply(time_to_seconds)

    # Save the updated DataFrame to a CSV file
    df.to_csv('Data_Outputs/cleaned_session_data.csv', index=False)

def main():
    
    addSecondsColumn(sessionDataCleanse())
  



if __name__ == "__main__":
    main()