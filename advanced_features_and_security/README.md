# LibraryProject 
Initial Django project setup for the ALX Django LearnLab.
This is my first Django project created for the ALX Django Learning Lab.

# LibraryProject Permissions Setup

## Groups & Permissions

### Groups
- **Viewers**: Can view books only (`can_view`)
- **Editors**: Can create and edit books (`can_create`, `can_edit`)
- **Admins**: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete`)

### Testing
1. Create users and assign them to the appropriate group.
2. Log in and test that access is enforced according to group permissions.

