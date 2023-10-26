# %%
# Housing датасеты ПИларға база данных салынбағаннан кейін анализ тек mtcars датасетімен жасалды.
import psycopg2
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
sns.set(color_codes=True)


# %%
conn = psycopg2.connect(
    dbname="mtcars",
    user="postgres",
    password="*********",
    host="127.0.0.1"
)


# %%
query = "SELECT * FROM mtcars;"
df = pd.read_sql_query(query, conn)


# %%
print(len(df))
print(df.head())

# %%

max_cars = df[df['qsec'] == df['qsec'].max()]
print('Самая быстрая машина:')
print(max_cars)

# %%
max_cars = df[df['disp'] == df['disp'].max()]
print('Объем')
print(max_cars)


# %%
num_rows, num_columns = df.shape

print(f"Количество строк: {num_rows}")
print(f"Количество столбцов: {num_columns}")

# %%
df.dtypes
# Бұл датасетте 12 баған бар және олар әр түрлі типтегі деректерді қамтиды. Олар object, int64 және float64 типтерінде.

# %%
df.shape

duplicate_rows_df = df[df.duplicated()]
print(f"Количество дубликатов: {duplicate_rows_df.shape}")
# Бұл датасетте дубликат деректер жоқ.

# %%
df.count()
# Бұл датасетте 32 машина бар.

# %%
sns.boxplot(x=df['hp'])
# Detecting Outliers графигі


# %%
df = df.drop(['model'], axis=1)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
#

# %%
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape

# %%
plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c

# %%

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['hp'], df['qsec'])
ax.set_xlabel('HP')
ax.set_ylabel('Qsec')
plt.show()

# %%
conn.close()
# %%
