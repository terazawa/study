#%%
import pandas as pd

#%%
dt = pd.to_datetime("2019-03-12")
print(repr(dt))
print(dt.tzinfo)

#%%
dt = dt.tz_localize('Asia/Tokyo')
print(repr(dt))
print(dt.tzinfo)
