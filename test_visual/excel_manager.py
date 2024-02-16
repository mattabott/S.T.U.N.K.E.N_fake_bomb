import pandas as pd
import os.path

def initialize_excel(excel_file):
    if not os.path.isfile(excel_file):
        df = pd.DataFrame(columns=['team1', 'team2', 'team3'])
        df.loc['Orario'] = [None] * len(df.columns)
        df.loc['Timer'] = [None] * len(df.columns)
        df.to_excel(excel_file)
    else:
        df = pd.read_excel(excel_file, index_col=0)
    return df


def update_excel(df, excel_file, team, now, mins, secs):
    try:
        df.loc['Orario', team] = now.strftime("%H:%M:%S")
        df.loc['Timer', team] = '{:02d}:{:02d}'.format(int(mins), int(secs))
        df.to_excel(excel_file)
    except Exception as e:
        print("Errore durante la scrittura del file Excel:", e)
