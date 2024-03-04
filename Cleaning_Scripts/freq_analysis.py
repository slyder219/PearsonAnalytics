import pandas as pd

if __name__ == "__main__":    

    freq_report_cleaned = "C:/Users/seanl/Documents/PearsonData/working_data/frequency_analysis_report/freq_report_cleaned.csv"

    df = pd.read_csv(freq_report_cleaned)



    df.to_csv(freq_report_cleaned, index=False)
