import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import *
import seaborn as sns

games = pd.read_csv('input/games.csv')
ranking = pd.read_csv('input/ranking.csv')

#TODOS LOS EQUIPOS DE LOCAL
todos = games[games['SEASON']>=2019]
df_todos = todos[['HOME_TEAM_ID','PTS_home', 'FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home','AST_home', 'REB_home']]
mediasLocales2019 = df_todos.groupby(['HOME_TEAM_ID']).mean()

#TODOS LOS EQUIPOS DE VISITANTE
todosVisitantes = games[games['SEASON']>=2019]
df_todosVisitantes = todosVisitantes[['VISITOR_TEAM_ID','PTS_away', 'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away','AST_away', 'REB_away']]
mediasVisitantes2019 = df_todosVisitantes.groupby('VISITOR_TEAM_ID').mean()

#UNIMOS Y LIMPIAMOS DATAFRAMES
df_2019 = games[['GAME_ID','HOME_TEAM_ID', 'VISITOR_TEAM_ID','SEASON','HOME_TEAM_WINS']]
df_2019 = df_2019[df_2019['SEASON']>=2019]
df_2019 = df_2019.merge(right=mediasLocales2019, on=['HOME_TEAM_ID'])
df_2019 = df_2019.merge(right=mediasVisitantes2019, on=['VISITOR_TEAM_ID'])





