Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> firstFile = input("Enter the input filename with extension ");
Enter the input filename with extension myfile.txt
>>> secondFile = input("Enter the output filename with extension ");
Enter the output filename with extension intergers.txt
>>> f1 = open(firstFile, "r");
>>> f2 = open(secondFile, "w+");
>>> content = f1.read();
>>> f2.write(content);
36
>>> f1.close()
>>> f2.close()
