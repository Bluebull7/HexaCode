import os

docs_dir = "public/docs"
for root, _, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace _static/ with /docs/_static/
            updated_content = content.replace('_static/', '/docs/_static/')

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

            print(f"Updated paths in {file_path}")

