from datetime import datetime, timedelta

def find_next_target_time():
    now = datetime.now()
    teams = ['team1', 'team2', 'team3']
    times = [now.replace(hour=23, minute=20, second=0, microsecond=0),
             now.replace(hour=23, minute=30, second=0, microsecond=0),
             now.replace(hour=22, minute=30, second=0, microsecond=0)]

    future_times = [(times[i], teams[i]) for i in range(len(times)) if times[i] > now]
    if future_times:
        return min(future_times, key=lambda x: x[0])
    else:
        return times[0] + timedelta(days=1), teams[0]
