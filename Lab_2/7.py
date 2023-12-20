day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
	return year%4 == 0	and year%100 != 0 or year%400 == 0
def day_of_year(day, month, year):
	if is_leap(year):
		day_in_month[1] = 29
	if month == 1:
		return day
	return sum(day_in_month[:month-1]) +day
x = list(map(int, input("Enter [day-month-year]: ").split("-")))
print(day_of_year(x[0], x[1], x[2]))
