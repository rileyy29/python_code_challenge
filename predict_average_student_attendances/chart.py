import matplotlib.pyplot as plt

def generate_line_chart(df, predictions):
    plt.figure(figsize=(12, 6))
    
    for year_group in df['year_group'].unique():
        year_data = df[df['year_group'] == year_group].groupby('week')['attendance'].mean().reset_index()
        weeks = list(year_data['week'].values)
        attendance = list(year_data['attendance'].values)

        future_weeks = [5, 6]
        future_attendance = predictions[year_group]
        weeks.extend(future_weeks)
        attendance.extend(future_attendance)

        plt.plot(weeks, attendance, marker='o', label=f"Year {year_group}")

    plt.title("Average Attendance with Predictions")
    plt.xlabel("Week")
    plt.ylabel("Average Attendance (%)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(".output/predict_average_student_attendances.png")
    plt.show()