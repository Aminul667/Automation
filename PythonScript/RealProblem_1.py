# You want to write a program that replaces this old domain with the new one in any outdated email addresses. The function to replace the 
# domain would look like this.

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("rahatkhan@company.com", "company.com", "agency.gov"))