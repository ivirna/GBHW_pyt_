import pandas as pd
housing = pd.read_csv("california_housing_test.csv")

housing_population_500_or_less = housing[housing["population"] <= 500]
average_value = housing_population_500_or_less["median_house_value"].mean()
print("Средная стоимость дома в зоне, где кол-во людей от 0 до 500: " + str(average_value))

housing_smallest_population = housing[housing["population"] == housing["population"].min()]
max_households_in_smallest_population = housing_smallest_population["households"].max()
print("Максимальная households в зоне минимального значения population: " + str(max_households_in_smallest_population))
