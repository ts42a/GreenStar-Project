# GreenStar Project

This is a project developed for the Object-Oriented Programming course at the University of Wollongong. The project involves managing and visualizing data related to GreenStar certifications.

The GreenStar Project Directory is designed to manage and visualize a wide array of project data, including intricate details about projects, associated companies, and organizations involved. The program enables users to generate visual data based on user requirements, which can be saved in a JSON file and later exported to regenerate the visual analysis.

Key Features
Object-Oriented Design: Utilizes principles of object-oriented analysis and design to encapsulate project data, participating companies, and organizations.
Modular Architecture: The project is structured with six key classes: Project, Organisation, Company, GreenStar, FileHandler, and VisualAnalysis, each encapsulating specific functionalities.
Data Management: Allows importing and exporting of project details from JSON files.
Visualization: Generates visual reports such as pie charts, bar charts, histograms, and scatter plots based on various project attributes.
Class Designs and Patterns
The GreenStar Project Directory is built using the following classes:

Project: Manages project-related data including associations with companies and organizations.
Organisation: Represents organizations participating in Green Star projects.
Company: Represents companies involved in Green Star projects.
GreenStar: Serves as a container for all Green Star projects.
FileHandler: Ensures smooth import and export of project details from JSON files.
VisualAnalysis: Allows users to create visual reports and export the data for future use.

## Project Structure
- **Tonmoy_A3.py**: Main project code
- **A3_unittest.py**: Unit tests for the project
- **data.json**: Sample data file for the project
- **test.json**: Additional sample data file for the project
- **A3.png**: UML diagram of the project structure

## UML Diagram
![UML Diagram](A3.png)

How to Run
Ensure you have Python installed.
Clone the repository:
bash
Copy code
git clone https://github.com/ts42a/GreenStar-Project.git
cd GreenStar-Project
Run the main script:
bash
Copy code
python Tonmoy_A3.py
Run the unit tests:
bash
Copy code
python A3_unittest.py
Data
data.json: Contains sample data for visualizing the projects.
test.json: Additional sample data file for the project.
Visualization and Generate Report
The program offers rich visualization capabilities, enabling users to generate various charts based on project attributes. Users can select specific data types for visualization and apply filter criteria to customize the results.

Options
Create a new visual report based on specified criteria.
Open an existing visual report stored in a JSON file.
Exception Handling
The program includes a robust exception-handling mechanism to manage errors and unexpected inputs:

Validation: Ensures user inputs meet expected criteria.
File Handling: Manages errors such as file not found or JSON decoding issues.
Data Processing: Catches exceptions related to data manipulation and visualization.
General Handling: Addresses unexpected errors and provides clear guidance for resolution.
Unit Testing and Coverage Analysis
Unit testing is integral to ensuring software reliability and correctness. This project includes comprehensive unit tests covering functionalities such as importing projects, filtering projects, and generating visual analyses.

Test Cases
test_add_project: Verifies adding a new project.
test_import_projects: Tests importing projects from a JSON file.
test_export_projects: Tests exporting projects to a JSON file.
test_read_and_visualize_data: Tests reading and visualizing data from a JSON file.
test_drawPieChart: Tests generating a pie chart.
test_drawBarChart: Tests generating a bar chart.
Code coverage analysis is performed using tools like coverage.py, providing metrics such as line coverage, branch coverage, and statement coverage. High code coverage is aimed to minimize the risk of undetected bugs.

Conclusion
The GreenStar Project Directory effectively manages and analyzes Green Star project data through robust object-oriented design and implementation of design patterns. Comprehensive unit testing ensures reliability, with high code coverage minimizing the risk of undetected bugs. The program offers rich visualization capabilities, enabling users to generate and customize visual reports for informed decision-making. Future enhancements could include additional charting options, UI improvements, and optimization for larger datasets, making the program a versatile tool for analyzing and visualizing Green Star project data.
