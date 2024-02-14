import pandas as pd
from datetime import datetime

# the time formats are hr:mn:sc and this is annoying to work with we're gonna simpligy to seconds
def time_to_seconds(time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds

def cleanse():
    
    df = pd.read_csv('Data/StudentTimeOnCapstoneVsScore.csv')

    # strip white space where we can 
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # should have all student ID but just in case drop if null
    df = df.dropna(subset=['StudentID'])

    # drop rows with no Score
    df = df.dropna(subset=['Score'])
    df = df[df['Score'] != '--']
    df = df[df['Score'] != '0%*']
    df = df[df['Score'].str.strip() != '']



    # drop rows with no Activity Level Average Time on Task
    df = df.dropna(subset=['Activity Level Average Time on Task'])

    # drop also if --:--:-- is in the Activity Level Average Time on Task
    df = df[~df['Activity Level Average Time on Task'].str.contains("--:--:--")]
    

    # make sure no white space for Activity Level Average Time on Task
    df['Activity Level Average Time on Task'] = df['Activity Level Average Time on Task'].str.strip()

    # add column for Activity Level Average Time on Task in seconds 
    df['AvgActivityTimeSeconds'] = df['Activity Level Average Time on Task'].apply(time_to_seconds)


    






    # save
    df.to_csv('Data_Outputs/cleaned_CapstoneData.csv', index=False)

def main():
    cleanse()

if __name__ == "__main__":
    main()
    