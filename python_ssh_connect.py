import paramiko
from pathos.multiprocessing import ProcessingPool

hosts = ["ec2-52-41-29-66.us-west-2.compute.amazonaws.com", "ec2-34-217-74-31.us-west-2.compute.amazonaws.com"]

def execute_commands(host_name, commands_list=[]):
    k = paramiko.RSAKey.from_private_key_file("/Users/sa20099277/Downloads/sagar_key_pair.pem")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(hostname = host_name, username = "ec2-user", pkey = k)
    for command in commands_list:
        stdin , stdout, stderr = c.exec_command(command)
        stdout.channel.set_combine_stderr(True)
        output = stdout.readlines()
	print "Output of command {0} in host {1} is {2}".format(command, host_name, output)
    print "Commands execution for host {} is completed".format(host_name)


if __name__ == '__main__':

    for i in range(0,2):
    	print "Enter the commands to be executed on the remote hosts, comma seperate or a list"
    	commands_list = list(input())
    	pool = ProcessingPool(nodes=len(hosts))
    	outputs = pool.map(execute_commands, hosts, [commands_list, commands_list])
