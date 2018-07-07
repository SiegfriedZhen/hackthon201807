
# coding: utf-8

# In[1]:

import pandas as pd
import gc


# In[2]:

file_path_action = r'E:\ChingYi_workspace\hack104\train-action.json'


# In[3]:

raw = []
ct = 0

# 目前預設讀100萬筆, 實際整體資料大於3000萬, 請依記憶體量力而為
limit_cnt =  1000000

with open(file_path_action) as f:
    for line in f:
        raw.append(line)
        ct = ct + 1
        
        if ct == limit_cnt:
            print(len(raw), ' size finished!')
            break



# In[4]:

output = ','.join(raw)


# In[5]:

del raw
gc.collect()


# In[6]:

output = output.replace('\n', '')


# In[7]:

gc.collect()


# In[8]:

output = pd.read_json('[' + output + ']')


# In[11]:

output_path = r'E:\ChingYi_workspace\hack104\train-action_10M.csv'


# In[14]:

output.to_csv(output_path)


# In[ ]:



