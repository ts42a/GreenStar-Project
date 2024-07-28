# GreenStar Project

This is a project developed for the Object-Oriented Programming course at the University of Wollongong. The project involves managing and visualizing data related to GreenStar certifications.

## Project Overview

The primary focus of the Green Star Project Directory lies in managing a wide array of project data, including intricate details about projects, associated companies, and organizations involved. The project aims to examine Green Star projects listed in the Green Star project directory and provide a comprehensive visual analysis based on user requirements. Notably, the visual data generated based on user requirements can be saved in a JSON file and later can be exported to regenerate the visual analysis. The program utilizes object-oriented analysis and design principles to model Green Star projects, companies involved, and organizations participating in these projects. Through the implementation of various class design patterns and UML class diagrams, the program empowers users with valuable insights essential for informed decision-making and strategic planning.

## Project Structure

- **Tonmoy_A3.py**: Main project code
- **A3_unittest.py**: Unit tests for the project
- **data.json**: Sample data file for the project
- **test.json**: Additional sample data file for the project
- **A3.png**: UML diagram of the project structure

## UML Diagram
![UML Diagram](A3.png)

## Class Designs and Patterns

The Green Star Project Directory is structured with a modular and flexible object-oriented design, comprising six key classes: `Project`, `Organisation`, `Company`, `GreenStar`, `FileHandler`, and `VisualAnalysis`. Each class encapsulates specific functionalities, promoting code organization and maintainability.

### Class Descriptions

- **Project**: Manages project-related data, including associations with companies and organizations, utilizing dictionaries and lists for effective data representation.
- **Organisation**: Represents organizations participating in Green Star projects, including attributes for organization name and role.
- **Company**: Represents companies involved in Green Star projects, including attributes for company names and associated categories, along with methods for adding projects.
- **GreenStar**: Serves as a container for all Green Star projects and provides methods for adding new projects.
- **FileHandler**: Ensures smooth import and export of project details from JSON files, guaranteeing precision and easy access.
- **VisualAnalysis**: Allows users to create visual reports like pie charts and bar charts based on certain criteria, which can be saved in a JSON file and later recreated.

## Implementation

The Python code provides user-friendly features to interact with Green Star project data. Upon running the program, users are presented with various options:

1. **Add Project**: Users can input details to add a new project to the system.
2. **Import Project**: Users can import project data from external JSON files.
3. **Export Project**: Users can export project data, including newly added projects, to JSON files.

### Visualization and Generate Report

The program offers rich visualization capabilities, enabling users to generate pie charts, bar charts, histograms, and scatter plots based on various project attributes. Users can select specific data types for visualization and apply filter criteria to customize the visualization results.

- **Option 1**: Create a new visual report based on specified criteria.
- **Option 2**: Open an existing visual report stored in a JSON file.

### Exception Handling Mechanism

The Green Star Project Directory program includes a robust exception-handling mechanism to manage errors and unexpected inputs. It ensures the validation of user inputs to meet expected criteria, providing informative feedback for corrections. Handling file-related errors such as file not found or JSON decoding issues during import/export operations. Robust data processing, catching exceptions related to data manipulation and visualization, ensuring smooth execution. General exception handling to address unexpected errors, providing clear guidance for resolution and enhancing user experience.

## Unit Testing and Coverage Analysis

Unit testing is an integral part of ensuring the reliability and correctness of software. This report outlines the unit tests developed for the various components of the Green Star Project Directory. These tests cover functionalities such as importing projects, filtering projects based on specified criteria, and generating visual analyses.

### Test Cases

- **test_add_project**: Verifies the functionality of adding a new project to the directory.
- **test_import_projects**: Tests importing projects from a JSON file and checks if the projects are correctly loaded.
- **test_export_projects**: Tests exporting projects to a JSON file and verifies if the projects are correctly saved.
- **test_read_and_visualize_data**: Tests reading visualized data from a JSON file and displaying it.
- **test_drawPieChart**: Tests drawing a pie chart based on project data.
- **test_drawBarChart**: Tests drawing a bar chart based on project data.

In the Green Star Project Directory, code coverage analysis is performed using tools like coverage.py, which instruments the Python bytecode to track which lines of code are executed during the tests. The coverage report generated provides metrics such as line coverage, branch coverage, and statement coverage. High code coverage is often associated with a lower chance of undetected software bugs.

## How to Run

1. Ensure you have Python installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/ts42a/GreenStar-Project.git
   cd GreenStar-Project
