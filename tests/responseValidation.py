response = {
    "status": "success",
    "code": 200,
    "message": "User data retrieved successfully",
    "data": {
        "user": {
            "id": 10243,
            "firstName": "Jane",
            "email": "jane.doe@example.com",
            "isActive": True,
            "roles": ["Developer", "Admin"]
        }
    }
}          

#Write a function check_roles(resp) that returns True only if roles is a list.

def check_roles(resp):
    roles = resp["data"]["user"]["roles"]
    if isinstance(roles, list):
        return True
    else:
        return False

print(check_roles(response))



