from aip import AipOcr

config = {
    'appId': '19535423',
    'apiKey': 'pnyWRrZ0YssbfoGmEbgu7wyr',
    'secretKey': 'ARBxjyKIITvbVnU5pjcP8k3mlg59vn7S'
}
client = AipOcr(**config)
def get_file_content(file):
    with open (file,"rb") as f:
        return f.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.handwriting(image)

    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])
response = img_to_str(r'C:\Users\liuxiangbiao\Desktop\2.png')
print(response)
