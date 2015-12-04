
# coding: utf-8

# In[10]:

import numpy as np
import pandas as pd
import json
import rauth 
import time


# In[5]:

def get_search_parameters(lat,long):
      #See the Yelp API for more details
      params = {}
      params["term"] = "restaurant"
      params["ll"] = "{},{}".format(str(lat),str(lon)
      params["radius_filter"] = "2000"
      params["limit"] = "1"

      return params


# In[86]:

def get_results(params):
 
      #Obtain these from Yelp's manage access page
      consumer_key = "cfcCUGuefQQwKTGNjoE0Lg"
      consumer_secret = "kq-fIb_37FfZJtjdGMXlhh6L3Gs"
      token = "h6tOB2r_UQbQVfriEZY1NTiz_1_VTBUp"
      token_secret = "oBPBMNmV65f2p3O3tx0DIPZIxcM"

      session = rauth.OAuth1Session(
        consumer_key = consumer_key
        ,consumer_secret = consumer_secret
        ,access_token = token
        ,access_token_secret = token_secret)

      request = session.get("http://api.yelp.com/v2/search?term=poisoning",params=params)

      #Transforms the JSON API response into a Python dictionary
      data = request.json()
      session.close()

      return data


# In[87]:

def main():
      locations = [(40.7127, -74.0059)]
      api_calls = []
      for lat,long in locations:
        params = get_search_parameters(lat,long)
        api_calls.append(get_results(params))
        #Be a good internet citizen and rate-limit yourself
        time.sleep(1.0)
        return api_calls 


# In[88]:

some = main()


# In[89]:

some


# In[90]:

some[0]['businesses'][0]


# In[29]:

dicto = {}
dicto['a']= 'a'


# In[32]:




# In[ ]:



