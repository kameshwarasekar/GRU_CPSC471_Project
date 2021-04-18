--SQL statement examples for transactions (not functional directly. variable names used in place of actual values)


--POST http://localhost:8000/gruUser-create/

INSERT INTO gru_user (user_id, email, name, password)
VALUES (null, input_email, input_name, input_password);

--GET http://localhost:8000/gruUser

SELECT * FROM gru_user;

--DEL http://localhost:8000/gruUser-delete/:user_id

DELETE FROM gru_user WHERE user_id = input_user_id; --user_id on right is input value

--PUT http://localhost:8000/gruUser-update/:user_id

UPDATE gru_user
SET email = input_email, name = input_name, password = input_pass
WHERE user_id = user_id; --user_id on right is input value

--POST http://localhost:8000/preference-create/

INSERT INTO preference (pref_id, user_id)
VALUES (pref_id, user_id);

--GET http://localhost:8000/preference/

SELECT * FROM preference;

--DEL http://localhost:8000/preference-delete/:pref_id

DELETE FROM preference WHERE pref_id = input_pref_id;

--POST http://localhost:8000/preferenceContain-create/

INSERT INTO preference_contain (pref_id, uni_name, user_id)
VALUES (input_pref_id, input_uni_name, input_user_id);

--GET http://localhost:8000/preferenceContain/

SELECT * FROM preference_contain;

--GET http://localhost:8000/preferenceContain/:pref_id

SELECT * FROM preference_contain WHERE pref_id = input_pref_id;

--PUT http://localhost:8000/preferenceContain-update/:pref_id

UPDATE preference_contain
SET uni_name = input_uni_name, pref_id = input_pref_id, user_id = input_user_id
WHERE pref_id = pref_id_from_path;

--DEL http://localhost:8000/preferenceContain-delete/:pref_id

DELETE FROM preference_contain WHERE pref_id = input_pref_id;

--POST http://localhost:8000/preferredUni-create/

INSERT INTO preferred_uni (pref_id, preferred_uni_name, user_id)
VALUES (input_pref_id, input_uni_name, input_user_id);

--GET http://localhost:8000/preferredUni

SELECT * FROM preferred_uni;

--DEL http://localhost:8000/preferredUni-delete/:pref_id

DELETE FROM preferred_uni WHERE pref_id = input_pref_id;

--GET http://localhost:8000/university

SELECT * FROM university;

--GET http://localhost:8000/university/:name

SELECT * FROM university WHERE name = input_uni_name;

--GET http://localhost:8000/faculty

SELECT * FROM faculty;

--GET http://localhost:8000/professor

SELECT * FROM professor;

--GET http://localhost:8000/professor/:prof_id

SELECT * FROM professor WHERE prof_id = input_prof_id;

--GET http://localhost:8000/provides

SELECT * FROM provides;

--GET http://localhost:8000/major

SELECT * FROM major;

--GET http://localhost:8000/entryRequirement

SELECT * FROM entry_requirement;

--GET http://localhost:8000/equivalentClass

SELECT * FROM equivalent_class;

--GET http://localhost:8000/alumni

SELECT * FROM alumni;

--GET http://localhost:8000/alumni/:alumni_id

SELECT * FROM alumni WHERE alumni_id = input_alumni_id;

--GET http://localhost:8000/course

SELECT * FROM course;

--GET http://localhost:8000/ranking

SELECT * FROM ranking;

--GET http://localhost:8000/ranking/:uni_code

SELECT * FROM ranking WHERE uni_code = input_uni_code;

--GET http://localhost:8000/sport

SELECT * FROM sport;

--GET http://localhost:8000/award

SELECT * FROM award;

--GET http://localhost:8000/club

SELECT * FROM club;

--GET http://localhost:8000/extracurricularOfferings

SELECT * FROM extracurricular_offerings;

--GET http://localhost:8000/staff

SELECT * FROM staff;

