import pandas as pd

squirrel_data_frame = pd.read_csv("central_park_squirrel_data_2018.csv")

# print(squirrel_data_frame["Primary Fur Color"])

primary_fur_unique_colors=(squirrel_data_frame["Primary Fur Color"]
                           .unique())



total_squirrels_by_fur_df=squirrel_data_frame.groupby(["Primary Fur Color"])["Primary Fur Color"].count()

total_squirrels_by_fur_df.to_csv("total_squirrels_by_fur_df.csv")

print(total_squirrels_by_fur_df)