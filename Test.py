%reset -f
import pandas as pd
import numpy as np
import random


#%%
users_rating  = {"user1" :{"history" : [1,2,3],"starsum" :0, "CompletedTasks":0 , "Cancelledtasks":0},
                  "user2" :{"history" : [4,5,6],"starsum" :0, "CompletedTasks":0 , "Cancelledtasks":0},
                  "user3" :{"history" : [7,8,9],"starsum" :0, "CompletedTasks":0, "Cancelledtasks":0},
                  "user4" :{"history" : [10,11,12],"starsum" :0, "CompletedTasks":0 , "Cancelledtasks":0},
                  "user5" :{"history" : [13,14,15],"starsum" :0, "CompletedTasks":0 , "Cancelledtasks":0},
                  "user6" :{"history" : [16,17,18],"starsum" :0, "CompletedTasks":0 , "Cancelledtasks":0}}



#%%
df = dict(user1 = np.array([0,0,1,2,2,3,3,4,4,4,5,5]),
               user2 = np.array([0,0,0,1,2,3,3,4,4,4,5,5]),
               user3 = np.array([0,1,1,2,2,2,3,3,3,4,4,5]),
               user4 = np.array([0,0,0,1,2,2,3,3,3,4,4,5]),
               user5 = np.array([0,1,2,3,3,4,4,4,4,5,5,5]),
               user6 = np.array([0,4, 4 ,4 ,4 ,4 ,4, 4, 4, 4 ,4 ,4 ,4, 4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4, 4, 4, 4, 4, 4 ,4 ,4, 4 ,4]))   
                     
df_probs = pd.DataFrame.from_dict(df, orient='index')
df_probs.transpose()
df_probs[0]
