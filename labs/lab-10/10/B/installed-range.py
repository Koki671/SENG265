#!/usr/bin/env python3
"""
Obtain and print the names of the packages without the cpu architecture (similar to A\installed4.py) that
 were installed within
the range of dates provided by the user (i.e., variables date_from and date_to). 

* Dates provided by the user should follow the format yyyy-mm-dd
* The output for each package belonging to the specified range should be:
yyyy-mm-dd: NAME_OF_PACKAGE
* An example of output from the program is described in range-2020-07-15-to-2020-07-16.txt

"""

import re
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit(0)
    date_from = sys.argv[1]
    date_to   = sys.argv[2] 
    with open("dpkg.log") as file:

        for line in file:
            if 'installed' in line:
                # Extract the date and package name from the line
                m = re.search(r'^(\d{4}-\d{2}-\d{2}).* installed (.+)', line)
                if m:
                    install_date = m.group(1)
                    package_name = m.group(2)
             # Check if the installation date is within the specified range
                    if date_from <= install_date <= date_to:
                        # Extract the package name without the architecture information
                        package_name_clean = re.sub(r':.*$', '', package_name)
                        # Print the output line in the specified format
                        print(f'{install_date}: {package_name_clean}')

if __name__ == "__main__":
    main()
