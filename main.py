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

                try:
                    tree = ET.parse(xml_path)
                    root = tree.getroot()

                    # found to first element
                    first_name_element = root.find(".//name")
                    if first_name_element is None:
                        print(f"Uyarı: <name> etiketi bulunamadı - {xml_path}")
                        continue
                    first_name = first_name_element.text

                    # create subfolder
                    label_dir = os.path.join(output_dir, first_name)
                    os.makedirs(label_dir, exist_ok=True)

                    # Determining target file paths
                    target_xml_path = os.path.join(label_dir, xml_file_name)
                    target_image_path = os.path.join(label_dir, file)

                    # Overwrite a file with the same name if it exists
                    if os.path.exists(target_xml_path):
                        print(same_data_count, f"--> Bilgi: {target_xml_path} dosyası üzerine yazılacak.")
                        same_data_count += 1
                    if os.path.exists(target_image_path):
                        print(f"Bilgi: {target_image_path} dosyası üzerine yazılacak.")

                    # Move the XML and image file to the subfolder
                    shutil.move(xml_path, target_xml_path)
                    shutil.move(os.path.join(subdir, file), target_image_path)

                except ET.ParseError:
                    print(f"Uyarı: XML dosyası parse edilemedi - {xml_path}")
                    continue

root_directory = r"D:\0609_yolodata_v2\val_e"
output_directory = r"D:\0609_yolodata_v2\val_e_split"
organize_images_by_label(root_directory, output_directory)