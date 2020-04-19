# programming-competition-testcase-generation

This is a tool written to generate testcases for Hackerrank competitions. This tool should run on bash shell (preferably linux).

## Example usecase

This repository contains the code for the following question.

Q: You are required to write a program to compute the radius of circles. The first line of input is an integer (T) denoting the number of circles. The next T lines contains one floating point number each, denoting the radius of the circle.

You should output T lines containing one floating point number denoting the radius of the circle. The answer should be output to the nearest 3 decimal places.

The example contains code for Java, Python and C. In practice, you can go with one or many languages.

## First run

<code>sudo apt-get install zip</code>

# How to use

1. Run the following shell commands
```bash
git clone https://github.com/gihanjayatilaka/programming-competition-testcase-generation.git
cd programming-competition-testcase-generation  
chmod 700 run.sh  
```

2. Insert your solutions to **solutions** folder
3. Update **testcase-gen.py**

4. Run the following shell command
<code>./run.sh</code>

5. If no error occurs, upload the **testcases-to-upload.zip** to Hackerrank.com


## Help

[Contact me](https://gihan.me/contact/) for any queries.

## Extra : Plagiarism checking

* Download the submissions using [https://github.com/kasvith/hackerrank-dl](https://github.com/kasvith/hackerrank-dl).
* Check for plagiarism using any tool.
