# Reproductive Rights Data Project
A capstone project for UChicago's CAPP122 where abortion related data is taken from multiple sources and used to create intuitive visuals and searchable spreadsheets.

## Project Requirements
- [Poetry](https://python-poetry.org/docs/basic-usage/)

## Technical Notes
- Any modules should be added via the `poetry add [module]` command.
  - Example: `poetry add pytest`
- Data from external APIs should be saved in JSON format in the `./data` folder. It will have to be pulled by each dev individually as we cannot save the data in a public repository, as per our agreement.

## Standard Commands
- `make format`: Formats the python files within the project using the Python formatter [Black](https://github.com/psf/black)
- `make lint`: Runs `pytlint` on the codebase
- `make test`: Runs test cases in the `test` directory
- `make api`: Runs the `api` portion of the codebase
- `make parse-data`: Parses the data output of the `api` layer
- `make visualize`: Takes the data produced from the `parse-data` layer and creates the project's visualizations

## How do we run this thing?
1. After you have installed [Poetry](https://python-poetry.org/docs/basic-usage/), run the command: `poetry shell`
2. Run the command `poetry install` to install the package dependencies within the project.
3. ADD MORE THINGS AS WE GET MORE FUNCTIONALITY

### Datasets courtesy of:
- _Abortion Policy API_: https://www.abortionpolicyapi.com/
- _ANSIRH Abortion Facility Database_: https://abortionfacilitydatabase-ucsf.hub.arcgis.com/
- _i need an a_: https://www.ineedana.com/
- _United States Census Bureau_: https://data.census.gov/
