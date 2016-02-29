import sys
import fileinput
import os

# replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th

def add_all_urls(file_path):
    for i, line in enumerate(fileinput.input(file_path, inplace = 1)):
        sys.stdout.write(line.replace(r'"clipboardRead"', r'"clipboardRead","<all_urls>"'))  # replace 'sit' and write

def manifest_mover(debug_json_file, manifest_json_file):
    if os.path.isfile(debug_json_file):
        add_all_urls(debug_json_file)
        os.remove(manifest_json_file)
        os.renames(debug_json_file, manifest_json_file)
    else:
        add_all_urls(manifest_json_file)

if __name__ == "__main__":
#     debug_json_file = r'/Users/pavang/Projects/html-office/crx/app/manifest_debug.json'
#     menifest_json_file = r'/Users/pavang/Projects/html-office/crx/app/manifest.json'

    base_debug_json_file = r'/home/synerzip/Projects/c2c/baseBuild/html-office/crx/app/manifest_debug.json'
    base_manifest_json_file = r'/home/synerzip/Projects/c2c/baseBuild/html-office/crx/app/manifest.json'
    manifest_mover(base_debug_json_file, base_manifest_json_file)
    
    compare_debug_json_file = r'/home/synerzip/Projects/c2c/compareBuild/html-office/crx/app/manifest_debug.json'
    compare_manifest_json_file = r'/home/synerzip/Projects/c2c/compareBuild/html-office/crx/app/manifest.json'
    manifest_mover(compare_debug_json_file, compare_manifest_json_file)



    

    