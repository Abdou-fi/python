applicant=input("Enter the applicant's name: ")
interviewer ='aissa'
time = input("Enter the appointment time: ")

print(interviewer + ' will interview ' + applicant  + ' at ' + time +'.')
print(interviewer, 'will interview', applicant, 'at', time, '.', sep='-')
print(f'{interviewer} will interview {applicant} at {time}.')
print('{} will interview {} at {}.'.format(interviewer, applicant, time))