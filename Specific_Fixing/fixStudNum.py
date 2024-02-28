import pandas as pd
from cleanPaths import filepaths 


# for each filepath csv, StudentNum column needs to be formatted as int. No decimals
def fixStudNum(filepaths):
    for filepath in filepaths:
        df = pd.read_csv(filepath)
        df["StudentNum"] = df["StudentNum"].astype(float).fillna(0).astype(int)
        df.to_csv(filepath, index=False)

def main():
    fixStudNum(filepaths)

if __name__ == "__main__":
    main()