import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image 
import zipfile
import shutil
import requests
import os
import uuid
from collections import Counter

from yolo.config import Config
from tools import decoder


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

@st.cache
def calculate(file):
	if file.type == 'application/x-zip-compressed':
		archieve = zipfile.ZipFile(file=file)
		archieve.extractall(f'.cache/{file.name}/')
		image_names = os.listdir(f'.cache/{file.name}/')
		image_paths = [os.path.join(f'.cache/{file.name}/', name) for name in image_names]

	else:
		img = load_image(file)
		img.save(f'.cache/{file.name}/{file.name}')
		image_paths = [os.path.join(f'.cache/{file.name}/', p) for p in os.listdir(f'.cache/{file.name}/')]

	r = requests.post(f"{Config.YOLO_SERVICE_PATH}/predict", json={'image_paths' : image_paths, 
																 		'file_name' : file.name})
	classes = decoder(r.content)

	return classes


def show_results(option_type, classes, option_count, file):
	if option_type == "all":
		for key, value in list(classes.items())[:option_count]:
			predicted_image = Image.open(f'.cache/{file.name}_results/{key}.jpg')
			st.image(predicted_image)
			st.text(f"Имя файла: {key}")
			string = ''
			for key, value in Counter(Counter(value)).items():
				string += f"{key} : {value} "
			st.text(f"Количество дефектов: {string}")
			
	else:
		for key, value in list(classes.items())[:option_count]:
			if option_type in value:
				predicted_image = Image.open(f'.cache/{file.name}_results/{key}.jpg')
				st.image(predicted_image)
				st.text(f"Имя файла: {key}")
				string = ''
				for key, value in Counter(Counter(value)).items():
					string += f"{key} : {value} "
				st.text(f"Количество дефектов: {string}")
def main():

	menu = ["Определение деффектов"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Определение деффектов":
		st.subheader("Определение деффектов")

		file = st.file_uploader("Upload File",type=['png','jpeg','jpg', 'zip'])
		print("Загрузка файла")

		if file is not None:

			if not os.path.isdir(f'./.cache/{file.name}'):
				os.mkdir(f'./.cache/{file.name}')
			else:
				shutil.rmtree(f'.cache/{file.name}')
				os.mkdir(f'./.cache/{file.name}')
			
			classes = calculate(file)

			shutil.make_archive(f'.cache/{file.name}_results', 'zip', f'.cache/{file.name}_results')
				
		
			btn = st.download_button(
						label="Download results",
						data=open(f'.cache/{file.name}_results.zip', "rb"),
						file_name=f'.cache/{file.name}_results.zip',
						mime= 'application/x-zip-compressed'
					)


			option_type = st.selectbox("Вид дефекта",
									("all",
									"adj", 
		  							"int", 
									"geo",
									"pro",
									"non", 
									 ))
			
			option_count = st.selectbox("Показать",
									(1,
									5, 
									10, 
									25,
									100,
									"all"))
			
			if option_count == "all":
				option_count = -1
			
			show_results(option_type, classes, option_count, file)


if __name__ == '__main__':
	main()
	