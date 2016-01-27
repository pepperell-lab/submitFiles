#This script creates individual submit files for each permutation run of BratNextGen. The files 'permutationInput.mat' and 'bratPermutationRun' must be present in the pwd.
for i in range(1,101):
    outFile = open(str(i)+"_BNGperm.submit", "w")
    outFile.write("universe = vanilla\n\
executable = /opt/PepPrograms/bratPackage_Linux/run_bratPermutationRun.sh\n\
arguments = "+"\""+"/opt/PepPrograms/MATLAB/MATLAB_Compiler_Runtime/v84/ "+str(i)+":"+str(i)+" permutationInput.mat ."+"\""+"\n\
transfer_input_files = permutationInput.mat,bratPermutationRun\nrequest_cpus = 1\n\n\n\
output = BNGperm.out\n\
error = BNGperm.err\n\
log = BNGperm.log\n\n\n\
transfer_executable = NO\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\n\
request_memory = 4GB\n\
request_disk = 1GB\n\n\n\
queue")

