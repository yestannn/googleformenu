import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("botmenu.json", scope)


client = gspread.authorize(creds)

meal = client.open("meals").sheet1


def get_type(typee):
	''' to get type of meal 
	there are three type of meal:
	'meal' , 'sweet' , 'drink'
	other arguments will return EROR
	'''

	global meal 

	result = []
	column1 = meal.col_values(1)
	column2 = meal.col_values(2)
	column3 = meal.col_values(3)
	
	j = min(len(column1),len(column2),len(column3))
	
	for i in range(1,j):
		if 	column3[i] == typee:
			result.append(str(column1[i]) + ' | ' + str(column2[i]))


	return result


a =str(input())
pprint(get_type(a))



