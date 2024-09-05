import csv
import json
import sys

def update_json(csv_file, json_file, env):
    # Read the CSV file and store its contents in a dictionary
    #print(env)
    if (env != PROD | DEV):
        print ("Please enter the environment as PROD or DEV")
        sys.exit(1)
    data_to_update = {}
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            env1 = row['ENV']
            if env == env1:
                #print(env1)
                data_to_update[env1] = {
                     "host": row["host"],
                     "port": int(row["port"]),  # Convert port to integer
                     "dbname": row["dbname"],
                     "user": row["user"],
                    "password": row["password"]
                    }
        print(data_to_update)
    # Read the JSON file
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    #print (json_data)

    for env, data in data_to_update.items():
        if env in json_data:
            json_data[env].update(data)
        else:
            # Add new environment section if it doesn't exist
            json_data[env] = data
    #print (json_data)

    # Write the updated data back to the JSON file
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    #
    # print(f"JSON file updated successfully for environment: {env}")

if __name__ == "__main__":
    # Ensure that the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <csv_file> <json_file> <env>")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    env = sys.argv[3]
update_json(csv_file, json_file, env)