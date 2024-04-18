import csv
import mysql.connector


def fetch_table_data(table_name):
    try:
        # Establish connection to MySQL server
        cnx = mysql.connector.connect(
            host='localhost',
            database='demo',
            user='root',
            password='Sonalisys@24',
            auth_plugin='mysql_native_password'
        )

        cursor = cnx.cursor()

        # Execute query to fetch data from the specified table
        cursor.execute('SELECT * FROM ' + table_name)

        # Get column names (header)
        header = [row[0] for row in cursor.description]

        # Fetch all rows
        rows = cursor.fetchall()

        # Closing connection
        cnx.close()

        return header, rows

    except mysql.connector.Error as err:
        print("Error:", err)
        return None, None


def export(table_name):
    header, rows = fetch_table_data(table_name)

    if header and rows:
        # Define CSV filename
        csv_filename = f'{table_name}.csv'

        # Write data to CSV file
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(header)

            # Write rows
            csv_writer.writerows(rows)

        print(f"{len(rows)} rows written successfully to {csv_filename}")
    else:
        print("Failed to fetch data from the database.")


# Example usage
export('lifeexpectancy')