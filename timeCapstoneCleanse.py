import pandas as pd
from datetime import datetime
import json 

# the time formats are hr:mn:sc and this is annoying to work with we're gonna simpligy to seconds
def time_to_seconds(time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds

def cleanse():
    
    df = pd.read_csv('Data/StudentTimeOnCapstoneVsScore.csv')

    # drop any rows that are perfect duplicates
    df = df.drop_duplicates()

    # strip white space where we can 
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # should have all student ID but just in case drop if null
    df = df.dropna(subset=['StudentID'])

    # drop rows with no Score
    df = df.dropna(subset=['Score'])
    df = df[df['Score'] != '--']
    df = df[df['Score'] != '0%*']
    df = df[df['Score'].str.strip() != '']

    # drop rows with score 0% 
    df = df[df['Score'] != '0%']

    # drop rows where Time on Task has a "-" in it
    df = df[~df['Time on Task'].str.contains("-")]


    # drop rows with no Activity Level Average Time on Task
    df = df.dropna(subset=['Activity Level Average Time on Task'])

    # drop also if --:--:-- is in the Activity Level Average Time on Task
    df = df[~df['Activity Level Average Time on Task'].str.contains("--:--:--")]
    

    # make sure no white space for Activity Level Average Time on Task
    df['Activity Level Average Time on Task'] = df['Activity Level Average Time on Task'].str.strip()

    # add column for Activity Level Average Time on Task in seconds 
    df['AvgActivityTimeSeconds'] = df['Activity Level Average Time on Task'].apply(time_to_seconds)

    # add seconds column for Time on Task
    df['TimeOnTaskSeconds'] = df['Time on Task'].apply(time_to_seconds)

    # standardize the score column
    df["Score"] = df["Score"].str.rstrip("*")
    df['Score'] = df['Score'].str.rstrip('%').astype(float) / 100.0

    # now the Activity Level Average Score
    df['Activity Level Average Score'] = df['Activity Level Average Score'].str.rstrip('%').astype(float) / 100.0


    # make sure Number Of Attmpets is a number
    df['Number Of Attempts'] = pd.to_numeric(df['Number Of Attempts'], errors='coerce')






    # now group by studentID and get: AvgSecsOnTask, AcvSecsOnActivity, AvgScore, AvgActivityLevelScore, AvgNumAttempts

    # first define aggregations
    aggregations = {
        'TimeOnTaskSeconds': 'mean',
        'Score': 'mean',
        'Number Of Attempts': 'mean',
        'Course Name': 'first',
    }

    grouped_df = df.groupby("StudentID").agg(aggregations).reset_index()

    # round the aggregated values to two decimal places
    grouped_df = grouped_df.round(2)

    # rename columns
    grouped_df = grouped_df.rename(columns={
        'TimeOnTaskSeconds': 'AvgSecsOnCapstoneTask',
        'Score': 'AvgCapstoneScore',
        'Number Of Attempts': 'AvgNumAttemptsCapstone'
    })

    # map sessions on Course Name 
    with open("sessionMap.json","r") as file:
        mappingData = json.load(file)

    # map mappingData to Course Name
    grouped_df['Course Name'] = grouped_df['Course Name'].map(mappingData)
    



    # save cleaned 
    df.to_csv('Data_Outputs/cleaned_CapstoneData.csv', index=False)

    # save grouped
    grouped_df.to_csv('Data_Outputs/cleaned_Grouped_CapstoneData.csv', index=False)

def main():
    cleanse()

if __name__ == "__main__":
    main()
    