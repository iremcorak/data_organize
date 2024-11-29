import os
import shutil
import xml.etree.ElementTree as ET


def find_and_copy_images_by_label(source_directory, output_path, label_name):
    # Belirtilen etiket adı için bir klasör oluştur
    label_folder = os.path.join(output_path, label_name)
    os.makedirs(label_folder, exist_ok=True)

    # Kaynak klasörde ve alt klasörlerdeki dosyaları tarar
    for root, _, files in os.walk(source_directory):
        for file in files:
            # Yalnızca .xml dosyalarını kontrol et
            if file.lower().endswith('.xml'):
                xml_path = os.path.join(root, file)

                # XML dosyasını oku ve belirli etiket adını ara
                try:
                    tree = ET.parse(xml_path)
                    root_element = tree.getroot()

                    # Eğer XML içerisinde "name" etiketi olarak belirtilen label_name varsa
                    for element in root_element.iter('name'):
                        if element.text and element.text.lower() == label_name.lower():
                            # Aynı isimdeki resim dosyasını bul ve kopyala
                            base_name = os.path.splitext(file)[0]
                            for ext in ['.png', '.jpg']:
                                image_path = os.path.join(root, base_name + ext)
                                if os.path.exists(image_path):
                                    shutil.copy(image_path, label_folder)
                                    print(f"Resim dosyası kopyalandı: {image_path}")

                            # XML dosyasını kopyala
                            shutil.copy(xml_path, label_folder)
                            print(f"XML dosyası kopyalandı: {xml_path}")

                            # Etiket bulunduğu için döngüyü kır (aynı dosya tekrar kontrol edilmez)
                            break
                except ET.ParseError as e:
                    print(f"Hata oluştu: {xml_path} dosyası işlenemedi. Hata: {e}")


# Kullanım örneği
source_directory = r'D:\class_all'  # Tarayacağınız klasörün yolunu buraya yazın
output_path = r'D:\single_class'  # Kopyalama işleminin yapılacağı yol

# Etiket adı doğrudan programda tanımlandı
label_name = "kedi"

find_and_copy_images_by_label(source_directory, output_path, label_name)
