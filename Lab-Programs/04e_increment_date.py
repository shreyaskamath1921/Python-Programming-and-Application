from datetime import datetime,timedelta
def next_date(value):
    return (datetime.strptime(value,"%d/%m/%Y")+timedelta(days=1)).strftime("%d/%m/%Y")
value=input("Enter a date (dd/mm/yyyy): ")
print("Next date:",next_date(value))
