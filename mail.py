import smtplib

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ';'.join(to_addr_list)
    header += 'Cc: %s\n' % ';'.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    smtpserver = "LasSMTPInt.active.local"
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems
sendemail('soi_admins@activenetwork.com','john.yang@activenetwork.com','','hello python','hello')
