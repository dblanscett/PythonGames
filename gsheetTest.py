#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Devan Blanscett
' Program name: 
' Program Description: 
' 
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import pandas
import pygsheets

#.authroize takes passed creds to google and returns with the account info in an object that
#has ability to open, create, edit, etc. the google sheets for that client
gClient = pygsheets.authorize(service_file='googlecreds.json')

testSheet = gClient.open('gsheet test')

page1 = testSheet[0]
page2 = testSheet[1]

print(page1.get_as_df())
print(page2.get_as_df())

#code body here
