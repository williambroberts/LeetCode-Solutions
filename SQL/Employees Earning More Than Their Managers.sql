select ee.name as Employee from employee ee
join employee em
on em.id = ee.managerid 
where ee.salary > em.salary
