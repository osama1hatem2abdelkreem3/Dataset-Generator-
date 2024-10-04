from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to get a country name without commas
def get_country_without_comma():
    country = fake.country()
    while ',' in country:
        country = fake.country()
    return country

# Function to escape single quotes in SQL strings
def escape_single_quotes(value):
    return value.replace("'", "''")

# File to write SQL insert statements
file_path = 'sql_insert_data.txt'

# Start writing to the file
with open(file_path, 'w') as file:
    
    # Customer table insert statements
    file.write("-- Customer table insert statements\n")
    for i in range(1, 11001):
        dob = fake.date_of_birth(minimum_age=18, maximum_age=80)
        gender = random.choice(['M', 'F'])
        email = escape_single_quotes(fake.email()[:30])  # Limit to 30 characters, escape single quotes
        username = escape_single_quotes(fake.user_name()[:20])  # Limit to 20 characters, escape single quotes
        password = escape_single_quotes(fake.password(length=10)[:30])  # Limit to 30 characters, escape single quotes
        fname = escape_single_quotes(fake.first_name()[:20])  # Limit to 20 characters, escape single quotes
        lname = escape_single_quotes(fake.last_name()[:20])  # Limit to 20 characters, escape single quotes
        file.write(f"INSERT INTO customer VALUES ({i}, '{dob}', '{gender}', '{email}', '{username}', '{password}', '{fname}', '{lname}');\n")
    
    # TheTransaction table insert statements
    file.write("\n-- TheTransaction table insert statements\n")
    for i in range(1, 11001):
        amount = round(random.uniform(10, 5000), 2)
        currency = random.choice(['USD', 'EUR', 'GBP'])
        transaction_type = random.choice(['Purchase', 'Refund'])
        payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal'])
        payment_status = random.choice(['Completed', 'Refunded', 'Pending'])
        customer_id = random.randint(1, 11000)
        file.write(f"INSERT INTO TheTransaction VALUES ({i}, {amount}, '{currency}', '{transaction_type}', '{payment_method}', '{payment_status}', {customer_id});\n")
    
    # Interaction table insert statements
    file.write("\n-- Interaction table insert statements\n")
    for i in range(1, 11001):
        interaction_type = random.choice(['Complaint', 'Feedback', 'Support Request'])
        interaction_outcome = random.choice(['Resolved', 'Implemented', 'Unresolved', 'Pending'])
        follow_up_required = random.choice(['Yes', 'No'])
        interaction_channel = random.choice(['Email', 'Phone', 'Chat'])
        follow_up_date = fake.date_between(start_date='today', end_date='+30d')
        customer_id = random.randint(1, 11000)
        file.write(f"INSERT INTO Interaction VALUES ({i}, '{interaction_type}', '{interaction_outcome}', '{follow_up_required}', '{interaction_channel}', '{follow_up_date}', {customer_id});\n")
    
    # Customer_phone table insert statements
    file.write("\n-- Customer_phone table insert statements\n")
    for i in range(1, 11001):
        phone = fake.random_number(digits=10)  # Random 10-digit phone number
        customer_id = random.randint(1, 11000)
        file.write(f"INSERT INTO Customer_phone VALUES ({phone}, {customer_id});\n")
    
    # Agent table insert statements
    file.write("\n-- Agent table insert statements\n")
    for i in range(1, 101):  # Assuming 100 unique agents
        fname = escape_single_quotes(fake.first_name()[:20])  # Escape single quotes
        lname = escape_single_quotes(fake.last_name()[:20])  # Escape single quotes
        file.write(f"INSERT INTO Agent VALUES ({i}, '{fname}', '{lname}');\n")
    
    # The_address table insert statements (updated table name)
    file.write("\n-- The_address table insert statements\n")
    for i in range(1, 11001):
        country = escape_single_quotes(get_country_without_comma()[:20])  # Escape single quotes, ensure no commas
        government = escape_single_quotes(fake.state()[:20])  # Escape single quotes
        city = escape_single_quotes(fake.city()[:20])  # Escape single quotes
        customer_id = random.randint(1, 11000)
        file.write(f"INSERT INTO The_address VALUES ('{country}', '{government}', '{city}', {customer_id});\n")
    
    # Interaction_Agent_Manager table insert statements
    file.write("\n-- Interaction_Agent_Manager table insert statements\n")
    for i in range(1, 11001):
        interaction_id = random.randint(1, 11000)
        agent_id = random.randint(1, 100)  # Referencing from the agents
        file.write(f"INSERT INTO interaction_Agent_manger VALUES ({interaction_id}, {agent_id});\n")

print(f"SQL insert statements generated in {file_path}")
