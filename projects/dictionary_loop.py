user = {
    "username": "userabc",
    "password": "12345",
    "DOB": {
            "year": 2000,
            "month": 10,
            "day": 11
        },
    "city": ['Kathmandu', 'Bhaktapur', 'Lalitpur']
}

for main_key_field, main_value_field in user.items():
    if main_key_field == "city":
        for city_id,city_name in enumerate(main_value_field):
            print(f"{user['username']}'s city number {city_id} is {city_name}")
    elif main_key_field == "DOB":
        for dob_key_field, dob_value_field in main_value_field.items():
            print(f"{user['username']}'s date {dob_key_field} is {dob_value_field}")
    else:
        print(f"user's {main_key_field} is {main_value_field}")