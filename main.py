import os
import shutil
import xml.etree.ElementTree as ET


def organize_images_by_label(root_dir, output_dir):
    same_data_count = 0
    # scanning folders
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                # found path to xml file
                xml_file_name = os.path.splitext(file)[0] + ".xml"
                xml_path = os.path.join(subdir, xml_file_name)

                if not os.path.exists(xml_path):
                    print(f"Uyarı: XML dosyası bulunamadı - {file}")
                    continue