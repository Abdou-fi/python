# 
def mail_applicant(applicant: str, interviewer: str, date: str, time: str) -> str:
    msg = f'Dear {applicant}\nYou have been selected for an interview, you will be interviewed by {interviewer} on {date} at {time}.\nPlease confirm your attendance.\n'
    return msg

# test 
print(mail_applicant('Hana', 'Hamza', '2026-01-02', '10:00 AM'))

appoitment = ['Amine', 'Said', '2026-01-03', '09:00 AM']
print(mail_applicant(*appoitment))   # unpacking
