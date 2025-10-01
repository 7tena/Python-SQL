# DBMS CheatSheet

### Basic Database Concepts
  - Database: Definition, types (Relational, NoSQL, etc.)
  - DBMS: Types (Hierarchical, Network, Relational, Object-Oriented, etc.)
  - Schema and Subschema
  - Data Independence: Logical and Physical data independence
  - ACID Properties: Atomicity, Consistency, Isolation, Durability
  - Normalization: 1NF, 2NF, 3NF, BCNF, and their use in eliminating redundancy
  - Denormalization: When and why it’s used

### SQL (Structured Query Language)
  - DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE
  - DDL (Data Definition Language): CREATE, ALTER, DROP
  - DCL (Data Control Language): GRANT, REVOKE
  - TCL (Transaction Control Language): COMMIT, ROLLBACK, SAVEPOINT
  - Joins: Inner join, Outer join (Left, Right, Full), Cross join, Self join
  - Subqueries: Nested queries, Correlated subqueries
  - Indexes: Purpose, types (Clustered, Non-clustered), pros/cons
  - Aggregate Functions: COUNT(), AVG(), SUM(), MIN(), MAX()
  - Group By and Having Clauses
  - Set Operations: UNION, INTERSECT, EXCEPT
  - Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), PARTITION BY

### Normalization and Denormalization
  - Normalization Process: How to move from unnormalized to 1NF, 2NF, 3NF, and BCNF
  - Denormalization: When it's used for performance optimization

### Database Design
  - Entity-Relationship (ER) Model: ER diagrams, Entities, Relationships, Attributes, Cardinality
  - Normalization: How to create tables and design schema efficiently
  - Keys: Primary Key, Foreign Key, Candidate Key, Composite Key, Alternate Key, Unique Key

### Transactions and Concurrency Control
  - Transaction: Definition, properties (ACID), examples
  - Transaction Management: COMMIT, ROLLBACK, and their use in maintaining transaction integrity
  - Concurrency Control: Locking mechanisms (Pessimistic vs Optimistic Locking)
  - Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable
  - Deadlock: Detection, prevention, and resolution strategies
  - Two-Phase Commit: For distributed transactions

### Indexes
  - Purpose of Indexing: Speeding up queries, creating efficient search paths
  - Types of Indexes: B-tree, Hash, Bitmap, Clustered, Non-clustered, Full-text
  - Indexing Strategies: When to use indexes, impact on performance (Read vs Write)

### Stored Procedures, Triggers, and Views
  - Stored Procedures: Definition, use cases, and advantages
  - Triggers: Purpose, how they work (e.g., AFTER, BEFORE triggers)
  - Views: Definition, advantages, when to use, and performance considerations

### Data Integrity and Constraints
  - Entity Integrity: Ensuring the primary key is unique and not NULL
  - Referential Integrity: Maintaining valid foreign key relationships
  - Check Constraints: Defining valid data ranges or conditions
  - Unique Constraints: Ensuring data uniqueness besides primary keys

### Advanced SQL Concepts
  - Joins Optimization: How to optimize joins for performance
  - Query Optimization: Index usage, execution plan, and performance tuning
  - Transactions in SQL: ACID properties, multi-step operations
  - Common Table Expressions (CTEs): Use cases for WITH statements

### Database Architecture
  - Client-Server Architecture: How databases are set up in a client-server model
  - Distributed Databases: Sharding, Replication, Partitioning
  - CAP Theorem: Consistency, Availability, Partition Tolerance in distributed systems
  - Data Warehousing: ETL processes, OLAP vs OLTP systems
  - NoSQL Databases: Types (Document, Columnar, Key-Value, Graph), when to use them
  - Cloud Databases: Concepts related to cloud-based DBMS (e.g., AWS RDS, Google BigQuery)

### Backup, Recovery, and Security
  - Backup Strategies: Full, Incremental, Differential backups
  - Recovery Techniques: Point-in-time recovery, Roll-forward and Roll-backward
  - Database Security: User roles, permissions, encryption, auditing
  - SQL Injection: What it is and how to prevent it

### Database Administration (DBA) Concepts
  - Database Maintenance: Regular backups, performance monitoring, tuning
  - Replication: Types of replication (Master-Slave, Peer-to-Peer)
  - Sharding and Partitioning: Techniques to split and distribute data across multiple machines
  - Capacity Planning: Estimating storage and hardware requirements based on usage

### Additional Topics (if time permits):
  - Big Data Concepts: Hadoop, MapReduce, NoSQL, and distributed data processing
  - Advanced Database Design Patterns: Star schema, Snowflake schema, Fact and Dimension tables (in Data Warehousing)
  - Graph Databases: Basics of graph databases (Neo4j)
