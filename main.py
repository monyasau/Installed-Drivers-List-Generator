import subprocess
import datetime

# Run the driverquery command to get a list of installed drivers
command = 'driverquery'
result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)

# Parsing the output and storing the data in a list
installed_drivers = result.stdout.split('\n')[1:]
installed_drivers = [driver.strip() for driver in installed_drivers if driver.strip()]

# Writing the data to a text file
with open('installed_drivers.txt', 'w') as file:
    file.write("List of Installed Drivers:\n")
    for driver in installed_drivers:
        file.write(driver + '\n')

current_year = datetime.datetime.now().year

print(f"\u00A9 {current_year}, Olajide Olanrewaju, Olajide.m.olanrewaju@gmail.com, www.olanre.netlify.app .")
print("List of installed drivers has been saved to installed_drivers.txt")
