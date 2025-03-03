# import requests
#
# response = requests.get(url=" https://jsonplaceholder.typicode.com/users/5/posts")
# # print(response.status_code)
# # print(response.text)
# # print(response.json())
#
# posts = response.json()
#
# for index in range(0, 3):
#     print(f'PostUser: {posts[index]["userId"]}, PostID: {posts[index]["id"]}, Post title: {posts[index]["title"]}, Post body: {posts[index]["body"]}')
#
# postari_ramase = len(posts) - 3
#
# print(f"Postari ramase {postari_ramase}")
#
#
# todo = requests.get(url='https://jsonplaceholder.typicode.com/users/10/todos')
# print(todo.status_code)
# print(todo.text)
# print(todo.json())
#
#
# posts = todo.json()
# for i in range(0, 3):
#     print(f'userId: {posts[i]["userId"]} post_id:{posts[i]["id"]}, title:{posts[i]["title"]}, completed:{posts[i]["completed"]}')
# postari_ramase = len(posts) - 3
#
#
# print(f'Au mai ramas {postari_ramase} postari ramase')
#
#

"""INCERCARE"""
import requests

# def get_informations(URL: str, *elem):
#     request = requests.get(url=URL)

"""ALBUMS"""

# information = {
#     "userId": 2,
#     "title": "Titlu nou"
# }
#
# request = requests.post(url="https://jsonplaceholder.typicode.com/albums", json=information)
# albums = request.json()
#
# print(albums)

"""TODOS"""

todos = {
    "userId": 10,
    "title": "Lista evenimente",
    "completed": True
}

request_todos = requests.post(url="https://jsonplaceholder.typicode.com/todos", json=todos)
todos1 = request_todos.json()

print(todos1)
