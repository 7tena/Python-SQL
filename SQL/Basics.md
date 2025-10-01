# Basics

- USE {db name}
- Standard date: YYYY-MM-DD
- LIKE '_ _ _ Y' : Four letter word ending with Y
- REGEXP
  - No %
  - ^ : bgeinning with
  - $ : ending with
  - 'filed|rose|mac' : any of these words
  - '[gim]e' : g or i or m but e
  - '[a-f]': a to f
  - LIMIT 3 : first 3 rows
  - LIMIT 6,3 : skip first 6, then take 3
 
### Indexing
- Clustered: employee id
- Non clustered: employee name
- Read execution plan from right to left and top to bottom 
