create schema hackerrank;

create table hackerrank.contest (
	contest_id int 
	, hacker_id int 
	, hacker_name varchar
);

create table hackerrank.college (
	college_id int 
	, contest_id int 
);

create table hackerrank.challenge ( 
	challenge_id int 
	, college_id int 
);

create table hackerrank.view_stat (
	challenge_id int 
	, total_views int 
	, total_unique_views int 
);

create table hackerrank.submission_stat (
	challenge_id int 
	, total_submissions int 
	, total_accepted_submissions int 
);


	