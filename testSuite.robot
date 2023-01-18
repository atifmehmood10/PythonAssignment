*** Settings ***
Suite Setup    Setup this suite
Library     OperatingSystem
Library     RequestsLibrary
Library     Process

*** Variables ***

*** Test Cases ***
GetPeopleValidTest
    ${response}=  GET On Session  mysession  people/1       expected_status=200

GetPeopleInvalidTest
    ${response}=  GET On Session  mysession  people/200     expected_status=404

GetPlanetsValidTest
    ${response}=  GET On Session  mysession  planets/1      expected_status=200

GetPlanetsInvalidTest
    ${response}=  GET On Session  mysession  planets/200     expected_status=404

GetStarshipsValidTest
    ${response}=  GET On Session  mysession  starships/1        expected_status=200

GetStarshipsInvalidTest
    ${response}=  GET On Session  mysession  starships/200      expected_status=404


*** Keywords ***
Setup this suite
    Create Session  mysession  http://127.0.0.1:5050/
