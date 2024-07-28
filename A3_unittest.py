import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import matplotlib.pyplot as plt
from Tonmoy_A3 import Project, Company, Organisation, Greenstar, FileHandler, VisualAnalysis

class TestGreenstar(unittest.TestCase):

    def setUp(self):
        self.greenstar = Greenstar()
        self.visual_analysis = VisualAnalysis(self.greenstar)
        self.project1 = Project("Project A", "Location A", "Certified", 4, "80", "01012020", "V1", ["Company A"], [Organisation("Org A", "Role A")])
        self.project2 = Project("Project B", "Location B", "Registered", 3, "70", "02022021", "V2", ["Company B"], [Organisation("Org B", "Role B")])
        self.greenstar.allprojects = {
            self.project1.project_name: self.project1,
            self.project2.project_name: self.project2
        }

    def test_add_project(self):
        with patch('builtins.input', side_effect=[
            'Project C', 'Location C', '1', '5', '90', '03-03-2022', 'V3', '', 'xx', '', 'xx'
        ]):
            self.greenstar.add_project()
            self.assertIn("Project C", self.greenstar.allprojects)
            self.assertEqual(self.greenstar.allprojects["Project C"].location, "Location C")
            self.assertEqual(self.greenstar.allprojects["Project C"].status, "Certified")
            self.assertEqual(self.greenstar.allprojects["Project C"].rating, 5)

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{
        "project_name": "Project D",
        "location": "Location D",
        "status": "Certified",
        "rating": 5,
        "score": "95",
        "certified_date": "04042022",
        "rating_tool": "V4",
        "companies": ["Company D"],
        "organisations": [{"name": "Org D", "role": "Role D"}]
    }]))
    def test_import_projects(self, mock_file):
        FileHandler.import_projects("dummy.json", self.greenstar)
        self.assertIn("Project D", self.greenstar.allprojects)
        self.assertEqual(self.greenstar.allprojects["Project D"].location, "Location D")
        self.assertEqual(self.greenstar.allprojects["Project D"].status, "Certified")

    @patch("builtins.open", new_callable=mock_open)
    def test_export_projects(self, mock_file):
        filename = "export_test.json"
        FileHandler.export_projects(filename, self.greenstar.allprojects)
        mock_file.assert_called_once_with(filename, "w")
        handle = mock_file()
        handle.write.assert_called()

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "visualization": {"type": "pie", "data": {"A": 1, "B": 2, "C": 3}},
        "issisuby": "location",
        "filter_values": None
    }))
    def test_read_and_visualize_data(self, mock_file):
        with patch.object(plt, 'show'):
            self.visual_analysis.read_and_visualize_data("test_visualization_data.json")



    def test_drawPieChart(self):
        with patch.object(self.visual_analysis, 'filterProjects', return_value=(
            [self.project1, self.project2], 'location', [])):
            with patch.object(plt, 'show'):
                self.visual_analysis.drawPieChart()

    def test_drawBarChart(self):
        with patch.object(self.visual_analysis, 'filterProjects', return_value=(
            [self.project1, self.project2], 'location', [])):
            with patch.object(plt, 'show'):
                self.visual_analysis.drawBarChart()

if __name__ == "__main__":
    unittest.main()
