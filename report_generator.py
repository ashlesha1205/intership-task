import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

data = pd.read_csv("data.csv")

average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

pdf = canvas.Canvas("Student_Report.pdf", pagesize=A4)
width, height = A4

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(180, height - 50, "Student Marks Report")

pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 100, f"Average Marks: {average_marks:.2f}")
pdf.drawString(50, height - 130, f"Highest Marks: {highest_marks}")
pdf.drawString(50, height - 160, f"Lowest Marks: {lowest_marks}")

pdf.drawString(50, height - 210, "Student Details:")

y = height - 240
for index, row in data.iterrows():
    pdf.drawString(70, y, f"{row['Name']} - {row['Marks']}")
    y -= 20

pdf.save()

print("PDF Report Generated Successfully!")
