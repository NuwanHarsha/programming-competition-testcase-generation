mkdir walk
mkdir walk/input
mkdir walk/output
javac WalkSolution.java
mv WalkSolution.class walk/
python walk-to-remember-testcase-gen.py -fnp walk/input/input
python bash-gen.py -s 0 -e 10 -o walk/gen.sh -l 'java WalkSolution < input/input{:02d}.txt > output/output{:02d}.txt'
cd walk
chmod 700 gen.sh
./gen.sh
