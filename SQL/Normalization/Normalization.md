<<<<<<< HEAD:SQL/Normalization/Normalization.md
Normalization is the process of organizing data to minimize redundancy.

- 1NF (First Normal Form): Eliminates duplicate columns from the same table.
- 2NF (Second Normal Form): Removes subsets of data that apply to multiple rows and places them in separate tables.
- 3NF (Third Normal Form): Removes columns that are not dependent upon the primary key.
- BCNF (Boyce-Codd Normal Form): A stronger version of 3NF; deals with certain types of anomaly not handled by 3NF.
=======
Normalization is the process of organizing data to minimize redundancy.

- 1NF (First Normal Form): Eliminates duplicate columns from the same table.
- 2NF (Second Normal Form): Removes subsets of data that apply to multiple rows and places them in separate tables.
- 3NF (Third Normal Form): Removes columns that are not dependent upon the primary key.
- BCNF (Boyce-Codd Normal Form): A stronger version of 3NF; deals with certain types of anomaly not handled by 3NF.

Denormalization is the process of combining normalized tables to improve read performance.

When to Use:
- When read performance is critical.
- To reduce the complexity of queries involving multiple joins.

Why Use:
- To improve query performance by reducing the number of joins.
- To simplify the database schema for certain applications.
>>>>>>> 7ed9aa8e62ae3ba6649ad595b545b4d7642e460b:Cheatsheet/Normalization/Normalization.md
