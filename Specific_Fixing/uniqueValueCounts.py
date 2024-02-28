import pandas as pd


def run():
    df = pd.read_csv('Data_Outputs/cleaned_session_data.csv')

    counts = df["Session"].value_counts()

    print(counts)


# !! Spring 2022 has most data 



def main():
    run()

if __name__ == "__main__":
    main()