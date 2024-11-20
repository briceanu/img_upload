import requests
import sys

 
def create_user():
    url = 'http://localhost:8000/api/user/'

    # Open the file and ensure it remains open during the request
    with open('./car3.jpg', 'rb') as file:
        files = {'user_img': file}
        data = {'username':'aw'}

        # Make the request inside the with block
        res = requests.post(url=url,data=data, files=files)

    print(res.status_code)
    print(res.text)


if __name__ == '__main__':
    if sys.argv[1] == 'create_list':
        create_user()
