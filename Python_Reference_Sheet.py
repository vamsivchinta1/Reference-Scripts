'''misc code:''' 
pd.set_option('display.max_columns', None)
new_directory = os.path.join(currentDirectory, r'NewDirectoryFolderName')
  if not os.path.exists(new_directory):
      os.makedirs(new_directory)
      
'''column editting'''
df1 = df[['a','b']]
df.loc[:, ['food', 'color']]
df1 = df.iloc[:,0:2]
print(df.columns.values.tolist())
df.loc[:, df.columns != 'b']
df[df.columns.difference(['b'])]
df.drop(['a', 'b'], axis=1)

'''row editting'''
df.dropna(axis='index', how='any', inplace=True)

'''list editting'''
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end

'''MultiIndexing'''
df.set_index(['year', 'month'], inplace=True)
list(mi.columns.levels[0])   | mi = multiindex dataframe

'''Imputting'''
df.fillna('',inplace=True)
df = df.fillna('')
df[col].fillna(0, inplace=True)

'''Joining'''
df = pd.merge(df1, df2, on='A', how='inner')
'''Exporting Data'''
df.to_excel('cat_kst_df.xlsx', sheet_name='Sheet_name_1')

'''Column Header Editting'''
df.columns = df.columns.str.upper()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.title() #camel casing
df.columns = df.columns.str.strip() #to remove all the leading or trailing spaces
df.columns = df.columns.map(lambda x : x.replace("-", "_").replace(" ", "_")) #a simple lambda function to replace the space and hyphen with underscore
dict = {'Dept.1':'Dept','Class.1':'Class'}
df1.rename(columns=dict, inplace=True)


'''Column Values Editting'''
data["First Name"]= data["First Name"].str.lower()
df['datetime'] = pd.to_datetime(df['datetime']).dt.date
