import os
import json

class JsonFileHandler:
    def ReadJsonFile(file_path):
        """
        Reads a JSON file from the specified file path and returns its content.

        :param file_path: The path to the JSON file.
        :return: A dictionary containing the JSON data.
        :raises FileNotFoundError: If the specified file does not exist.
        :raises ValueError: If the file content is not valid JSON.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")

        with open(file_path, encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error reading JSON file at {file_path}: {e}")

        return data
