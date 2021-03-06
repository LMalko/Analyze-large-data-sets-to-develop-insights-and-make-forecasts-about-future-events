import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911_data.csv")

# 1. Check info of the file.

# print(df.info())


# 2. What are the top 6 zipcodes for 911 calls?

# print(df["zip"].value_counts().head(6))


# 3. How many unique title codes are there?

# print(df['title'].unique())
# print(df['title'].nunique())


# 4. Reason column with abbreviation value of Reasons/ Departments column.

df["Reason"] = df["title"].apply(lambda title: title.split(":")[0])
#
# print(df["Reason"])

# 5. Most common reason.

# print(df["Reason"].value_counts())

# 6. Countplot for 'Reason column'

# sns.countplot(x="Reason", data=df, palette="viridis")
# plt.show()

# 7. Datatype of the objects in the timeStamp column

# print(type(df['timeStamp'].iloc[0]))

# 8. Convert this objects into DateTime objects.

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# print(type(df['timeStamp'].iloc[0]))

# 9. Grab hour attribute from 'timeStamp column.

# time = df['timeStamp'].iloc[0]
#
# print(time.hour)

# 10. Create Hour, Month, Day of Week columns.

df["Hour"] = df['timeStamp'].apply(
    lambda time: time.hour)
df["Month"] = df['timeStamp'].apply(
    lambda time: time.month)

#
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

df["Day of Week"] = df['timeStamp'].apply(
    lambda time: days[time.dayofweek])


# alternative

# dmap = {0: "Mon", 1: "Tue", 2:"Wed", 3:"Thu",
#         4:"Fri", 5:"Sat", 6:"Sun"}
# df["Day of Week"] = df['timeStamp'].apply(
#     lambda time: time.dayofweek)
# df["Day of Week"] = df["Day of Week"].map(dmap)



# print(df["Day of Week"])



# 11. Sort days of the week


df["Day of Week"] = df["Day of Week"].astype('category',
                                  ordered=True,
                                  categories=days)


# 12. Countplot of the Day of Week column
# with the hue based off of the Reason column &
# the legend relocated outside

# sns.countplot(x="Day of Week", data=df, hue="Reason")
# plt.legend(loc=2, bbox_to_anchor=(1.0, 0.5))

# plt.show()


# 13. Countplot of the Month column
# with the hue based off of the Reason column &
# the legend relocated outside.
# Months 9,10,11 are missing.


# sns.countplot(x="Month", data=df, hue="Reason")
# plt.legend(loc=2, bbox_to_anchor=(1.0, 0.5))

# plt.show()

byMonth = df.groupby("Month").count()
# byMonth["lat"].plot(marker="o")

# plt.show()


# 14. Linear fit on the number of calls per month.


# sns.lmplot(x="Month", y="twp", data=byMonth.reset_index())
#
# plt.show()

# 15. "Date" column with date value from timeStamp column.
# This column is grouped by with count() aggregate.

df["Date"] = df['timeStamp'].apply(lambda time: time.date())

# df.groupby("Date").count()['desc'].plot()
# # df.groupby("Date").count()['lat'].plot()
# plt.tight_layout()

# plt.show()

# 16. "Date" column with "Reason" seperately.

# df[df["Reason"] == "Traffic"].groupby("Date").count()['desc'].plot()
# plt.tight_layout()
# plt.title("Traffic")
# plt.show()

# df[df["Reason"] == "Fire"].groupby("Date").count()['desc'].plot()
# plt.tight_layout()
# plt.title("Fire")
# plt.show()

# df[df["Reason"] == "EMS"].groupby("Date").count()['desc'].plot()
# plt.tight_layout()
# plt.title("EMS")
# plt.show()

# 17. Heatmaps. Dataframe restructured to matrix form -
# columns become the Hours and the index becomes the
# day of the week.

plt.figure(figsize=(12, 6))


# print(df.groupby(by=["Day of Week", "Hour"]).count())
# print(df.groupby(by=["Day of Week", "Hour"]).count()["Reason"].unstack())

dayHour = df.groupby(by=["Day of Week", "Hour"]).count()["Reason"].unstack()
sns.heatmap(dayHour, cmap="viridis")


plt.show()

# 18. Clustermap of the above DataFrame.

sns.clustermap(dayHour, cmap="coolwarm")
plt.show()

# 19. Heatmap and clustermap of the above DataFrame
# with months instead of hours.

dayMonth = df.groupby(by=["Day of Week", "Month"]).count()["Reason"].unstack()
sns.heatmap(dayMonth, cmap="viridis")


plt.show()

sns.clustermap(dayMonth, cmap="coolwarm")
plt.show()