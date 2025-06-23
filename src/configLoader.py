import yaml
import os

class ConfigLoader:
    CONFIG_FOLDER_NAME = "conf"
    CONFIG_FILE_NAME = "conf.yml"

    def __init__(self):
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.join(current_script_dir, '..')
        self.config_path = os.path.join(project_root, self.CONFIG_FOLDER_NAME, self.CONFIG_FILE_NAME)

        print(f"Loading config from: {self.config_path}")
        try:
            with open(self.config_path, 'r') as file:
                self.data = yaml.safe_load(file)
            if self.data is None:  # Si le fichier YAML est vide
                self.data = {}
            print("Configuration loaded successfully.")
        except FileNotFoundError:
            print(f"Error: Configuration file not found at {self.config_path}")
            self.data = {}  # Assurez-vous que self.data est un dictionnaire vide en cas d'erreur
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            self.data = {}

    def get_active_pairs(self):
        """
        Filters the pairs and returns only those with 'active: 1'.
        """
        active_pairs = {}
        if 'pairs' in self.data and isinstance(self.data['pairs'], dict):
            for pair_name, pair_details in self.data['pairs'].items():
                # Check if 'active' key exists and its value is 1
                if isinstance(pair_details, dict) and pair_details.get('active') == 1:
                    active_pairs[pair_name] = pair_details
        return active_pairs


CONFIG = ConfigLoader()
