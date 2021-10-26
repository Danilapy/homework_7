import os.path

project_path = 'my_project'
paths = ['settings', 'mainapp', 'adminapp','authapp']

for p in paths:
    os.makedirs(os.path.join(project_path, p), exist_ok=True)

