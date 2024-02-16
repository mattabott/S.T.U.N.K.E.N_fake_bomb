import tkinter as tk
from datetime import datetime
from excel_manager import initialize_excel, update_excel
from timer_logic import find_next_target_time

excel_file = 'team_times.xlsx'
df = initialize_excel(excel_file)

last_printed_team = None
timer_start_time = None

def update_timer():
    global last_printed_team, timer_start_time, df

    now = datetime.now()
    target_time, team = find_next_target_time()
    remaining = target_time - now
    if remaining.total_seconds() > 0:
        mins, secs = divmod(remaining.total_seconds(), 60)
        time_str.set('{:02d}:{:02d}'.format(int(mins), int(secs)))
    else:
        time_str.set("00:00")
    
    if team != last_printed_team:
        print("Prossimo team:", team)
        last_printed_team = team
        if timer_start_time is None:
            timer_start_time = now.strftime("%H:%M:%S")

        update_excel(df, excel_file, team, now, mins, secs)

    root.after(1000, update_timer)

root = tk.Tk()
root.title("Eliminazione Database")
root.geometry("1280x920")
root.configure(bg='black')

time_str = tk.StringVar()
timer_label = tk.Label(root, textvariable=time_str, font=("Helvetica", 300), fg='red', bg='black')
timer_label.pack(expand=True)

update_timer()

root.mainloop()
