import pandas as pd
import random

def mock_data():
    year_groups = [10, 11, 12]
    data = {"students": []}

    for i in range(100):
        name = f"Student_{i+1}"
        year_group = random.choice(year_groups)
        attendance = [random.randint(2, 100) for _ in range(4)] 
        data["students"].append({"name": name, "year_group": year_group, "attendance": attendance})

    return data

def parse_data(data):
    records = []
    for student in data['students']:
        for week, attendance in enumerate(student['attendance'], start=1):
            records.append({
                "name": student['name'],
                "year_group": student['year_group'],
                "week": week,
                "attendance": attendance
            })
    return pd.DataFrame(records)