import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# This is the url of the page with the state menu. 
BASE_URL = "https://askus-resource-center.unitedspinal.org/index.php?pg=kb.page&id="

# Pages on the site are numbered. The first segment of the tuple
# has the output filename and the second segment is the id of the page.
PAGES = [
    ("ALABAMA", "3318"),
    ("ALASKA", "3320"),
    ("ARIZONA", "3321"),
    ("ARKANSAS", "3322"),
    ("CALIFORNIA", "3328"),
    ("COLORADO", "3329"),
    ("CONNECTICUT", "3330"),
    ("DELAWARE", "3339"),
    ("DISTRICT OF COLUMBIA", "3331"),
    ("FLORIDA", "3350"),
    ("GEORGIA", "3334"),
    ("HAWAII", "3332"),
    ("IDAHO", "3341"),
    ("ILLINOIS", "3362"),
    ("INDIANA", "3335"),
    ("IOWA","3333"),
    ("KANSAS", "3345"),
    ("KENTUCKY", "3383"),
    ("LOUISIANA", "3340"),
    ("MAINE", "3336"),
    ("MARYLAND", "3346"),
    ("MASSACHUSETTS", "3384"),
    ("MICHIGAN", "3343"),
    ("MINNISOTA", "3337"),    
    ("MISSISSIPPI", "3348"),
    ("MISSOURI", "3390"),
    ("MONTANA", "3355"),
    ("NEBRASKA", "3338"),
    ("NEVADA", "3351"),
    ("NEW HAMPSHIRE", "3556"),
    ("NEW JERSEY", "3357"),
    ("NEW MEXICO", "3342"),
    ("NEW YORK", "3352"),
    ("NORTH CAROLINA", "3388"),
    ("NORTH DAKOTA", "3359"),
    ("OHIO", "3344"),
    ("OKLAHOMA", "3353"),
    ("OREGON", "3387"),
    ("PENNSYLVANIA", "3360"),
    ("RHODE ISLAND", "3347"),
    ("SOUTH CAROLINA", "3356"),
    ("SOUTH DAKOTA", "3389"),
    ("TENNESSEE", "3379"),
    ("TEXAS", "3349"),
    ("UTAH", "3358"),
    ("VERMONT", "3386"),
    ("VIRGINIA", "3380"),
    ("WASHINGTON", "3354"),
    ("WEST VIRGINIA", "3361"),
    ("WISCONSIN", "3385"),
    ("WYOMING", "3381")
]

def parse_state(page_num):
    """ This function reads the page into a tree and parses 
        out the relevant tags. 

        Keyword arguments:
            page_num -- id of the page corresponding to a state

        Return: List of facilities contained in the state.
    """

    # Construct the dynamic url
    page_to_read = f'{BASE_URL}{page_num}'
    # Retrieve the page contents
    page = requests.get(page_to_read)
    # Load the page contents into the tree for traversal
    soup = BeautifulSoup(page.text, "html.parser")
    
    # Find the first facility label
    ps = soup.find_all('strong')
    # Get all of the facility labels and strip out outlyers
    list_of_facilities = [(x,x.text) for x in ps if len(x.text.replace(' ', '').strip()) > 2]
    
    # List to hold the parsed facilities objects
    facilities = [] 
    
    # walk the tree of li tags under the facility
    for (ptr,facility) in list_of_facilities[::]:
        # Create a dictionary for key/value pairs.
        facility_obj = {}
        # Sometimes they put a number and period embedded in the name.
        name_parts = ptr.text.replace('\xa0', ' ').split(". ")
        if len(name_parts) == 1:
            # No preceding number
            facility_obj['name'] = ptr.text.replace("\n", "")
        else:
            # Has a preceding number so take the part 
            # without the number
            facility_obj['name'] = name_parts[1].replace("\n", "")

        # List of identifiers that denote a reserved word.  Need this to 
        # identify the activities since it doesnt have any identifier.
        specific_labels = ['OVERVIEW', 'LINK', 'PHONE', 'EMAIL', 'LOCATION', 'CONTACT']

        # Grab a list of all of the li tags that follow
        # the current node in the tree
        lis = ptr.find_all_next('li')
        for item in lis:
            # Try to determine the unidentified activities
            # string by eliminating all of the other identifiers
            if item.text is not None:
                found = False
                for label in specific_labels:
                    if label in item.text.replace('\xa0', ' ').replace("\n", "").upper():
                        found = True
                if not found and len(item.text) > 1:
                    facility_obj['activities'] = item.text.replace('\xa0', ' ').replace("\n", "").strip()
            
            # Grab the Overview and strip out the label
            if 'Overview'.upper() in item.text.upper():
                facility_obj['overview'] = item.text.replace('\xa0', ' ').replace("Overview: ", "").replace("\n", "").strip()
            
            # Grab the href tags and accomodate inconsistencies where they could be on the 
            # same line or multiple lines
            if 'Link'.upper() in item.text.upper() and item.css.select("href") is not None:
                if item.a is not None:
                    # Multiple lines
                    facility_obj['links'] = item.a.text.replace('\xa0', ' ').replace("\n", "").strip()
                else:
                    # Same line
                    facility_obj['links'] = item.text.replace('\xa0', ' ').replace("\n", "").strip()

            # Grab the Phone and strip out and trim off extra spaces
            if 'Phone'.upper() in item.text.replace('\xa0', ' ').upper():
                facility_obj['phone'] = item.text.replace('\xa0', ' ').replace('Phone: ','').replace(' ','').replace("\n", "").strip()
                
            # Grab the Email and trim off extra spaces and accomodate inconsistencies same
            # as Link.
            if 'Email'.upper() in item.text.upper():
                if item.a is not None:
                    # Multiple lines
                    facility_obj['email'] = item.a.text.replace('\xa0', ' ').replace("\n", "").strip()
                else:
                    # Same line
                    facility_obj['email'] = item.text.replace('\xa0', ' ').replace("\n", "").strip()
                    
            # Stop when we find the location so we know
            # the facility is done
            if 'Location:' in item.text:
                facility_obj['location'] = item.text.replace('\xa0', ' ').replace("\n", "").replace('Location: ','').strip()
                break
            
        facilities.append(facility_obj)
        # break
    return facilities

def create_data_dir(path):
    """ Check if directory exists and create if it doesnt.

    Args:
        path (_type_): output path for json and csv files.
    """
    import os
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)

def main():
    # Check if there is a ./data folder and
    # create it if its not there already
    create_data_dir("data")
   
    # Traverse the list of state/page tuples
    for state, page_num in PAGES:
        # Set up the output files
        filename = f"./data/{state}"
        filename_json = f"{filename}.json"
        filename_csv = f"{filename}.csv"
        
        # Create or overwrite the state json file
        with open(filename_json, "w") as state_file:
            print(f"{state}...")

            # Load and Walk the tree
            facilities = parse_state(page_num)
            # Convert the facility objects to proper json
            json.dump(facilities, state_file)
            
            # Write out a csv version of the file also
            # using Pandas DataFrame.
            df = pd.DataFrame(facilities)
            df.to_csv(filename_csv, index=False)

# Main
if __name__ == "__main__":
    main()
    