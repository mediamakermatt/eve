import os
import urllib.request
import bz2

# Files we care about
FILES = [
    "invTypes.csv.bz2",
    "dgmTypeAttributes.csv.bz2",
    "dgmAttributeTypes.csv.bz2",
    "dgmTypeEffects.csv.bz2",
    "dgmEffects.csv.bz2",
    "invGroups.csv.bz2",
    "invCategories.csv.bz2",
    "invMarketGroups.csv.bz2",
    "invMetaTypes.csv.bz2",
    "industryBlueprints.csv.bz2",
    "invTypeMaterials.csv.bz2"
]

BASE_URL = "https://www.fuzzwork.co.uk/dump/latest/"
DEST_DIR = "sde_csv"

os.makedirs(DEST_DIR, exist_ok=True)

for file in FILES:
    url = BASE_URL + file
    local_bz2 = os.path.join(DEST_DIR, file)
    local_csv = local_bz2[:-4]  # remove .bz2

    print(f"📥 Downloading {file}...")
    urllib.request.urlretrieve(url, local_bz2)

    print(f"📦 Decompressing to {local_csv}...")
    with bz2.open(local_bz2, 'rb') as fr, open(local_csv, 'wb') as fw:
        fw.write(fr.read())

    os.remove(local_bz2)
    print(f"✅ Done: {local_csv}")

print("🎉 All selected CSV files downloaded and extracted.")
