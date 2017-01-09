import paramiko
import time



def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(2)

    # Clear the buffer on the screen
    output = remote_conn.recv(10000)

    return output


if __name__ == '__main__':


    # VARIABLES THAT NEED CHANGED
    ip = '10.107.123.220'
    username = 'cliuser'
    password = 'cliuser'

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    # Strip the initial router prompt
    output = remote_conn.recv(10000)

    # See what we have
    print output

    # Turn off paging
    disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("show server inventory 1/1 expand  detail\n")
    remote_conn.send('quit\n')

    # Wait for the command to complete
    time.sleep(15)

    output = remote_conn.recv(10000)
    print output
    with open('result.txt','w') as f:
        f.write(output)