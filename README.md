# Library Web App

This web app is a library management system that allows the fast and simple transferring, returning and management of books.
<br/>
# Note
If you are running it locally, you must have django 3.2 installed. Go to the library folder with manage.py and run the command "python manage.py runserver" in the terminal. Then, go to the link given in the terminal or go to localhost:8000.
<br/>

## Table of Contents  
 - [User Login/Register](#user-login)  
 - [Member](#member)
 - [Librarian](#librarian)
 - [Search](#search)  
 - [Admin](#admin)

<br/>
<a name="user-login"/>

## User Login
On going to the link, it redirects you to a login page, where you can enter your username and password. If you don't have an account, there is a link where you can register.

<br/>
<img src="pics/login.PNG">
<img src="pics/register.PNG"> 
<br/>
<a name="member"/>

## Member

The user can see the list of all the books available and can see the details of each book.
<br/>
<img src="pics/books_member.PNG">
<br/>
If the user is not a librarian, the can comment on the book, give it a rating or borrow it by specifying the return date. 
<br/>
<img src="pics/book_page_member.PNG">
<br/>
If their request is accepted, they can choose to either return the book or renew their return date.
<br/>
<img src="pics/borrowed_member.PNG">
<br/>
Users can also see their details in their homepage along with their accepted, pending and rejected requests.
<br/>
<img src="pics/my_books.PNG">
<img src="pics/pending_request.PNG">
<img src="pics/rejected_requests.PNG">
<br/>
<a name="librarian"/>

## Librarian
If the user is a librarian, they can edit or delete any book. 
<br/>
<img src="pics/book_page_librarian.PNG">
<img src="pics/edit_book.PNG">
<br/>
They can also see all the pending requests and renew requests and can choose to accept or reject them.
<br/>
<img src="pics/requests_librarian.PNG">
<br/>
<a name="search"/>


## Search

Members and librarians can also use the search bar to help them find books based on the books' title, author, location etc.
<br/>
<img src="pics/search.PNG">
<br/>
<a name="admin"/>


## Admin
<img src="pics/admin_page.PNG">
<br/>
If the user is an admin, they can see all the users and comments. 
<br/>
<img src="pics/users.PNG">
<img src="pics/comments.PNG">
<br/>
The admin can make a member a librarian and vise-versa along with editing and deleting any user or comment.
<br/>
<img src="pics/edit_users.PNG">
<img src="pics/edit_comment.PNG">
<br/>

Admins also have their own ligin page, in which only admins can login.
<br/>
<img src="pics/admin_login.PNG">

