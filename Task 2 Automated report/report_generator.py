import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ------------------------------------
# STEP 1: READ DATA
# ------------------------------------
df = pd.read_csv("sales_data.csv")

total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
highest_month = df.loc[df['Sales'].idxmax(), 'Month']
highest_value = df['Sales'].max()

# ------------------------------------
# STEP 2: CREATE PDF REPORT
# ------------------------------------
pdf_file = "Sales_Report.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

c.setFont("Helvetica-Bold", 20)
c.drawString(200, 750, "Sales Report")

c.setFont("Helvetica", 12)
c.drawString(50, 700, "Summary of Sales Data:")
c.drawString(50, 680, f"Total Sales: {total_sales}")
c.drawString(50, 660, f"Average Monthly Sales: {average_sales:.2f}")
c.drawString(50, 640, f"Highest Sales Month: {highest_month} ({highest_value})")

# Table Header
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 600, "Month")
c.drawString(200, 600, "Sales")

# Table Rows
y = 580
c.setFont("Helvetica", 12)
for i, row in df.iterrows():
    c.drawString(50, y, str(row['Month']))
    c.drawString(200, y, str(row['Sales']))
    y -= 20

c.save()

print("PDF generated successfully as Sales_Report.pdf")
