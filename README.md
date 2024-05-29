# Best Version of Yourself REST API

## API Endpoints

### Users:

- `POST /users/signup`
    - Description: Create a new user.
    - Response: The created user object.
- `POST /token`
    - Description: Logs in user and returns token
- `POST /token/refresh`
    - Description: Refreshes token
- `GET /user`
    - Description: Gets user profile if the token is validated
    - Authentication: Required
- `GET /user/communities`
    - Description: Gets all communities a user has joined
    - Authentication: Required

### Communities:

- `POST /communities`
    - Description: Create a new community and the user creating it automatically becomes admin of the community
    - Authentication: Required
- `GET /communities`
    - Description: Gets all communities
    - Authentication: Not Required
- `GET /communities/<id>`
    - Description: Gets community by id
- `DELETE /communities/<id>`
    - Description: Deletes a community
- `PUT /communities/<id>`
    - Description: Updates a community's data

### Community Members:

- `POST /communities/<id>/members/`
    - Description: Create a new community
- `DELETE /communities/<id>/members`
    - Description: Create a new community


