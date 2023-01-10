This code uses the os.path module to get the current directory of the source code and creates a file results.txt in the same directory. then it reads CIDR notations from the 'cidrs.txt' file, converts each one to a list of IP addresses, then saves each list of IP addresses to the file results.txt using the save_to_file function and the 'a' mode to append the data to the file.

You can run this program by running python filename.py in your terminal, provided you have a file named 'cidrs.txt' in the same directory as your source code, containing one CIDR notation per line.

If you want to keep the file results.txt always a new one, you can replace 'a' with 'w' in with open(filepath, 'a') as f:
