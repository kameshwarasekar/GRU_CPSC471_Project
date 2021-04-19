CREATE DATABASE gru;
\c gru
CREATE TABLE IF NOT EXISTS university(
	name text PRIMARY KEY,
	location text NOT NULL,
	description text NOT NULL,
	impact_on_industry text,
	finances int
);

CREATE TABLE IF NOT EXISTS degree(
	name text PRIMARY KEY,
	field text
);

CREATE TABLE IF NOT EXISTS provides(
	uni_name text REFERENCES university(name),
	degree_name text REFERENCES degree(name)
);

CREATE TABLE IF NOT EXISTS faculty(
	faculty_id serial PRIMARY KEY,
	name text NOT NULL,
	description text,
	uni_name text REFERENCES university(name)
);

CREATE TABLE IF NOT EXISTS major(
	major_code serial PRIMARY KEY,
	major_name text NOT NULL,
	no_of_years int NOT NULL,
	degree_name text REFERENCES degree(name),
	faculty_id int REFERENCES faculty(faculty_id)
);

CREATE TABLE IF NOT EXISTS entry_requirement(
	major_code int REFERENCES major(major_code),
	class_name text NOT NULL,
	grade int NOT NULL,
	CONSTRAINT erPK PRIMARY KEY(major_code, class_name)
);

CREATE TABLE IF NOT EXISTS equivalent_class(
	major_code int ,
	class_name text,
	name text NOT NULL,
	grade int NOT NULL,
	CONSTRAINT equiclassPK PRIMARY KEY(major_code, class_name, name),
	CONSTRAINT equiclassFK FOREIGN KEY(major_code, class_name) REFERENCES entry_requirement(major_code, class_name)
);

CREATE TABLE IF NOT EXISTS extra_curricular_program(
	name text PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS club(
	club_id serial PRIMARY KEY,
	name text REFERENCES extra_curricular_program(name),
	description text
);

CREATE TABLE IF NOT EXISTS sport(
	sport text PRIMARY KEY,
	name text REFERENCES extra_curricular_program(name)
);

CREATE TABLE IF NOT EXISTS award(
	sport text REFERENCES sport(sport),
	award_name text,
	year_awarded int,
	CONSTRAINT awardPK PRIMARY KEY(sport, award_name, year_awarded)
);

CREATE TABLE IF NOT EXISTS extracurricular_offerings(
	uni_name text REFERENCES university(name),
	excurricular_name text REFERENCES extra_curricular_program(name),
	CONSTRAINT exoPK PRIMARY KEY(uni_name, excurricular_name)
);

CREATE TABLE IF NOT EXISTS staff(
	staff_id serial PRIMARY KEY,
	position text NOT NULL,
	name text NOT NULL,
	uni_name text REFERENCES university(name)
);

CREATE TABLE IF NOT EXISTS professor(
	prof_id serial PRIMARY KEY,
	rating real,
	name text NOT NULL,
	uni_name text REFERENCES university(name),
	faculty_id int REFERENCES faculty(faculty_id)
);

CREATE TABLE IF NOT EXISTS field_of_study(
	prof_id int REFERENCES professor(prof_id),
	field_name text NOT NULL,
	CONSTRAINT fosPK PRIMARY KEY(prof_id, field_name)
);

CREATE TABLE IF NOT EXISTS course(
	course_code serial UNIQUE,
	course_number real,
	course_name text, 
	faculty_id int REFERENCES faculty(faculty_id),
	CONSTRAINT coursePK PRIMARY KEY(course_code, course_number)
);

CREATE TABLE IF NOT EXISTS course_teaching(
	course_code int,
	course_number real,
	prof_id int REFERENCES professor(prof_id),
	CONSTRAINT ctPK PRIMARY KEY(course_code, course_number, prof_id),
	CONSTRAINT ctFK FOREIGN KEY(course_code, course_number) REFERENCES course (course_code, course_number)
);

CREATE TABLE IF NOT EXISTS alumni(
	alumni_id serial PRIMARY KEY,
	name text NOT NULL,
	graduation_year int NOT NULL,
	achievement_description text,
	uni_name text REFERENCES university(name)
);

CREATE TABLE IF NOT EXISTS alumni_has(
	alumni_id int REFERENCES alumni(alumni_id),
	degree_name text REFERENCES degree(name),
	CONSTRAINT alumni_has_pk PRIMARY KEY (alumni_id, degree_name)
);

CREATE TABLE IF NOT EXISTS ranking(
	uni_code serial PRIMARY KEY,
	best_program text,
	rank int NOT NULL,
	prev_year_rank int,
	uni_name text REFERENCES university(name)
);

CREATE TABLE IF NOT EXISTS gru_user(
	user_id serial PRIMARY KEY,
	email text NOT NULL,
	name text,
	password text NOT NULL
);

CREATE TABLE IF NOT EXISTS preference(
	pref_id serial UNIQUE,
	user_id int REFERENCES gru_user(user_id),
	CONSTRAINT prefPK PRIMARY KEY(pref_id, user_id)
);

CREATE TABLE IF NOT EXISTS preferred_uni(
	pref_id int REFERENCES preference(pref_id),
	preferred_uni_name text,
	user_id int REFERENCES gru_user(user_id),
	CONSTRAINT prefuniPK PRIMARY KEY(pref_id, user_id)
);

CREATE TABLE IF NOT EXISTS preference_contain(
	pref_id int REFERENCES preference(pref_id),
	uni_name text REFERENCES university(name),
	user_id int REFERENCES gru_user(user_id),
	CONSTRAINT pcPK PRIMARY KEY(pref_id, uni_name, user_id)
);

INSERT INTO university VALUES 
(
	'University of Calgary',
	'Calgary, Alberta, Canada',
	'A public research university started in 1944 as a branch of the University of Alberta before becoming an autonomous university in 1966. It is composed of 14 faculties and over 85 research institutes and centres',
	'The University of Calgary is ranked one of the top 10 research universities in Canada and works to find solutions to some of the most challenging problems facing society',
	5594
);

INSERT INTO ranking VALUES
(
	DEFAULT,
	'Engineering',
	246,
	233,
	'University of Calgary'
);

INSERT INTO degree VALUES
(
	'Bachelor of Science',
	'Science'
);


INSERT INTO degree VALUES
(
	'Bachelor of Science in Engineering',
	'Engineering'
);

INSERT INTO degree VALUES
(
	'Bachelor of Arts',
	'Arts'
);

INSERT INTO provides VALUES
(
	'University of Calgary',
	'Bachelor of Science'
);

INSERT INTO provides VALUES
(
	'University of Calgary',
	'Bachelor of Science in Engineering'
);

INSERT INTO provides VALUES
(
	'University of Calgary',
	'Bachelor of Arts'
);

INSERT INTO faculty VALUES
(
	DEFAULT,
	'Faculty of Science',
	'University of Calgary'
);

INSERT INTO faculty VALUES
(
	DEFAULT,
	'Schulich School of Engineering',
	'University of Calgary'
);

INSERT INTO faculty VALUES
(
	DEFAULT,
	'Faculty of Art',
	'University of Calgary'
);

INSERT INTO major VALUES
(
	DEFAULT,
	'Computer Science',
	4,
	'Bachelor of Science',
	1
);


INSERT INTO major VALUES
(
	DEFAULT,
	'Mechanical Engineering',
	4,
	'Bachelor of Science in Engineering',
	2
);

INSERT INTO major VALUES
(
	DEFAULT,
	'Chemical Engineering',
	4,
	'Bachelor of Science in Engineering',
	2
);

INSERT INTO  entry_requirement VALUES
(
	1,
	'Math 30',
	70
);

INSERT INTO  equivalent_class VALUES
(
	1,
	'Math 30',
	'IB Math',
	5
);

INSERT INTO  equivalent_class VALUES
(
	1,
	'Math 30',
	'AP Calculus AB',
	4
);

INSERT INTO  entry_requirement VALUES
(
	2,
	'Physics 30',
	85
);

INSERT INTO  entry_requirement VALUES
(
	3,
	'Physics 30',
	80
);

INSERT INTO extra_curricular_program VALUES
(
	'Dinos'
);

INSERT INTO sport VALUES
(
	'Men''s Hockey',
	'Dinos'
);

INSERT INTO award VALUES
(
	'Men''s Hockey',
	'DR. W.G. Hardy Trophy - Canada West Champion',
	1996
);

INSERT INTO sport VALUES
(
	'Women''s Volleyball',
	'Dinos'
);

INSERT INTO award VALUES
(
	'Women''s Volleyball',
	'Canada West Champion',
	2005
);

INSERT INTO award VALUES
(
	'Women''s Volleyball',
	'Canada West Champion',
	2018
);

INSERT INTO extra_curricular_program VALUES
(
	'Birthday Wishes'
);

INSERT INTO club VALUES
(
	DEFAULT,
	'Birthday Wishes',
	'Student run organization devoted to providing underprivileged children (ages 4 - 12) from financially insecure homes with a birthday party'
);

INSERT INTO extra_curricular_program VALUES
(
	'Bouldering Club'
);

INSERT INTO club VALUES
(
	DEFAULT,
	'Bouldering Club',
	'"Bouldering is 10% climbing, 90% socializing." The Bouldering Club is entirely about encouraging new climbers and boulderers to give the sport a shot.'
);

INSERT INTO extracurricular_offerings VALUES
(
	'University of Calgary',
	'Dinos'
);

INSERT INTO extracurricular_offerings VALUES
(
	'University of Calgary',
	'Birthday Wishes'
);

INSERT INTO extracurricular_offerings VALUES
(
	'University of Calgary',
	'Bouldering Club'
);

INSERT INTO staff VALUES
(
	DEFAULT,
	'Janitor',
	'Marianna Lu',
	'University of Calgary'
);

INSERT INTO staff VALUES
(
	DEFAULT,
	'Librarian',
	'Dan Seward',
	'University of Calgary'
);

INSERT INTO professor VALUES
(
	DEFAULT,
	4.4,
	'Max Alexanderson',
	'University of Calgary',
	1
);

INSERT INTO professor VALUES
(
	DEFAULT,
	4.2,
	'Isabelle Mortensen',
	'University of Calgary',
	1
);

INSERT INTO professor VALUES
(
	DEFAULT,
	4.5,
	'Chris Vaccaro',
	'University of Calgary',
	2
);

INSERT INTO professor VALUES
(
	DEFAULT,
	4.3,
	'Ian Flynn',
	'University of Calgary',
	2
);

INSERT INTO field_of_study VALUES
(
	1,
	'Human Computer Interactions'
);

INSERT INTO field_of_study VALUES
(
	2,
	'Computer Security'
);

INSERT INTO field_of_study VALUES
(
	2,
	'Computer Graphics'
);

INSERT INTO field_of_study VALUES
(
	3,
	'Mechanical Engineering'
);

INSERT INTO field_of_study VALUES
(
	4,
	'Chemical Engineering'
);

INSERT INTO course VALUES
(
	DEFAULT,
	481,
	'Human Computer Interactions I',
	1
);

INSERT INTO course VALUES
(
	DEFAULT,
	329,
	'Explorations in Computer Security',
	1
);

INSERT INTO course VALUES
(
	DEFAULT,
	485,
	'Mechanical Engineering Thermodynamics',
	2
);

INSERT INTO course VALUES
(
	DEFAULT,
	501,
	'Transport Phenomena',
	2
);

INSERT INTO course_teaching VALUES
(
	1,
	481,
	1
);

INSERT INTO course_teaching VALUES
(
	2,
	329,
	2
);

INSERT INTO course_teaching VALUES
(
	3,
	485,
	3
);

INSERT INTO course_teaching VALUES
(
	4,
	501,
	4
);

INSERT INTO alumni VALUES
(
	DEFAULT,
	'Stephen Harper',
	1985,
	'22nd Prime Minister of Canada (2006 - 2015)',
	'University of Calgary'
);

INSERT INTO alumni VALUES
(
	DEFAULT,
	'James Gosling',
	1977,
	'Inventor of the Java programming language',
	'University of Calgary'
);

INSERT INTO alumni_has VALUES
(
	1,
	'Bachelor of Arts'
);

INSERT INTO alumni_has VALUES
(
	2,
	'Bachelor of Science'
);

INSERT INTO university VALUES
(
	'Massachusetts Institute of Technology',
	'Cambridge, Massachusetts, United States',
	'A private land-grant research university founded in 1861 and is regarded as one of the most prestigious universities in the world. The institute has an urban campus that extends more than a mile.',
	'MIT plays a key role in the developement of many aspects of modern science, engineering, mathematics, and technology and is widely known for its innovation and academic strength',
	53790
);

INSERT INTO ranking VALUES
(
	DEFAULT,
	'Engineering',
	1,
	1,
	'Massachusetts Institute of Technology'
);

INSERT INTO faculty VALUES
(
	DEFAULT,
	'School of Engineering',
	'Massachusetts Institute of Technology'
);

INSERT INTO faculty VALUES
(
	DEFAULT,
	'School of Science',
	'Massachusetts Institute of Technology'
);

INSERT INTO major VALUES
(
	DEFAULT,
	'Electrical Engineering',
	4,
	'Bachelor of Science',
	4
);

INSERT INTO major VALUES
(
	DEFAULT,
	'Brain and Cognitive Science',
	4,
	'Bachelor of Science',
	5
);

INSERT INTO entry_requirement VALUES
(
	4,
	'SAT Math',
	790
);

INSERT INTO equivalent_class VALUES
(
	4,
	'SAT Math',
	'ACT Math',
	35
);

INSERT INTO entry_requirement VALUES
(
	4,
	'SAT EBRW',
	730
);

INSERT INTO extra_curricular_program VALUES
(
	'Engineers'
);

INSERT INTO sport VALUES
(
	'Men''s Basketball',
	'Engineers'
);

INSERT INTO award VALUES 
(
	'Men''s Basketball',
	'NEWMAC Sports Tournament Champion',
	2018
);

INSERT INTO extra_curricular_program VALUES
(
	'Laboratory for Chocolate Science'
);

INSERT INTO club VALUES
(
	DEFAULT,
	'Laboratory for Chocolate Science',
	'A club dedicated to the appreciation of our favorite substance in all its myriad forms. Only group at MIT that orders more than 500lbs of chocolate a year.'
);

INSERT INTO extracurricular_offerings VALUES
(
	'Massachusetts Institute of Technology',
	'Engineers'
);

INSERT INTO extracurricular_offerings VALUES
(
	'Massachusetts Institute of Technology',
	'Laboratory for Chocolate Science'
);

INSERT INTO staff VALUES
(
	DEFAULT,
	'Janitor',
	'Tarina Alden',
	'Massachusetts Institute of Technology'
);

INSERT INTO professor VALUES
(
	DEFAULT,
	4.7,
	'Clint Adrichem',
	'Massachusetts Institute of Technology',
	4
);

INSERT INTO professor VALUES
(
	DEFAULT,
	4.1,
	'Soma Keo',
	'Massachusetts Institute of Technology',
	5
);

INSERT INTO field_of_study VALUES
(
	5,
	'Electrical Engineering'
);

INSERT INTO field_of_study VALUES
(
	6,
	'Neuroscience'
);

INSERT INTO field_of_study VALUES
(
	6,
	'Cognitive Science'
);

INSERT INTO course VALUES
(
	DEFAULT,
	6.013,
	'Electromagnetic Waves and Applications',
	4
);

INSERT INTO course VALUES
(
	DEFAULT,
	9.46,
	'Neuroscience of Morality',
	5
);

INSERT INTO course_teaching VALUES
(
	5,
	6.013,
	5
);

INSERT INTO course_teaching VALUES
(
	6,
	9.46,
	6
);

INSERT INTO alumni VALUES
(
	DEFAULT,
	'Rudolf E. Kalman',
	1953,
	'Won the Charles Stark Draper Prize in 2008 for the developement of the Kalman Filter.',
	'Massachusetts Institute of Technology'
);

INSERT INTO alumni_has VALUES
(
	3,
	'Bachelor of Science'
);

INSERT INTO provides VALUES
(
	'Massachusetts Institute of Technology',
	'Bachelor of Science'
);

