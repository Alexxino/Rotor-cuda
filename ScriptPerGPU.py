import subprocess

base_command = './clientRotorCudaX64 -prog Rotor -d {device_ids} -name Vast{gpu_id} -pass x -pool 213.242.45.187:8000 -b 256,256 -nopow'

processes = []

for i in range(8):
    command = base_command.format(device_ids=i, gpu_id=i)
    processes.append(subprocess.Popen(command, shell=True))

for proc in processes:
    proc.wait()