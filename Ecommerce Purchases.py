import pandas as pd
dataframe = pd.read_csv('Ecommerce Purchases.csv')
#print(dataframe)


#1. Display top 10 rows of the dataset
#print(dataframe.head(10))


#2. Display last 10 rows
#print(dataframe.tail(10))


#3. Check the datatype of columns
#print(dataframe.dtypes)


#4. Check null values
#print(dataframe.isnull().sum())


#5. How many rows and columns
'''
print(len(dataframe.columns)) 
print(len(dataframe))
print(dataframe.info())
'''


#6. Highest and lowest purchases
'''
#print(dataframe.columns)
print(dataframe['Purchase Price'].max())
print(dataframe['Purchase Price'].min())
'''


#7. Average Purchase Price
#print(dataframe['Purchase Price'].mean())


#8. How many people have French 'fr' as their language
'''
#print(dataframe.columns)
#print(len(dataframe[dataframe['Language']=='fr']))
print(dataframe[dataframe['Language']=='fr'].count())
'''


#9. Job title contains Engineer
'''
#print(dataframe.columns)
print(dataframe[dataframe['Job'].str.contains('Engineer', case=False)])
'''


#10. Find email of the person with the following IP address: 132.207.160.22
'''
#print(dataframe.columns)
print(dataframe[dataframe['IP Address']=='132.207.160.22']['Email'])
'''

#11. How many people have Mastercard as their credit card provider and made a purchase above 50
'''
#print(dataframe.columns)
dataframe = dataframe[(dataframe['CC Provider']=='Mastercard') & (dataframe['Purchase Price']>=50)]
print(len(dataframe))
'''


#12. Find email of the person with the following credit card number:
#4664825258997302/60430098636
'''
#print(dataframe.columns)
print(dataframe[dataframe['Credit Card']==60430098636]['Email'])
'''

#13. How many people purchase during AM and PM
'''
#print(dataframe.columns)
print(dataframe['AM or PM'].value_counts())
'''


#14. How many people have a credit card that expires in 2020
'''
#print(dataframe.columns)
#print(dataframe['CC Exp Date'])

def fun():
    count=0
    for date in dataframe['CC Exp Date']:
        if date.split('-')[0]=='20':
            count = count+1
    print(count)
fun()

#print(len(dataframe[dataframe['CC Exp Date'].apply(lambda x:x[:2]=='20')]))
'''


#15. Top 5 most popular email providers
#print(dataframe.columns)
#print(dataframe['Email'])
'''
list1 = []
for email in dataframe['Email']:
    list1.append(email.split('@')[1])

dataframe['temp']=list1
#print(dataframe.head(1))
dataframe = dataframe['temp'].value_counts().head()
print(dataframe)

print(dataframe['Email'].apply(lambda x:x.split('@')[1]).value_counts().head())
'''












