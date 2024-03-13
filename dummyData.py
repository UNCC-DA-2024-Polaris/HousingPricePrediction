import random

def generate_dummy_data(n):
    dummyData = []
    gen_data = {
        "price": [175000, 200000, 225000, 250000, 275000, 30000, 325000, 350000, 475000, 500000, 525000, 550000, 575000, 600000],
        "area": [1650, 2000, 2500, 3500, 4000, 4500, 6500, 7000, 7500, 9000, 9500, 11000, 11500, 12000, 12500, 14000, 14500, 15000],
        "bedrooms": [1,2,3,4,5],
        "bathrooms": [1,2,3,4],
        "stories": [1,2,3,4],
        "mainroad": ["Yes", "No"],
        "guestroom": ["Yes", "No"],
        "basement": ["Yes", "No"],
        "hotwaterheating": ["Yes", "No"],
        "airconditioning": ["Yes", "No"],
        "parking": [0,1,2,3,4],
        "prefarea": ["Yes", "No"],
    }

    # loop through n times and randomly generate data by selecting from gen_data
    for _ in range(n):
        house = {}
        for key, value in gen_data.items():
            house[key] = random.choice(value)

        dummyData.append(house)

    return dummyData