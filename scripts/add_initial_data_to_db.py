import os
import pandas as pd
from simapp.models import Plant, Weather
plants_data = [
    {
        "name": "lettuce",
        "W_max": 30,
        "k": 0.001,
        "n": 2,
        "b":855,
        "max_moves": 5,
        "Yield": 0.8,
        "planting_cost": 0.5,
        "revenue": 1.5
    },
    {
        "name": "cabbage",
        "W_max": 40,
        "k": 0.0005,
        "n": 2,
        "b":855,
        "max_moves": 5,
        "Yield": 1.6,
        "planting_cost": 0.5,
        "revenue": 1.5
    },
    {
        "name": "spinach",
        "W_max": 20,
        "k": 0.002,
        "n": 2,
        "b":855,
        "max_moves": 5,
        "Yield": 0.4,

        "planting_cost": 0.5,
        "revenue": 1.5
    },
    {
        "name": "weed",
        "W_max": 30,
        "k": 0.001,
        "n": 2,
        "b":855,
        "max_moves": 5,
        "Yield": 0.8,

        "planting_cost": 0.5,
        "revenue": 1.5
    },
    {
        "name": "Buckweed",
        "W_max": 30,
        "k": 0.125,
        "n": 2.077 ,
        "b":855,
        "max_moves": 5,
        "Yield": 0.8,
        "planting_cost": 0.5,
        "revenue": 1.5
        
    },
    {
        "name": "Lactuca Sativa L.",
        "W_max": 32,
        "k": 0.0045,
        "n": 1.477 ,
        "b":180,
        "max_moves": 5,
        "Yield": 0.8,
        "planting_cost": 0.05,
        "revenue": 100
    },
]


# Save the data to the database
def add_initial_plant_data_to_db():
    print("Loading plant data...")
    for plant_data in plants_data:
        print("Creating plant: ", plant_data["name"])
        Plant.objects.create(**plant_data)



#check if the weather data is in the db

# Construct the path to the CSV file
def add_initial_weather_data_to_db():
    print("Loading weather data...")
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the directory where the script is located
    data_file = os.path.join(base_dir, 'data', 'transformed_weather_data.csv')  # Path to the CSV file
    try:
        df = pd.read_csv(data_file)
        for _, row in df.iterrows():
            weather_instance = Weather()
            weather_instance.set_data({
                'date': row['date'],
                'temperature': row['temperature'],
                'rain': row['rain']
            })
            weather_instance.save()

    except Exception as e:
        print(f'Error loading weather data: {e}')