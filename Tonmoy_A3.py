import json
import matplotlib.pyplot as plt

class Project:
    def __init__(self, project_name, location, status, rating, score, certified_date, rating_tool, companies, organisations):
        self.project_name = project_name
        self.location = location
        self.status = status
        self.rating = rating
        self.score = score
        self.certified_date = certified_date
        self.rating_tool = rating_tool
        self.companies = companies if companies else []
        self.organisations = organisations if organisations else []

class Company:
    def __init__(self, name, categories=None):
        self.name = name
        self.categories = categories if categories else []
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

class Organisation:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Greenstar:
    def __init__(self, allprojects=None):
        self.allprojects = allprojects if allprojects is not None else {}

    def add_project(self):
        title = input("Enter project title: ").strip()
        location = input("Enter location: ").strip()
        while True:
            status = input("Enter 1 = Certified or 2 = Registered: ").strip()
            if status == "1":
                status = "Certified"
                break
            elif status == "2":
                status = "Registered"
                break
            else:
                print("Invalid choice! Try again.")
        while True:
            try:
                rating = int(input("Enter rating (Range 1-5): ").strip())
                if 1 <= rating <= 5:
                    break
                else:
                    print("Invalid rating range")
            except ValueError:
                print("Please enter an integer value for rating")
        score = input("Enter score: ").strip()
        while True:
            certified_date = input("Enter certified date (dd-mm-yyyy): ").strip().replace("-", "").replace("/", "")
            if len(certified_date) == 8 and certified_date.isdigit():
                break
            else:
                print("Invalid date format! Please enter the date in dd-mm-yyyy format.")
        rating_tool_options = ["V1", "V2", "V3", "V4"]
        while True:
            rating_tool = input("Enter rating tool (V1, V2, V3, V4): ").strip().upper()
            if rating_tool in rating_tool_options:
                break
            else:
                print("Invalid rating tool! Please enter one of V1, V2, V3, V4.")
        organisations = []
        while True:
            org_name = input("Enter organization name for this project (Press 'ENTER' or 'xx' to finish): ").strip()
            if org_name.lower() == 'xx' or org_name == '':
                break
            org_role = input("Enter role for the organization: ").strip()
            organisations.append(Organisation(org_name, org_role))
        companies = []
        while True:
            com_name = input("Enter company name for this project (Press 'ENTER' or 'xx' to finish): ").strip()
            if com_name.lower() == 'xx' or com_name == '':
                break
            else:
                companies.append(com_name)
        project = Project(title, location, status, rating, score, certified_date, rating_tool, companies, organisations)
        self.allprojects[title] = project
        print("Project added successfully.\n")

class FileHandler:
    @staticmethod
    def import_projects(filename, greenstar):
        if not filename.endswith(".json"):
            filename += ".json"
        try:
            with open(filename, "r") as file:
                projects_data = json.load(file)
                new_projects = {project_data["project_name"]: Project(
                    project_data["project_name"],
                    project_data["location"],
                    project_data["status"],
                    project_data["rating"],
                    project_data["score"],
                    project_data["certified_date"],
                    project_data["rating_tool"],
                    project_data["companies"],
                    [Organisation(org["name"], org["role"]) for org in project_data["organisations"]]
                ) for project_data in projects_data}
                greenstar.allprojects.update(new_projects)
                print("Projects loaded successfully from", filename)
        except FileNotFoundError:
            print("File not found.")

    @staticmethod
    def export_projects(filename, projects):
        if not filename.endswith(".json"):
            filename += ".json"
        try:
            with open(filename, "w") as file:
                projects_data = []
                for project_name, project in projects.items():
                    project_dict = {
                        "project_name": project.project_name,
                        "location": project.location,
                        "status": project.status,
                        "rating": project.rating,
                        "score": project.score,
                        "certified_date": project.certified_date,
                        "rating_tool": project.rating_tool,
                        "companies": project.companies,
                        "organisations": [{"name": org.name, "role": org.role} for org in project.organisations]
                    }
                    projects_data.append(project_dict)
                json.dump(projects_data, file, indent=5)
                print("Projects saved successfully to", filename)
        except Exception as e:
            print(f"Error saving projects to {filename}: {e}")

class VisualAnalysis:
    def __init__(self, greenstar):
        self.greenstar = greenstar
        self.filter_values = []
    
    def filterProjects(self):
        datatype = ["project_name", "location", "status", "rating", "score", "certified_date", "rating_tool", "companies", "organisations"]
        while True:
            issisuby = input("Select what to visualize (project_name, location, status, rating, score, certified_date, rating_tool, companies, organisations): ").strip().lower()
            if issisuby in datatype:
                break
            else:
                print("Unknown data selected. Please select a valid data type.")
        datatype.remove(issisuby)
        print(f"Visualization based on {issisuby}.")
        filter_criteria = {}
        Filter_option = input("Do you want to add filter criteria? (yes=Y, No=N): ").strip().upper()
        if Filter_option == "Y":
            filter_values = []
            for attribute in datatype:
                filter_value = input(f"Enter the filter value for {attribute} (Press 'ENTER' or type 'xx' to skip): ").strip()
                if filter_value.lower() != 'xx' and filter_value:
                    filter_criteria[attribute] = filter_value
                    filter_values.append(filter_value)
        else:
            filter_values = None
        filtered_projects = []
        for project in self.greenstar.allprojects.values():
            match = True
            for key, value in filter_criteria.items():
                if key == 'companies' or key == 'organisations':
                    if not any(value.lower() in obj.name.lower() for obj in getattr(project, key)):
                        match = False
                        break
                else:
                    if str(getattr(project, key)).lower() != value.lower():
                        match = False
                        break
            if match:
                filtered_projects.append(project)
        return filtered_projects, issisuby, filter_values

    def save_visualization_data(self, data, issisuby, filter_values=None):
        filename = input("File save as: ").strip()
        if not filename.endswith(".json"):
            filename += ".json"
        try:
            with open(filename, "w") as file:
                visualization_data = {"visualization": data, "issisuby": issisuby, "filter_values": filter_values}
                json.dump(visualization_data, file, indent=5)
            print(f"Visualization data saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving visualization data: \n{e}")

    def read_and_visualize_data(self, filename):
        if not filename.endswith(".json"):
            filename += ".json"
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            print(f"Visualization data loaded successfully from {filename}") 
            if not data:
                print("No data to visualize.")
                return
            
            visualization_data = data.get("visualization", {})
            filter_values = data.get("filter_values", [])
            issisuby = data.get("issisuby")

            if visualization_data.get("type") == "pie":
                labels = list(visualization_data["data"].keys())
                sizes = list(visualization_data["data"].values())
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                if filter_values:
                    plt.title(f"Projects Issued By: {issisuby}\nFilter By: {filter_values}")
                else:
                    plt.title(f"Projects Issued By: {issisuby}")
                plt.show()

            elif visualization_data.get("type") == "bar":
                labels = list(visualization_data["data"].keys())
                sizes = list(visualization_data["data"].values())
                plt.figure(figsize=(10, 6))
                plt.bar(labels, sizes, color='skyblue')
                plt.xlabel('Categories')
                plt.ylabel('Values')
                plt.title("Visualization Based on Bar Chart")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif visualization_data.get("type") == "histogram":
                values = visualization_data["data"]
                plt.figure(figsize=(10, 6))
                plt.hist(values, bins=10, color='skyblue', edgecolor='black')
                plt.xlabel('Values')
                plt.ylabel('Frequency')
                plt.title("Visualization Based on Histogram")
                plt.tight_layout()
                plt.show()

            elif visualization_data.get("type") == "scatter":
                x_values = visualization_data["x_data"]
                y_values = visualization_data["y_data"]
                plt.figure(figsize=(10, 6))
                plt.scatter(x_values, y_values, color='skyblue', edgecolor='black')
                plt.xlabel('X-axis Values')
                plt.ylabel('Y-axis Values')
                plt.title("Visualization Based on Scatter Plot")
                plt.tight_layout()
                plt.show()

            else:
                print("Invalid visualization type.")

        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def drawPieChart(self):
        filtered_projects, issisuby, filter_values = self.filterProjects()
        if not filtered_projects:
            print("No projects to display based on the selected criteria.")
            return

        if isinstance(issisuby, list):
            for company_name in issisuby:
                count_dict = {}
                for project in filtered_projects:
                    if any(company_name.lower() in company.name.lower() for company in project.companies):
                        count_dict[company_name] = count_dict.get(company_name, 0) + 1
                if count_dict:
                    labels = list(count_dict.keys())
                    values = list(count_dict.values())
                    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
                    plt.title(f"Projects Filtered By Company: {company_name}")
                    plt.show()
        else:
            count_dict = {}
            for project in filtered_projects:
                key = getattr(project, issisuby)
                if isinstance(key, list):
                    key = ', '.join(key)
                count_dict[key] = count_dict.get(key, 0) + 1
            labels = list(count_dict.keys())
            values = list(count_dict.values())
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            filter_values_str = ', '.join(filter_values)
            plt.title(f"Projects Issued By: {issisuby.capitalize()}\nFilter By:{filter_values_str}")
            plt.show()

        self.save_visualization_data({"type": "pie", "data": count_dict}, issisuby, filter_values)

    def drawBarChart(self):
        filtered_projects, issisuby, filter_values = self.filterProjects()
        if not filtered_projects:
            print("No projects to display based on the selected criteria.")
            return
        count_dict = {}
        for project in filtered_projects:
            key = getattr(project, issisuby)
            if isinstance(key, list):
                key = ', '.join(key)
            count_dict[key] = count_dict.get(key, 0) + 1
        labels = list(count_dict.keys())
        values = list(count_dict.values())
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='skyblue')
        plt.xlabel(issisuby.capitalize())
        plt.ylabel('Number of Projects')
        filter_values_str = ', '.join(filter_values)
        plt.title(f"Projects Issued By: {issisuby.capitalize()}\nFilter By:{filter_values_str}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        self.save_visualization_data({"type": "bar", "data": count_dict}, issisuby, filter_values)

    def drawHistogram(self):
        filtered_projects, issisuby, filter_values = self.filterProjects()
        if not filtered_projects:
            print("No projects to display based on the selected criteria.")
            return
        values = []
        for project in filtered_projects:
            key = getattr(project, issisuby)
            if isinstance(key, (int, float)):
                values.append(key)
            elif isinstance(key, str) and key.isdigit():
                values.append(int(key))
            elif isinstance(key, str) and key.replace('.', '', 1).isdigit():
                values.append(float(key))
        if not values:
            print(f"No numeric values found for {issisuby}. Cannot generate histogram.")
            return
        plt.figure(figsize=(10, 6))
        plt.hist(values, bins=10, color='skyblue', edgecolor='black')
        plt.xlabel(issisuby.capitalize())
        plt.ylabel('Frequency')
        plt.title(f"Histogram of {issisuby.capitalize()}")
        plt.show()
        self.save_visualization_data({"type": "histogram", "data": values}, issisuby, filter_values)

    def drawScatterPlot(self):
        x_attr = input("Select attribute for x-axis: ").strip().lower()
        y_attr = input("Select attribute for y-axis: ").strip().lower()
        valid_datatypes = ["project_name", "location", "status", "rating", "score", "certified_date", "rating_tool", "companies", "organisations"]
        if x_attr not in valid_datatypes or y_attr not in valid_datatypes:
            print("Invalid attributes selected.")
            return
        filtered_projects, _, filter_values = self.filterProjects()
        if not filtered_projects:
            print("No projects to display based on the selected criteria.")
            return
        x_values = []
        y_values = []
        for project in filtered_projects:
            x_key = getattr(project, x_attr)
            y_key = getattr(project, y_attr)
            if isinstance(x_key, (int, float)) and isinstance(y_key, (int, float)):
                x_values.append(x_key)
                y_values.append(y_key)
            elif str(x_key).isdigit() and str(y_key).isdigit():
                x_values.append(int(x_key))
                y_values.append(int(y_key))
            elif str(x_key).replace('.', '', 1).isdigit() and str(y_key).replace('.', '', 1).isdigit():
                x_values.append(float(x_key))
                y_values.append(float(y_key))
        plt.figure(figsize=(10, 6))
        plt.scatter(x_values, y_values, color='skyblue', edgecolor='black')
        plt.xlabel(x_attr.capitalize())
        plt.ylabel(y_attr.capitalize())
        plt.title(f"Scatter Plot of {x_attr.capitalize()} vs {y_attr.capitalize()}")
        plt.tight_layout()
        plt.show()
        self.save_visualization_data({"type": "scatter", "x_data": x_values, "y_data": y_values}, f"{x_attr.capitalize()} vs {y_attr.capitalize()}", filter_values)

def main():
    greenstar = Greenstar()
    visual_analysis = VisualAnalysis(greenstar)
    while True:
        UserInput = input("Welcome to Greenstar\n  1: Add Project\n  2: Import Project\n  3: Export Project\n  4: Visualization and Generate Report\n  5: Exit\nSelect an option: ").strip()
        if UserInput == '1' or UserInput.lower() == "add project":
            greenstar.add_project()
        elif UserInput == '2' or UserInput.lower() == "import project":
            fileName = input("Enter the file name (json): ").strip()
            FileHandler.import_projects(fileName, greenstar)
            print()
        elif UserInput == '3' or UserInput.lower() == "export project":
            fileName = input("Enter the file name (json): ").strip()
            FileHandler.export_projects(fileName, greenstar.allprojects)
            print()
        elif UserInput == '4' or UserInput.lower() == "visualization and generate report":
            UserInput=input("visualization (1=Create New Report) or (2=Open Existing Report): ")
            if UserInput == '1':
                viz_option = input("Select visualization type:\n  1: Pie Chart\n  2: Bar Chart\n  3: Histogram\n  4: Scatter Plot\nSelect an option: ").strip()
                if viz_option == '1':
                    visual_analysis.drawPieChart()
                elif viz_option == '2':
                    visual_analysis.drawBarChart()
                elif viz_option == '3':
                    visual_analysis.drawHistogram()
                elif viz_option == '4':
                    visual_analysis.drawScatterPlot()
                else:
                    print("Invalid visualization option. Please select again.")
            else:
                filename = input("Enter the file name to load visualization data (json): ")
                visual_analysis.read_and_visualize_data(filename)

        elif UserInput == '5' or UserInput.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main()
