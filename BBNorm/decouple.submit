universe = vanilla
executable =  decouple.sh
arguments = "$(RUN)"

transfer_input_files = $(RUN)_out.fastq
request_cpus = 5

output = decouple_$(RUN).out
error =  decouple_$(RUN).err
log = decouple_$(RUN).log

transfer_executable = TRUE
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
transfer_input_files = $(RUN)_out.fastq

request_memory = 4GB
request_disk = 1GB

queue
