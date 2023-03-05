# Reproductive Rights Data Project
**Author(s):** Michael Plunkett

A capstone project for UChicago's CAPP122 where abortion related data is taken from multiple sources and used to create intuitive visuals.

## Project Requirements
- [Poetry](https://python-poetry.org/docs/basic-usage/)
- An API key from [Abortion Policy API](https://www.abortionpolicyapi.com/) stored as an environment variable called `ABORTION_POLICY_API_KEY`.
  - The developers of this project stored it in our `.zshrc` file, but you may opt for a `.env` file if that is more comfortable.

## Technical Notes
- Any modules should be added via the `poetry add [module]` command.
  - Example: `poetry add pytest`
- Data from external APIs should be saved in JSON format in the `./reproductive_rights_data_project/data` folder. It will have to be pulled by each dev individually as various data sources required for this project cannot be saved in a public repository, as per our agreements.

## Standard Commands
- `make format`: Formats the python files within the project using the Python formatter [Black](https://github.com/psf/black)
- `make lint`: Runs `pytlint` on the codebase
- `make test`: Runs test cases in the `test` directory
- `make api`: Runs the `api` portion of the codebase
- `make parse-data`: Parses the data output of the `api` layer
- `make visualize`: Takes the data produced from the `parse-data` layer and creates the project's visualizations

## How do we run this thing?
There are two ways that you can run this application, one of them is to run all components of it at once and the other is to run each component individually. I will give you the instructions for both methods below.

#### Run with one command
1. After you have installed [Poetry](https://python-poetry.org/docs/basic-usage/), run the command from the base repository directory: `poetry shell`
2. Run the command `poetry install` to install the package dependencies within the project.
3. Run the `make run` command, and you will run the `api`, `data-parsing`, and `visualization` layers in serial. This will spin up a web page you can access via the URL `localhost:8005`.

#### Run each package individually
1. After you have installed [Poetry](https://python-poetry.org/docs/basic-usage/), run the command from the base repository directory: `poetry shell`
2. Run the command `poetry install` to install the package dependencies within the project.
3. Run the `make api` command to get the data from the _Abortion Policy API_.
4. Run the `make parse-data` command to parse the data so that we can have our data fit the format needed for the next step.
5. Run the `make visualize` command to start the [Flask](https://flask.palletsprojects.com/en/2.2.x/) server, accessible via the URL `localhost:8005`, so that we can visualize the data we have pulled and parsed!
   - For the `make visualize` command, you must have called the two commands that are referenced before it for it to run successfully.
     - Without the data from `make api` and `make parse-data`, `make visualize` has nothing to act on.

## We would like to thank the following organizations for providing our reference data:
- _Abortion Policy API_: https://www.abortionpolicyapi.com/
- _ANSIRH Abortion Facility Database_: https://abortionfacilitydatabase-ucsf.hub.arcgis.com/
- _i need an a_: https://www.ineedana.com/
  - If you or someone you love needs an abortion, you can find up-to-date help at ineedana.com. ❤️
  - The data was given to us by ineedana.com on 2/7/2023.
- _United States Census Bureau_: https://data.census.gov/
- _OpenDataSE_: https://github.com/OpenDataDE/State-zip-code-GeoJSON
