# Reproductive Rights Data Project
**Author(s):** Michael Plunkett

A capstone project for UChicago's CAPP122 where abortion related data is taken from multiple sources and used to create intuitive visuals.

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
For the `make visualize` command, you must have called the two commands that are referenced before it for it to run successfully.
- Without the data from `make api` and `make parse-data`, `make visualize` has nothing to act on.

1. After you have installed [Poetry](https://python-poetry.org/docs/basic-usage/), run the command: `poetry shell`
2. Run the command `poetry install` to install the package dependencies within the project.
3. Run the `make api` command to get the data from the _Abortion Policy API_.
4. Run the `make parse-data` command to parse the data so that we can have our data fit the format needed for the next step.
5. Run the `make visualize` command to start the [Flask](https://flask.palletsprojects.com/en/2.2.x/) server so that we can visualize the data we have pulled and parsed!
  - The previous two steps must have been run for this step to execute successfully.

### We would like to thank the following organizations for providing our reference data:
- _Abortion Policy API_: https://www.abortionpolicyapi.com/
- _ANSIRH Abortion Facility Database_: https://abortionfacilitydatabase-ucsf.hub.arcgis.com/
- _i need an a_: https://www.ineedana.com/
  - If you or someone you love needs an abortion, you can find up-to-date help at ineedana.com. ❤️
  - The data was given to us by ineedana.com on 2/7/2023.
- _United States Census Bureau_: https://data.census.gov/
