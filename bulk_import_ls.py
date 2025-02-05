import os

from label_studio_sdk import Client
from tqdm import tqdm

# Connect to Label Studio
LABEL_STUDIO_URL = "http://localhost:8080"  # Update with your Label Studio URL
API_KEY = "525f61f0196adaf4a89d9d980e424d636f0b10a3"  # Replace with your API key
PROJECT_ID = 11  # Replace with your project ID

ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
project = ls.get_project(PROJECT_ID)

# Path to your local image folder
image_folder = "/mnt/c/Users/abdulrehman/PycharmProjects/traffic_signs_training_yolo_arabic/results_testing/develop_dataset_from_vid_frames/zoomed_cropped_dataset"

tasks = []

# Uploading files and preparing task definitions

with tqdm(total=len(os.listdir(image_folder)), desc="Uploading files", unit="file") as progress_bar:
    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith(('.jpg', '.png', '.jpeg')):
            image_file_path = os.path.join(image_folder, image_file)

            # Upload file to Label Studio backend
            with open(image_file_path, 'rb') as f:
                upload_response = ls.make_request(
                    'POST',
                    f'/api/projects/{PROJECT_ID}/import',
                    files={'file': f}
                )

            # Parse the JSON response
            progress_bar.update(1)
            try:
                response_data = upload_response.json()
            except ValueError as e:
                print(f"Failed to parse JSON response for file {image_file}: {e}")
                continue

            # Check if 'file_upload' and 'path' keys exist
            uploaded_file_path = ""
            tasks.append({
                "data": {
                    "file_upload": response_data['file_upload_ids'][0]
                }
            })

# Close the progress bar
progress_bar.close()
