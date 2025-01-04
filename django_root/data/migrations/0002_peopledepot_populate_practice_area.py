import os
import json
from django.db import migrations

PEOPLE_DEPOT_URL = os.environ.get("PEOPLE_DEPOT_URL", default="")

def update_from_json_file():
    from people_depot.models import PracticeArea

    file_spec = os.path.join(
        BASE_DIR, "data/people_depot/practice_area_export.json"
    )
    print("Updating PracticeArea from practice_area_export.json")
    f = open(file_spec, "r")
    data = json.load(f)
    for record in data:
        PracticeArea.objects.get_or_create(name=record["fields"]["name"])

def run(__apps__, __schema_editor__):
    if not PEOPLE_DEPOT_URL:
        update_from_json_file

class Migration(migrations.Migration):
    dependencies = [("data", "0001_peopledepot_populate_user")]
    operations = [migrations.RunPython(run, migrations.RunPython.noop)]
