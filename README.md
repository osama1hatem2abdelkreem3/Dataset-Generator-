# Dataset-Generator-
this python  file powered by faker that generate a dataset for customer management services 

# Data Generation Module

## Overview

This module generates synthetic data for a relational database, specifically designed for a customer management system. The generated data includes various entities such as customers, transactions, interactions, agents, phone numbers, and addresses. This module is ideal for testing and development purposes, allowing you to simulate a real-world database environment.

## Features

- Generates 11,000 records for each table in the database.
- Ensures referential integrity with foreign key constraints.
- Randomly generates realistic data using the Faker library.
- Escapes special characters (e.g., single quotes) to prevent SQL syntax errors.
- Saves all generated SQL insert statements in a `.txt` file for easy execution.

## Tables

The module generates data for the following tables:

1. **Customer**
   - customer_id
   - date_of_birth
   - gender
   - email
   - username
   - Account_password
   - FName
   - LName

2. **TheTransaction**
   - Transaction_id
   - amount
   - currency
   - Transaction_type
   - payment_method
   - payment_status
   - customer_id

3. **Interaction**
   - Interaction_id
   - interaction_type
   - interaction_outcome
   - follow_up_required
   - interaction_channel
   - follow_up_date
   - customer_id

4. **Customer_phone**
   - phone
   - customer_id

5. **Agent**
   - Agent_id
   - FName
   - LName

6. **The_address**
   - country
   - government
   - city
   - customer_id

7. **interaction_Agent_manger**
   - interaction_id
   - Agent_id

## Prerequisites

- Python 3.x
- Required Libraries:
  - Faker

You can install the required library using:

```bash
pip install faker

