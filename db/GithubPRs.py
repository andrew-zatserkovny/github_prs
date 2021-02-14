#!/usr/bin/env python
# coding: utf-8

# In[1]:


from github import Github
import pandas as pd
import time


# In[ ]:


token = 'some_token'

owner = 'apache'
repo_name = 'airflow'

ONE_HOUR = 3600

g = Github(token)
while True:
    try:
        repo = g.get_repo(f'{owner}/{repo_name}')
    except Exception as e:
        print(e)
        print('Waiting for 1 hr...')
        time.sleep(ONE_HOUR)
        continue
    break

pull_requests = repo.get_pulls('all')
total_pr_count = pull_requests.totalCount

pr_df = pd.DataFrame(columns=['number', 'title', 'url', 'created_at', 'merged_at', 'state'])
file_df = pd.DataFrame(columns=['pr_number', 'filename', 'raw_url'])

for pr in pull_requests:
    print(pr.number)
    pr_df = pr_df.append(
        {
            'number': pr.number, 
            'title': pr.title, 
            'url': pr.url,
            'created_at': pr.created_at,
            'merged_at': pr.merged_at,
            'state': pr.state
        }, 
        ignore_index=True
    )
        
    while True:
        try:
            pr_files = pr.get_files()
            for pr_file in pr_files:
                print(pr_file.filename)
                file_df = file_df.append(
                    {
                        'pr_number': pr.number, 
                        'filename': pr_file.filename, 
                        'raw_url': pr_file.raw_url
                    }, 
                    ignore_index=True
                )
        except Exception as e:
            print(e)
            print('Waiting for 1 hr...')
            time.sleep(ONE_HOUR)
            continue
        break


# In[25]:


pr_df.to_csv('d:\\pr_df.csv', index=False)


# In[26]:


file_df.to_csv('d:\\file_df.csv', index=False)


# In[ ]:




