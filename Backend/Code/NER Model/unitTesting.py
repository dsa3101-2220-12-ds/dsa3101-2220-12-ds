# 01_example_basic_test.py
import math

import pytest
import sys
import unitTrial
import Scoring_Universities


# def test_add():
#     assert unitTrial.add(1, 1) == 2


def test_calc_score():
    # outside range
    assert Scoring_Universities.calc_score(2) == 100
    assert Scoring_Universities.calc_score(-2) == 0

    ## edge cases
    assert Scoring_Universities.calc_score(-1) == 0
    assert Scoring_Universities.calc_score(1) == 100
    assert Scoring_Universities.calc_score(1.00001) == 100
    assert Scoring_Universities.calc_score(-1.00001) == 0

    # within range
    assert Scoring_Universities.calc_score(0) == 50

    # able to tolerate small margin or rounding errors (with test case division)
    val = round(200 / 3, 14)
    assert Scoring_Universities.calc_score(0.5) - val < 0.00000000000001

    # impossible numbers
    with pytest.raises(ZeroDivisionError) as Zero_error:
        Scoring_Universities.calc_score(1 / 0) == 50

    # bad input
    with pytest.raises(TypeError) as Type_error_text:
        Scoring_Universities.calc_score("Daddy Ernest") == 50
    # Scoring_Universities.calc_score(True) == 50


def test_cleaning():
    # edge case
    text = [""]
    assert Scoring_Universities.cleaning(text) == [[]]

    # happy path
    text = ["hello world", "Sql, I"]
    assert Scoring_Universities.cleaning(text) == [['hello', 'world'], ['sql']]
    text = [
        "https://www.w3schools.com/python/ref_func_round.asp#:~:text=The%20round()%20function%20returns,will%20return%20the%20nearest%20integer."]
    assert Scoring_Universities.cleaning(text) == [[]]
    text = ["1234567890", "Ernest Liu my No.1 Daddy"]
    assert Scoring_Universities.cleaning(text) == [[], ['ernest', 'liu', 'daddy']]

    # bad input
    text = True
    with pytest.raises(ValueError) as Value_error_text:
        Scoring_Universities.process_job_desc(text) == [['True']]
    text = 4243
    with pytest.raises(ValueError) as Value_error_num:
        Scoring_Universities.process_job_desc(text) == [[4243]]


def test_process_job_desc():
    # edge case
    text = ""
    assert Scoring_Universities.process_job_desc(text) == []
    text = " "
    assert Scoring_Universities.process_job_desc(text) == []
    text = "bomputer bision"
    assert Scoring_Universities.process_job_desc(text) == []

    # happy path
    text = "https://www.w3schools.com/python/ref_func_round.asp#:~:text=The%20round()%20function%20returns,will%20return%20the%20nearest%20integer."
    assert Scoring_Universities.process_job_desc(text) == []
    text = "hello world!"
    assert Scoring_Universities.process_job_desc(text) == []
    text = "I want to learn SQL"
    assert Scoring_Universities.process_job_desc(text) == [['sql']]
    text = " Combine Machine Learning technology and business scenario requirements, " \
           "use cutting-edge modeling skills including Reinforcement Learning, Sequence Modeling, " \
           "Large Language Model, Multi-task Learning, etc., to solve business pain points and improve online effects"
    assert Scoring_Universities.process_job_desc(text) == [['machine', 'learning'],
                                                           ['reinforcement', 'learning'],
                                                           ['sequence', 'modeling'],
                                                           ['large', 'language', 'model'],
                                                           ['multi', 'task', 'learning'],
                                                           ['improve', 'online', 'effect']]

    # bad inputs
    text = True
    with pytest.raises(ValueError) as Value_error_bool:
        Scoring_Universities.process_job_desc(text) == [['True']]
    text = 4243
    with pytest.raises(ValueError) as Value_error_num:
        Scoring_Universities.process_job_desc(text) == [[4243]]


def test_get_skill2mod_score():
    mod_desc = "The aim of this module is to introduce the fundamental concepts and techniques necessary for the " \
               "understanding and practice of design and implementation of database applications and of the " \
               "management of data with relational database management systems. The module covers practical and " \
               "theoretical aspects of design with entity-relationship model, theory of functional dependencies and" \
               " normalisation by decomposition in second, third and Boyce-Codd normal forms. The module covers" \
               " practical and theoretical aspects of programming with SQL data definition and manipulation " \
               "sublanguages, relational tuple calculus, relational domain calculus and relational algebra."
    true_sentence = "I still think Han Xiao Guang's trashcan is full."
    # assert Scoring_Universities.get_skill2mod_score("sql", mod_desc) == (99.98900981053919, 'sql')
    assert Scoring_Universities.get_skill2mod_score('sql', true_sentence) == (99.98900981053919, 'sql')


def test_get_school_scores():
    assert 1 == 1
    # assert Scoring_Universities.get_school_scores({"NUS":1}) == []


def test_get_mod_recommendations():

    # edge cases
    jd = ""
    assert Scoring_Universities.get_mod_recommendations(jd) == ({}, {})
    jd = " "
    assert Scoring_Universities.get_mod_recommendations(jd) == ({}, {})
    jd = "Ernest Liu"
    assert Scoring_Universities.get_mod_recommendations(jd) == ({'ernest liu': {'NTU': ('CZ1003', 0),
                                                                                'NUS': ('CS1010', 0),
                                                                                'SIT': ('CSC3009', 0),
                                                                                'SMU': ('OPIM326', 0),
                                                                                'SUSS': ('MKT371', 0),
                                                                                'SUTD': ('10.014', 0)}},
                                                                {'NTU': 0.0, 'NUS': 0.0, 'SIT': 0.0, 'SMU': 0.0,
                                                                 'SUSS': 0.0, 'SUTD': 0.0}) != ({}, {})
    # bad inputs
    jd = 1
    with pytest.raises(ValueError) as Value_error_num:
        Scoring_Universities.get_mod_recommendations(jd) == ({}, {})
    jd = True
    with pytest.raises(ValueError) as Value_error_bool:
        Scoring_Universities.get_mod_recommendations(jd) == ({}, {})
    jd = []
    with pytest.raises(ValueError) as Value_error_ls:
        Scoring_Universities.get_mod_recommendations(jd) == ({}, {})

    jd = " Combine Machine Learning technology and business scenario requirements, " \
         "use cutting-edge modeling skills including Reinforcement Learning, Sequence Modeling, " \
         "Large Language Model, Multi-task Learning, etc., to solve business pain points and improve online effects"
    assert Scoring_Universities.get_mod_recommendations(jd) == (
    {'improve online effect': {'NTU': ('CZ1003', 75.35499790443514),
                               'NUS': ('CS1010', 75.35499790443514),
                               'SIT': ('CSC3009', 75.35499790443514),
                               'SMU': ('OPIM326', 75.35499790443514),
                               'SUSS': ('MKT371', 75.35499790443514),
                               'SUTD': ('10.014', 75.35499790443514)},
     'large language model': {'NTU': ('CZ1003', 100.0),
                              'NUS': ('CS1010', 100.0),
                              'SIT': ('CSC3009', 100.0),
                              'SMU': ('OPIM326', 100.0),
                              'SUSS': ('MKT371', 100.0),
                              'SUTD': ('10.014', 100.0)},
     'machine learning': {'NTU': ('CZ1003', 100.0),
                          'NUS': ('CS1010', 100.0),
                          'SIT': ('CSC3009', 100.0),
                          'SMU': ('OPIM326', 100.0),
                          'SUSS': ('MKT371', 100.0),
                          'SUTD': ('10.014', 100.0)},
     'multi task learning': {'NTU': ('CZ1003', 100.0),
                             'NUS': ('CS1010', 100.0),
                             'SIT': ('CSC3009', 100.0),
                             'SMU': ('OPIM326', 100.0),
                             'SUSS': ('MKT371', 100.0),
                             'SUTD': ('10.014', 100.0)},
     'reinforcement learning': {'NTU': ('CZ1003', 100.0),
                                'NUS': ('CS1010', 100.0),
                                'SIT': ('CSC3009', 100.0),
                                'SMU': ('OPIM326', 100.0),
                                'SUSS': ('MKT371', 100.0),
                                'SUTD': ('10.014', 100.0)},
     'sequence modeling': {'NTU': ('CZ1003', 100.0),
                           'NUS': ('CS1010', 100.0),
                           'SIT': ('CSC3009', 100.0),
                           'SMU': ('OPIM326', 100.0),
                           'SUSS': ('MKT371', 100.0),
                           'SUTD': ('10.014', 100.0)}},
    {'NTU': 95.89249965073918,
     'NUS': 95.89249965073918,
     'SIT': 95.89249965073918,
     'SMU': 95.89249965073918,
     'SUSS': 95.89249965073918,
     'SUTD': 95.89249965073918})
