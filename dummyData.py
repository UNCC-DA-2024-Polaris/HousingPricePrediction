import random

def generate_fake_data(n):
    fake_data = []
    gen_data = {
        "price": random.randint(175000, 1500000),
        "area": random.randint(1650, 17000),
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
            if isinstance(value, list):
                house[key] = random.choice(value)
            else:
                house[key] = value
        fake_data.append(house)

    return fake_data

print(generate_fake_data(10))