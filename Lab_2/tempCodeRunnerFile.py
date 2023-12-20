day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
	return year%4 == 0	and year%100 != 100 or year%400 == 0
def day_of_year(day, month, year):
	if is_leap(year):
		day_in_month[1] = 29
	if month == 1:
		return day
	return sum(day_in_month[0:month-1], day)
def day_in_year(year):
	if is_leap(year):
		return 366
	else: return 365
def date_diff(x, y):
	if x[2] == y[2]:
		return day_of_year(y[0], y[1], y[2]) - day_of_year(x[0], x[1], x[2]) + 1
	else:
		day_in_first_year = day_in_year(x[2]) - day_of_year(x[0], x[1], x[2]) + 1
		day_in_btw_year = 0
		for i in range(x[2]+1, y[2]):
			day_in_btw_year += day_in_year(i)
		return day_of_year(y[0], y[1], y[2]) + day_in_first_year + day_in_btw_year
x = list(map(int, input("Enter [day-month-year]: ").split("-")))
y = list(map(int, input("Enter [day-month-year]: ").split("-")))
print(date_diff(x,y))
