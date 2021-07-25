import requests

# ------------------------------------------delete parameters---------------------------------------------
# url = 'https://www.w3schools.com/python/showpython.asp?filename=demo_requests_delete_allow_redirects'
# x=requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(x.status_code)
# # print(x.text)
#
# # print(x.raise_for_status())
# # print(x.links)
# # print(x.json())
# # print(x.iter_lines())
# # for item in x.iter_lines():
# #     print(item)
# # print(x.iter_content())
# # for item in x:
# #     print(item)
# # print(x.is_permanent_redirect)
# # print(x.history)
# print(x.headers)
#
# # print(x.encoding)
# # print(x.elapsed)
#
# # print(x.cookies)
# # x.close()
# # # print(x.apparent_encoding)

# url = 'http://w3schools.com/python/demopage.htm'
#
# #first, make a request without setting the 'allow_redirects' parameter to False:
# x = requests.get(url)
# print(x.text)
#
# print("----------------")

#then, make a request with the 'allow_redirects' parameter set to False:
# x = requests.get(url, allow_redirects=False)
# print(x.text)

#
# url = 'https://www.w3schools.com/python/showpython.asp?filename=demo_requests_post_json'
# myjson = {'somekey': 'somevalue'}
#
# x = requests.post(url, json = myjson)
#
#
#
# print(x.text)


"""
_________________________________import os________________________________________
def current_path():
    print("print before a value")
    print(os.getcwd())
    print()
"""



import os


# fd = "gfs.txt"
#
# file=open(fd,"w")
# file.write("hello")
# file.close()
# file=open(fd,"r")
# text=file.read()
# print(text)

# file = os.popen(fd, 'w')
# file.write("Hello")

# os.remove("gfs.txt")
# size = os.path.getsize("hetfood.txt")
#
# print("Size of the file is", size, " bytes.")