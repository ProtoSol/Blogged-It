# Bloggedit Flask Application

## Overview
Bloggedit is a blogging platform project built with Flask. It allows users to register, log in, and create, update, or delete posts. The application supports user account management, including profile updates and password resets.

## Features

### User Authentication
- **Register**: Users can create an account with a unique username and email.
- **Login**: Secure login with email and password.
- **Logout**: End the user session.

### User Account Management
- **Update Account**: Users can update their profile information, including username, email, and profile picture.
- **Password Reset**: Allows users to reset their password via email, but not working at the moment.

### Post Management
- **Create Posts**: Authenticated users can create new posts.
- **Edit Posts**: Authenticated users can update their existing posts.
- **Delete Posts**: Authenticated users can delete their posts.
- **View Posts**: All users can view posts, filtered by author or displayed in a paginated feed.

### Additional Features
- **Profile Pictures**: Users can upload and update profile pictures.
- **Pagination**: Posts are displayed in a paginated format on the homepage and user-specific pages.

## Technologies Used
- **Flask**: Core web framework.
- **Flask-WTF**: For form handling and validation.
- **Flask-Login**: For user session management.
- **Flask-Mail**: For email-based password resets (disabled in the current version).
- **Flask-Bcrypt**: For password hashing.
- **SQLite**: For database management.
- **Pillow**: For image processing (profile pictures).

## Usage
1. Register for an account.
2. Log in to access the dashboard.
3. Create, update, or delete posts.
4. Update your account details from the account page.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any feature additions or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Note
This project is still under development and will be updated later, and the Reset password logic will be implemented again.