import datacollection
import pandas as pd

df = pd.read_csv('df_cluster.csv', sep="\"\,\"")
df = pd.concat([df.iloc[:,0].str.split(',', expand=True).rename(columns=dict(zip([0,1], df.columns[0].split(',')))), df.iloc[:,1:]], axis=1)
df.drop(index=df.index[0], axis=0, inplace=True)
df.drop(index=df.index[0], axis=0, inplace=True)
print(df.head())
print(df.shape)
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

sp = datacollection.login()

user_id = sp.current_user()['id']
print(user_id)
name_study = "study"
description_study = "a blend between five fantastic and studious friends"
playlist_study = sp.user_playlist_create(user = user_id, name = name_study, description = description_study)

name_gym = "gym"
description_gym = "a blend between five fantastic and strong friends"
playlist_gym = sp.user_playlist_create(user = user_id, name = name_gym, description = description_gym)

name_cooking = "cooking"
description_cooking = "a blend between five fantastic and satiated friends"
playlist_cooking = sp.user_playlist_create(user = user_id, name = name_cooking, description = description_cooking)

name_celebration = "celebration"
description_celebration = "a blend between five fantastic and spirited friends"
playlist_celebration = sp.user_playlist_create(user = user_id, name = name_celebration, description = description_celebration)

name_sleep = "sleep"
description_sleep = "a blend between five fantastic and sleepy friends"
playlist_sleep = sp.user_playlist_create(user = user_id, name = name_sleep, description = description_sleep)

zero = df.loc[df[13] == '0.0'][:10]
one = df.loc[df[13] == '1.0'][:10]
two = df.loc[df[13] == '2.0'][:10]
three = df.loc[df[13] == '3.0'][:10]
four = df.loc[df[13] == '4.0'][:10]

zero_list = zero.loc[:,3].values.tolist()
one_list = one.loc[:,3].values.tolist()
two_list = two.loc[:,3].values.tolist()
three_list = three.loc[:,3].values.tolist()
four_list = four.loc[:,3].values.tolist()

playlist_study_id = playlist_study['id']
sp.playlist_add_items(playlist_id=playlist_study_id, items = zero_list)

playlist_gym_id = playlist_gym['id']
sp.playlist_add_items(playlist_id=playlist_gym_id, items = one_list)

playlist_cooking_id = playlist_cooking['id']
sp.playlist_add_items(playlist_id=playlist_cooking_id, items = two_list)

playlist_celebration_id = playlist_celebration['id']
sp.playlist_add_items(playlist_id=playlist_celebration_id, items = three_list) 

playlist_sleep_id = playlist_sleep['id']
sp.playlist_add_items(playlist_id=playlist_sleep_id, items = four_list)  

