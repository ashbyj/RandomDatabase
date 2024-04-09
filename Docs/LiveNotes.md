- do i have to load the db correctly the first time or can i clean it up after?

- contest table should be the first to be populated
    - this will be tough from the erd, how do i decide which to start with?  is it necessary to know which or can i clean them up after?

- contest table should have multiple instances of a contest_id but contest_id, hacker_id should be unique.  
    - this may move the composite key feature up in the roadmap

- should i load data as a stream or in one push (maybe from a np array?)

- would it be better to try to hold the data generated in memory or rely on a successful db write and then use sql to populate domains for other tables?