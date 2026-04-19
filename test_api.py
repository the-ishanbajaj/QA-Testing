import requests

def test_delete_user():
    url = "https://jsonplaceholder.typicode.com/users/2"

    response = requests.delete(url)

    assert response.status_code== 200 , "error"

    json_data = response.json()

    assert json_data== {} , "not deleted"



# def test_update_user():
    
#     url = "https://jsonplaceholder.typicode.com/users/2"
#     payload = {
#          "name" : "QA Architect" ,
#          "username" : "qa_ninja" ,
#          "email" : "testing@enterprise.com"
#     }


#     response = requests.put( url ,json= payload )

#     assert response.status_code == 200 , f"error updating , says:{response.status_code}"

#     json_data = response.json()

#     assert json_data['name'] == "QA Architect" , "Not updated !"



# def test_create_new_user():
#     url = "https://jsonplaceholder.typicode.com/users"

#     payload = {
#         "name" : "QA Master" ,
#         "username" : "qa_ninja" ,
#         "email" : "testing@enterprise.com"
#     }
    
#     print()

#     response = requests.post(url , json=payload)
    
#     assert response.status_code == 201 , f"server rejected creation , says : {response.status_code}"
#     json_data = response.json()
#     assert json_data["name"] == "QA Master" , "Wrong user data returned !"


# def test_api_testing():

#     url = "https://jsonplaceholder.typicode.com/users/2"

#     response = requests.get(url)

#     assert response.status_code == 200 , f"fatal error"

#     json_data = response.json()

#     print(f"[DATA Recieved] {json_data}")

#     assert json_data['name'] == 'Ervin Howell' , "Wrong user data returned !"