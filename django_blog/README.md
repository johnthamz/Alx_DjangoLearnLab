# Django Blog – Blog Post Management Features

## Overview
This project implements full blog post management functionality using Django. Authenticated users can create, update, and delete blog posts, while all users can view published posts.

---

## Features Implemented

### 1. Blog Post CRUD Operations
The blog supports full Create, Read, Update, and Delete (CRUD) functionality for posts using Django class-based views.

- **List Posts**
  - URL: `/posts/`
  - Accessible to all users
  - Displays all blog posts with title, snippet, author, and date

- **View Post Details**
  - URL: `/posts/<id>/`
  - Accessible to all users
  - Displays full post content

- **Create Post**
  - URL: `/posts/new/`
  - Authentication required
  - Author is automatically assigned based on the logged-in user

- **Update Post**
  - URL: `/posts/<id>/edit/`
  - Authentication required
  - Only the original author can edit their post

- **Delete Post**
  - URL: `/posts/<id>/delete/`
  - Authentication required
  - Only the original author can delete their post

---

## Permissions and Security

- Django’s `LoginRequiredMixin` ensures only authenticated users can create posts
- `UserPassesTestMixin` restricts editing and deleting posts to their authors
- CSRF protection is enabled for all forms
- Passwords are securely handled using Django’s built-in authentication system

---

## Forms
Blog post creation and editing is handled using a Django `ModelForm`, which validates input and securely manages user-submitted data.

---

## Templates
The following templates are used:
- `post_list.html` – display all posts
- `post_detail.html` – view single post
- `post_form.html` – create and update posts
- `post_confirm_delete.html` – confirm deletion

---

## Notes
This project uses Django class-based views for clean, reusable, and scalable code.


## Comment System

A comment system that allows users to interact with blog posts.

### Features
- View comments under each blog post
- Authenticated users can add comments
- Comment authors can edit or delete their comments

### Technical Details
- Each comment is linked to a specific blog post using a ForeignKey
- Permissions are enforced so only comment authors can modify their comments
- Django generic class-based views are used for CRUD operations
- CSRF protection is enabled for all comment forms

### Permissions
- Only logged-in users can post comments
- Only the comment author can edit or delete their comment

