#Change these two variables.
NO_TEST_CASES=10
MANUAL_TEST_CASES=0


rm testcases-to-upload.zip
rm -r testcases
mkdir testcases testcases/input testcases/outputJava testcases/outputPython testcases/outputC

javac solutions/Solution.java
mv solutions/Solution.class testcases/

gcc solutions/Solution.c -o solutions/SolutionC
mv solutions/SolutionC testcases/

cp solutions/Solution.py testcases/

python testcase-gen.py -fnp testcases/input/input -s $MANUAL_TEST_CASES -e $NO_TEST_CASES

python bash-gen.py -s 0 -e $NO_TEST_CASES -o testcases/java.sh -l 'java Solution < input/input{:02d}.txt > outputJava/output{:02d}.txt'
python bash-gen.py -s 0 -e $NO_TEST_CASES -o testcases/c.sh -l './SolutionC < input/input{:02d}.txt > outputC/output{:02d}.txt'
python bash-gen.py -s 0 -e $NO_TEST_CASES -o testcases/python.sh -l 'python Solution.py < input/input{:02d}.txt > outputPython/output{:02d}.txt'

python bash-gen.py -s 0 -e $NO_TEST_CASES -o testcases/checkJavaC.sh -l 'diff outputJava/output{:02d}.txt  outputC/output{:02d}.txt'
python bash-gen.py -s 0 -e $NO_TEST_CASES -o testcases/checkJavaPython.sh -l 'diff outputJava/output{:02d}.txt  outputPython/output{:02d}.txt'

cd testcases/
chmod 700 *.sh

./java.sh
./c.sh
./python.sh

cp -r outputJava/ output/
zip -r testcases.zip . -i input/input* output/output* > zipLog.txt
mv testcases.zip ../testcases-to-upload.zip

echo "Running tests Java - C"
./checkJavaC.sh
echo "Running tests Java - Python"
./checkJavaPython.sh
echo "If no error, upload testcases-to-upload.zip"
echo "End of prog"
