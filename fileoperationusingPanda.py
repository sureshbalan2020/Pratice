import pandas as pd

#import numpy as np
# filenameCSV = 'C:\POC\Pandas Practice datasets\Inbound\D_CUSTOMER.csv'
filenameJSON = 'C:\POC\Pandas Practice datasets\Inbound\ol_cdump.json'
dfJSON=pd.read_json(filenameJSON,lines=True)
print(dfJSON.head(5))
print(dfJSON.columns)
# dfCSV=pd.read_csv(filenameCSV)
# print(dfCSV.head(5))
# print(dfCSV.columns)
# print(dfCSV['INSERTED_AUDIT_KEY'].head(5))
print(dfJSON.title.value_counts())
dfCleanTitle=dfJSON.copy()
print('count before cleaning title is: '+ str(dfCleanTitle.title.count()))
dfCleanTitle = dfCleanTitle[dfCleanTitle['title']!='No Title Exists.']
print('count after cleaning title is: '+ str(dfCleanTitle.title.count()))
dfCleanTitle = dfCleanTitle[dfCleanTitle['title'].notnull()]
print('count after cleaning nulls from title is: '+ str(dfCleanTitle.title.count()))



# print(dfCleanTitle.publish_date.value_counts().to_csv('C:\POC\Pandas Practice datasets\dfCleandate.csv'))
dfCleanPublishDate=dfCleanTitle.copy()
dfCleanPublishDate['publish_date'] = dfCleanPublishDate['publish_date'].str[-4:]
# print(dfCleanPublishDate.publish_date.value_counts().to_csv('C:\POC\Pandas Practice datasets\dfCleandate_new1.csv'))
dfCleanPublishDate = dfCleanPublishDate[dfCleanPublishDate['publish_date'].astype('str').str.isnumeric()]
dfCleanPublishDate['publish_date'] = dfCleanPublishDate['publish_date'].str.replace(' ', '').astype('int')

#dfCleanPublishDate.publish_date.value_counts().to_csv('C:\POC\Pandas Practice datasets\dfCleandate_new2.csv')
dfCleanPublishDate = dfCleanPublishDate[dfCleanPublishDate['publish_date']>1950]
dfCleanPublishDate = dfCleanPublishDate[dfCleanPublishDate['publish_date']<=2021]
#dfCleanPublishDate['publish_date']<2021]
print('count after cleaning publish date: '+ str(dfCleanPublishDate.publish_date.count()))
dfCleanNumberOfPages=dfCleanPublishDate.copy()
dfCleanNumberOfPages['number_of_pages']=dfCleanNumberOfPages['number_of_pages'].astype(str).str.strip('')
dfCleanNumberOfPages=dfCleanNumberOfPages[dfCleanNumberOfPages['number_of_pages'].str.len() > 0]
dfCleanNumberOfPages=dfCleanNumberOfPages[dfCleanNumberOfPages['number_of_pages'] != "nan"]
dfCleanNumberOfPages['number_of_pages']=dfCleanNumberOfPages['number_of_pages'].apply(float)
dfCleanNumberOfPages['number_of_pages']=dfCleanNumberOfPages['number_of_pages'].apply(int)
dfCleanNumberOfPages = dfCleanNumberOfPages[dfCleanNumberOfPages['number_of_pages']> 20]
print('count after cleaning number of pages: '+ str(dfCleanNumberOfPages.number_of_pages.count()))

dfFinal = dfCleanNumberOfPages.copy()
print(dfFinal.columns)
dfFinal = dfFinal[dfFinal['title'].str.contains('harry',case=False)]
dfFinal = dfFinal[dfFinal['title'].str.contains('potter',case=False)]
dfFinal.to_csv('C:\POC\Output\harrypotter.csv')


dfFinal = dfCleanNumberOfPages.copy()
print(dfFinal.columns)
dfFinal = dfFinal[dfFinal['number_of_pages']==dfFinal['number_of_pages'].max()]
dfFinal.to_csv('C:\POC\Output\\bookwithmaxpages.csv')


dfFinal = dfCleanNumberOfPages.copy()
print(dfFinal['number_of_pages'].mean())
dfFinal = dfFinal['number_of_pages'].sum()/dfFinal['number_of_pages'].count()
f=open('C:\POC\Output\\avenumofpages.csv','a+')
f.write(str(dfFinal))
f.close()




dfFinal = dfCleanNumberOfPages.copy()
print(dfFinal.columns)
dfFinal = dfFinal[['publish_date','authors']]
dfFinal=dfFinal.groupby('publish_date')['authors'].nunique()
dfFinal.to_csv('C:\POC\Output\\author.csv')